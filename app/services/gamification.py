from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.daily_log import DailyLog
from app.models.dsa import DSAProblem
from app.models.system_design import SystemDesignSubConcept, SystemDesignCase
from app.models.ai_llm import AILLMTopic
from app.models.github import GithubTask
from app.models.application import Application
from app.services import analytics

LEVEL_TITLES = [
    (1, "Prep Novice"),
    (3, "Syntax Scholar"),
    (5, "Algorithm Apprentice"),
    (7, "Concurrency Cadet"),
    (9, "Data Structurer"),
    (11, "System Designer"),
    (13, "Backend Craftsman"),
    (15, "Distributed Architect"),
    (17, "AI Specialist"),
    (19, "Principal Candidate"),
    (22, "Systems Demigod"),
]

ACHIEVEMENT_SCHEMAS = {
    "streak": {
        "title": "Consistent Grind",
        "icon": "🔥",
        "description": "Consecutive days logging study sessions.",
        "unit": "days",
        "tiers": [
            {"tier": "Bronze", "threshold": 3, "bonus": 100, "badge": "🥉"},
            {"tier": "Silver", "threshold": 7, "bonus": 250, "badge": "🥈"},
            {"tier": "Gold", "threshold": 14, "bonus": 600, "badge": "🥇"},
            {"tier": "Platinum", "threshold": 30, "bonus": 1500, "badge": "🏆"},
        ]
    },
    "hours": {
        "title": "Clocking Hours",
        "icon": "⏱️",
        "description": "Total hours spent studying core topics.",
        "unit": "hours",
        "tiers": [
            {"tier": "Bronze", "threshold": 10, "bonus": 100, "badge": "🥉"},
            {"tier": "Silver", "threshold": 50, "bonus": 250, "badge": "🥈"},
            {"tier": "Gold", "threshold": 120, "bonus": 600, "badge": "🥇"},
            {"tier": "Platinum", "threshold": 300, "bonus": 1500, "badge": "🏆"},
        ]
    },
    "dsa": {
        "title": "Algorithm Decimator",
        "icon": "💻",
        "description": "LeetCode & DSA problems marked Solved.",
        "unit": "problems",
        "tiers": [
            {"tier": "Bronze", "threshold": 10, "bonus": 100, "badge": "🥉"},
            {"tier": "Silver", "threshold": 50, "bonus": 250, "badge": "🥈"},
            {"tier": "Gold", "threshold": 150, "bonus": 600, "badge": "🥇"},
            {"tier": "Platinum", "threshold": 250, "bonus": 1500, "badge": "🏆"},
        ]
    },
    "sys_design": {
        "title": "System Architect",
        "icon": "🏗️",
        "description": "System Design concepts and cases completed.",
        "unit": "topics",
        "tiers": [
            {"tier": "Bronze", "threshold": 3, "bonus": 100, "badge": "🥉"},
            {"tier": "Silver", "threshold": 10, "bonus": 250, "badge": "🥈"},
            {"tier": "Gold", "threshold": 20, "bonus": 600, "badge": "🥇"},
            {"tier": "Platinum", "threshold": 28, "bonus": 1500, "badge": "🏆"},
        ]
    },
    "ai_llm": {
        "title": "AI Specialist",
        "icon": "🤖",
        "description": "AI / RAG / Agent topics completed.",
        "unit": "topics",
        "tiers": [
            {"tier": "Bronze", "threshold": 3, "bonus": 100, "badge": "🥉"},
            {"tier": "Silver", "threshold": 10, "bonus": 250, "badge": "🥈"},
            {"tier": "Gold", "threshold": 18, "bonus": 600, "badge": "🥇"},
            {"tier": "Platinum", "threshold": 22, "bonus": 1500, "badge": "🏆"},
        ]
    },
    "github": {
        "title": "Open Source Builder",
        "icon": "🐙",
        "description": "Portfolio GitHub project tasks marked Done.",
        "unit": "tasks",
        "tiers": [
            {"tier": "Bronze", "threshold": 5, "bonus": 100, "badge": "🥉"},
            {"tier": "Silver", "threshold": 15, "bonus": 250, "badge": "🥈"},
            {"tier": "Gold", "threshold": 30, "bonus": 600, "badge": "🥇"},
            {"tier": "Platinum", "threshold": 40, "bonus": 1500, "badge": "🏆"},
        ]
    },
    "applications": {
        "title": "Career Hunter",
        "icon": "📤",
        "description": "Job applications added & tracked.",
        "unit": "applications",
        "tiers": [
            {"tier": "Bronze", "threshold": 2, "bonus": 100, "badge": "🥉"},
            {"tier": "Silver", "threshold": 8, "bonus": 250, "badge": "🥈"},
            {"tier": "Gold", "threshold": 15, "bonus": 600, "badge": "🥇"},
            {"tier": "Platinum", "threshold": 25, "bonus": 1500, "badge": "🏆"},
        ]
    },
}


def get_level_title(level: int) -> str:
    title = "Prep Novice"
    for lvl_threshold, name in LEVEL_TITLES:
        if level >= lvl_threshold:
            title = name
    return title


def get_level_data(xp: float) -> dict:
    """Calculates user level based on XP using: xp = 50 * level * (level - 1)."""
    level = 1
    while True:
        next_xp = 50 * level * (level + 1)
        if xp >= next_xp:
            level += 1
        else:
            break
            
    current_level_xp = 50 * (level - 1) * level
    next_level_xp = 50 * level * (level + 1)
    
    xp_in_level = xp - current_level_xp
    xp_needed_in_level = next_level_xp - current_level_xp
    
    pct_progress = round((xp_in_level / xp_needed_in_level * 100) if xp_needed_in_level > 0 else 0)
    
    return {
        "level": level,
        "title": get_level_title(level),
        "total_xp": int(xp),
        "current_boundary": current_level_xp,
        "next_boundary": next_level_xp,
        "xp_in_level": int(xp_in_level),
        "xp_needed_for_next": int(next_level_xp - xp),
        "pct_progress": min(pct_progress, 100)
    }


def get_gamification_state(db: Session) -> dict:
    """Computes all stats, XP, achievement tiers, and leveling boundaries."""
    
    # 1. Gather raw inputs
    total_hours = analytics.get_total_hours(db)
    streak = analytics.get_streak(db)
    
    # DSA Solved Problems by difficulty
    solved_easy = db.query(DSAProblem).filter(DSAProblem.status == "Solved", DSAProblem.difficulty == "Easy").count()
    solved_medium = db.query(DSAProblem).filter(DSAProblem.status == "Solved", DSAProblem.difficulty == "Medium").count()
    solved_hard = db.query(DSAProblem).filter(DSAProblem.status == "Solved", DSAProblem.difficulty == "Hard").count()
    total_dsa = solved_easy + solved_medium + solved_hard
    
    # System Design Done SubConcepts + Cases
    sd_concepts_done = db.query(SystemDesignSubConcept).filter(SystemDesignSubConcept.status == "Done").count()
    sd_cases_done = db.query(SystemDesignCase).filter(SystemDesignCase.status == "Done").count()
    total_sys_design = sd_concepts_done + sd_cases_done
    
    # AI/LLM Done Topics
    total_ai_llm = db.query(AILLMTopic).filter(AILLMTopic.status == "Done").count()
    
    # GitHub Done Tasks
    total_github = db.query(GithubTask).filter(GithubTask.done == True).count()
    
    # Applications added
    total_apps = db.query(Application).count()
    
    # 2. Calculate Base XP
    base_xp = 0.0
    base_xp += total_hours * 10.0
    base_xp += solved_easy * 10.0
    base_xp += solved_medium * 25.0
    base_xp += solved_hard * 50.0
    base_xp += total_ai_llm * 20.0
    base_xp += sd_concepts_done * 20.0
    base_xp += sd_cases_done * 40.0
    base_xp += total_github * 15.0
    base_xp += total_apps * 10.0
    base_xp += streak * 5.0
    
    # Map key metric types to actual calculated values
    metrics_map = {
        "streak": streak,
        "hours": total_hours,
        "dsa": total_dsa,
        "sys_design": total_sys_design,
        "ai_llm": total_ai_llm,
        "github": total_github,
        "applications": total_apps,
    }
    
    # 3. Process achievements and sum bonuses
    achievements_list = []
    bonus_xp = 0
    
    for key, schema in ACHIEVEMENT_SCHEMAS.items():
        current_value = metrics_map[key]
        tiers_status = []
        active_tier = None
        next_tier = None
        
        for t in schema["tiers"]:
            unlocked = current_value >= t["threshold"]
            tiers_status.append({
                "tier": t["tier"],
                "threshold": t["threshold"],
                "bonus": t["bonus"],
                "badge": t["badge"],
                "unlocked": unlocked
            })
            if unlocked:
                bonus_xp += t["bonus"]
                active_tier = t
            elif next_tier is None:
                next_tier = t
        
        # Calculate progress towards next tier
        if next_tier:
            prev_threshold = 0
            if active_tier:
                # Find index
                idx = schema["tiers"].index(active_tier)
                prev_threshold = schema["tiers"][idx]["threshold"]
            
            sub_progress = current_value - prev_threshold
            sub_target = next_tier["threshold"] - prev_threshold
            progress_pct = round((sub_progress / sub_target * 100) if sub_target > 0 else 0)
            progress_pct = max(0, min(100, progress_pct))
        else:
            progress_pct = 100
            
        achievements_list.append({
            "key": key,
            "title": schema["title"],
            "icon": schema["icon"],
            "description": schema["description"],
            "unit": schema["unit"],
            "current_value": current_value,
            "tiers": tiers_status,
            "active_tier": active_tier["tier"] if active_tier else "None",
            "active_badge": active_tier["badge"] if active_tier else "🔒",
            "next_tier_name": next_tier["tier"] if next_tier else "Maxed",
            "next_tier_threshold": next_tier["threshold"] if next_tier else current_value,
            "next_tier_badge": next_tier["badge"] if next_tier else "⭐",
            "progress_pct": progress_pct
        })
        
    total_xp = base_xp + bonus_xp
    
    # 4. Calculate Level details
    level_details = get_level_data(total_xp)
    
    # Summary stats for badges unlocked
    total_badges = sum(1 for a in achievements_list if a["active_tier"] != "None")
    total_tiers_possible = len(ACHIEVEMENT_SCHEMAS)
    
    return {
        "level_details": level_details,
        "achievements": achievements_list,
        "metrics": metrics_map,
        "base_xp": int(base_xp),
        "bonus_xp": bonus_xp,
        "total_badges_unlocked": total_badges,
        "total_badges_possible": total_tiers_possible,
    }
