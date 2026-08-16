from datetime import date
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.daily_log import DailyLog
from app.models.dsa import DSAProblem
from app.models.system_design import SystemDesignSubConcept, SystemDesignCase
from app.models.ai_llm import AILLMTopic
from app.models.github import GithubTask
from app.models.application import Application
from app.services import analytics

# ══════════════════════════════════════════════════════════════════════════════
# 1. RANK TIERS & 30-LEVEL SYSTEM DEFINITIONS
# ══════════════════════════════════════════════════════════════════════════════

RANK_TIERS = [
    {
        "id": "apprentice",
        "name": "Apprentice",
        "min_level": 1,
        "max_level": 3,
        "icon": "sprout",
        "color": "#10B981",
        "bg_gradient": "linear-gradient(135deg, #10B981, #059669)",
        "badge_class": "rank-apprentice",
        "tagline": "Initiate of the Codebase",
    },
    {
        "id": "practitioner",
        "name": "Practitioner",
        "min_level": 4,
        "max_level": 6,
        "icon": "terminal",
        "color": "#0EA5E9",
        "bg_gradient": "linear-gradient(135deg, #0EA5E9, #0284C7)",
        "badge_class": "rank-practitioner",
        "tagline": "Syntax & Logic Craftsman",
    },
    {
        "id": "engineer",
        "name": "Engineer",
        "min_level": 7,
        "max_level": 9,
        "icon": "code-2",
        "color": "#6366F1",
        "bg_gradient": "linear-gradient(135deg, #6366F1, #4F46E5)",
        "badge_class": "rank-engineer",
        "tagline": "Data Structures & Core Systems",
    },
    {
        "id": "senior_specialist",
        "name": "Senior Specialist",
        "min_level": 10,
        "max_level": 13,
        "icon": "server",
        "color": "#8B5CF6",
        "bg_gradient": "linear-gradient(135deg, #8B5CF6, #7C3AED)",
        "badge_class": "rank-senior",
        "tagline": "Architecture & Scalability Master",
    },
    {
        "id": "staff_architect",
        "name": "Staff Architect",
        "min_level": 14,
        "max_level": 17,
        "icon": "layers",
        "color": "#EC4899",
        "bg_gradient": "linear-gradient(135deg, #EC4899, #DB2777)",
        "badge_class": "rank-staff",
        "tagline": "Distributed Systems & AI Engineer",
    },
    {
        "id": "principal_engineer",
        "name": "Principal Engineer",
        "min_level": 18,
        "max_level": 21,
        "icon": "gem",
        "color": "#F59E0B",
        "bg_gradient": "linear-gradient(135deg, #F59E0B, #D97706)",
        "badge_class": "rank-principal",
        "tagline": "Enterprise Visionary & Technical Titan",
    },
    {
        "id": "distinguished_demigod",
        "name": "Distinguished Demigod",
        "min_level": 22,
        "max_level": 25,
        "icon": "flame",
        "color": "#EF4444",
        "bg_gradient": "linear-gradient(135deg, #EF4444, #DC2626)",
        "badge_class": "rank-demigod",
        "tagline": "High-Scale Ascendant & Tech Luminary",
    },
    {
        "id": "mythic_legend",
        "name": "Mythic Legend",
        "min_level": 26,
        "max_level": 999,
        "icon": "crown",
        "color": "#A855F7",
        "bg_gradient": "linear-gradient(135deg, #A855F7, #EC4899, #EAB308)",
        "badge_class": "rank-mythic",
        "tagline": "Transcendent Engineering God",
    },
]

LEVEL_DEFINITIONS = [
    {"level": 1,  "title": "Code Initiate",            "icon": "sprout",        "perk": "Unlocks Daily Quests & Core DSA Tracker"},
    {"level": 2,  "title": "Syntax Explorer",          "icon": "sparkles",      "perk": "+5% Streak Multiplier Bonus"},
    {"level": 3,  "title": "Bug Hunter",               "icon": "shield",        "perk": "Unlocks Bronze Milestone Badges"},
    {"level": 4,  "title": "Algorithm Apprentice",     "icon": "terminal",      "perk": "+10 XP bonus on Medium DSA Solves"},
    {"level": 5,  "title": "Data Structurer",          "icon": "binary",        "perk": "Unlocks Badge Showcase & Trophy Case"},
    {"level": 6,  "title": "Logic Specialist",         "icon": "zap",           "perk": "+10% Deep Work Study XP Bonus"},
    {"level": 7,  "title": "Backend Craftsman",        "icon": "code-2",        "perk": "Unlocks System Design Tracker & Silver Badges"},
    {"level": 8,  "title": "Concurrency Cadet",        "icon": "cpu",           "perk": "+15 XP bonus on Hard DSA Solves"},
    {"level": 9,  "title": "Performance Tuner",        "icon": "gauge",         "perk": "Unlocks Silver Profile Border Flair"},
    {"level": 10, "title": "Senior Backend Pro",       "icon": "server",        "perk": "Unlocks Weekly Sprint Multiplier"},
    {"level": 11, "title": "System Designer",          "icon": "network",       "perk": "+20 XP bonus on Case Studies"},
    {"level": 12, "title": "Microservices Maven",      "icon": "boxes",         "perk": "Unlocks AI & LLM Pioneer Roadmap"},
    {"level": 13, "title": "API Architect",            "icon": "workflow",      "perk": "Unlocks Gold Profile Border Flair"},
    {"level": 14, "title": "Distributed Architect",    "icon": "layers",        "perk": "Unlocks Gold Milestone Badges"},
    {"level": 15, "title": "High-Scale Strategist",    "icon": "activity",      "perk": "+15% Streak Multiplier Boost"},
    {"level": 16, "title": "AI Systems Pioneer",       "icon": "bot",           "perk": "+25 XP bonus on Agent Architectures"},
    {"level": 17, "title": "RAG & LLM Master",         "icon": "sparkles",      "perk": "Unlocks Platinum Profile Border Flair"},
    {"level": 18, "title": "Principal Candidate",      "icon": "gem",           "perk": "Unlocks Platinum Milestone Badges"},
    {"level": 19, "title": "Enterprise Visionary",     "icon": "compass",       "perk": "+20% Total XP Multiplier Boost"},
    {"level": 20, "title": "Technical Titan",          "icon": "shield-check",  "perk": "Unlocks Diamond Hall of Fame Trophies"},
    {"level": 21, "title": "Systems Grandmaster",      "icon": "award",         "perk": "Unlocks Senior Staff Candidate Title"},
    {"level": 22, "title": "Systems Demigod",          "icon": "flame",         "perk": "Unlocks Demigod Aura & Glowing Avatar"},
    {"level": 23, "title": "Cloud Sovereign",          "icon": "cloud-lightning","perk": "Unlocks Obsidian Tier Badges"},
    {"level": 24, "title": "Infrastructure Deity",     "icon": "database",      "perk": "Unlocks Grandmaster Title & Perks"},
    {"level": 25, "title": "Architecture Ascendant",   "icon": "star",          "perk": "+25% Streak Multiplier Boost"},
    {"level": 26, "title": "Interview Conqueror",      "icon": "trophy",        "perk": "Unlocks Mythic Crown Badge"},
    {"level": 27, "title": "Algorithmic Oracle",       "icon": "eye",           "perk": "Master of all DSA Patterns"},
    {"level": 28, "title": "Chief AI Architect",       "icon": "cpu",           "perk": "Supreme Modern AI Stack Mastery"},
    {"level": 29, "title": "Supreme Tech Fellow",      "icon": "medal",         "perk": "Unlocks Legendary Profile Ribbon"},
    {"level": 30, "title": "Transcendent Engineer",    "icon": "crown",         "perk": "Engineering Perfection Reached"},
]


# ══════════════════════════════════════════════════════════════════════════════
# 2. ENHANCED ACHIEVEMENT SCHEMAS (11 Tracks across 5 Categories)
# ══════════════════════════════════════════════════════════════════════════════

ACHIEVEMENT_SCHEMAS = {
    # ── Category 1: Discipline & Grind ──
    "streak": {
        "title": "Unbroken Discipline",
        "category": "grind",
        "category_name": "Discipline & Grind",
        "icon": "flame",
        "lucide_icon": "flame",
        "description": "Consecutive days logging active study sessions.",
        "unit": "days",
        "tiers": [
            {"tier": "Bronze",   "threshold": 3,  "bonus": 100,  "badge": "Bronze"},
            {"tier": "Silver",   "threshold": 7,  "bonus": 250,  "badge": "Silver"},
            {"tier": "Gold",     "threshold": 14, "bonus": 600,  "badge": "Gold"},
            {"tier": "Platinum", "threshold": 30, "bonus": 1500, "badge": "Platinum"},
            {"tier": "Diamond",  "threshold": 60, "bonus": 3000, "badge": "Diamond"},
        ]
    },
    "hours": {
        "title": "Deep Work Marathon",
        "category": "grind",
        "category_name": "Discipline & Grind",
        "icon": "clock",
        "lucide_icon": "clock",
        "description": "Cumulative focused hours dedicated to prep.",
        "unit": "hours",
        "tiers": [
            {"tier": "Bronze",   "threshold": 10,  "bonus": 100,  "badge": "Bronze"},
            {"tier": "Silver",   "threshold": 50,  "bonus": 250,  "badge": "Silver"},
            {"tier": "Gold",     "threshold": 120, "bonus": 600,  "badge": "Gold"},
            {"tier": "Platinum", "threshold": 250, "bonus": 1500, "badge": "Platinum"},
            {"tier": "Diamond",  "threshold": 400, "bonus": 3500, "badge": "Diamond"},
        ]
    },
    "weekend_warrior": {
        "title": "Weekend Crusher",
        "category": "grind",
        "category_name": "Discipline & Grind",
        "icon": "calendar-heart",
        "lucide_icon": "calendar-heart",
        "description": "Weekend study hours logged on Saturday and Sunday.",
        "unit": "hours",
        "tiers": [
            {"tier": "Bronze",   "threshold": 8,   "bonus": 100,  "badge": "Bronze"},
            {"tier": "Silver",   "threshold": 25,  "bonus": 250,  "badge": "Silver"},
            {"tier": "Gold",     "threshold": 60,  "bonus": 600,  "badge": "Gold"},
            {"tier": "Platinum", "threshold": 120, "bonus": 1500, "badge": "Platinum"},
        ]
    },

    # ── Category 2: Algorithm Decimator (DSA) ──
    "dsa": {
        "title": "Algorithm Decimator",
        "category": "dsa",
        "category_name": "Algorithms (DSA)",
        "icon": "code-2",
        "lucide_icon": "code-2",
        "description": "Total LeetCode & DSA problems marked Solved.",
        "unit": "problems",
        "tiers": [
            {"tier": "Bronze",   "threshold": 15,  "bonus": 150,  "badge": "Bronze"},
            {"tier": "Silver",   "threshold": 50,  "bonus": 350,  "badge": "Silver"},
            {"tier": "Gold",     "threshold": 120, "bonus": 800,  "badge": "Gold"},
            {"tier": "Platinum", "threshold": 200, "bonus": 2000, "badge": "Platinum"},
            {"tier": "Diamond",  "threshold": 250, "bonus": 4000, "badge": "Diamond"},
        ]
    },
    "dsa_medium": {
        "title": "Medium Problem Crusher",
        "category": "dsa",
        "category_name": "Algorithms (DSA)",
        "icon": "zap",
        "lucide_icon": "zap",
        "description": "Medium difficulty DSA problems solved.",
        "unit": "problems",
        "tiers": [
            {"tier": "Bronze",   "threshold": 10,  "bonus": 150,  "badge": "Bronze"},
            {"tier": "Silver",   "threshold": 35,  "bonus": 350,  "badge": "Silver"},
            {"tier": "Gold",     "threshold": 75,  "bonus": 750,  "badge": "Gold"},
            {"tier": "Platinum", "threshold": 150, "bonus": 2000, "badge": "Platinum"},
        ]
    },
    "dsa_hard": {
        "title": "Hard Mode Slayer",
        "category": "dsa",
        "category_name": "Algorithms (DSA)",
        "icon": "flame",
        "lucide_icon": "flame",
        "description": "Hard difficulty DSA problems conquered.",
        "unit": "problems",
        "tiers": [
            {"tier": "Bronze",   "threshold": 2,  "bonus": 150,  "badge": "Bronze"},
            {"tier": "Silver",   "threshold": 8,  "bonus": 400,  "badge": "Silver"},
            {"tier": "Gold",     "threshold": 20, "bonus": 1000, "badge": "Gold"},
            {"tier": "Platinum", "threshold": 40, "bonus": 2500, "badge": "Platinum"},
        ]
    },

    # ── Category 3: System Design & Architecture ──
    "sys_concepts": {
        "title": "High-Scale Architect",
        "category": "sys_design",
        "category_name": "System Design",
        "icon": "network",
        "lucide_icon": "network",
        "description": "System Design core building blocks completed.",
        "unit": "concepts",
        "tiers": [
            {"tier": "Bronze",   "threshold": 3,  "bonus": 100,  "badge": "Bronze"},
            {"tier": "Silver",   "threshold": 10, "bonus": 300,  "badge": "Silver"},
            {"tier": "Gold",     "threshold": 20, "bonus": 700,  "badge": "Gold"},
            {"tier": "Platinum", "threshold": 28, "bonus": 1800, "badge": "Platinum"},
        ]
    },
    "sys_cases": {
        "title": "Case Study Master",
        "category": "sys_design",
        "category_name": "System Design",
        "icon": "server",
        "lucide_icon": "server",
        "description": "Real-world end-to-end architecture cases completed.",
        "unit": "cases",
        "tiers": [
            {"tier": "Bronze",   "threshold": 2,  "bonus": 150,  "badge": "Bronze"},
            {"tier": "Silver",   "threshold": 5,  "bonus": 400,  "badge": "Silver"},
            {"tier": "Gold",     "threshold": 10, "bonus": 900,  "badge": "Gold"},
            {"tier": "Platinum", "threshold": 15, "bonus": 2200, "badge": "Platinum"},
        ]
    },

    # ── Category 4: AI & LLM Systems ──
    "ai_llm": {
        "title": "AI & RAG Pioneer",
        "category": "ai_llm",
        "category_name": "AI & LLM Stack",
        "icon": "cpu",
        "lucide_icon": "cpu",
        "description": "AI / RAG / Agentic workflows topics mastered.",
        "unit": "topics",
        "tiers": [
            {"tier": "Bronze",   "threshold": 3,  "bonus": 100,  "badge": "Bronze"},
            {"tier": "Silver",   "threshold": 8,  "bonus": 300,  "badge": "Silver"},
            {"tier": "Gold",     "threshold": 15, "bonus": 700,  "badge": "Gold"},
            {"tier": "Platinum", "threshold": 22, "bonus": 1800, "badge": "Platinum"},
        ]
    },

    # ── Category 5: Portfolio & Open Source ──
    "github": {
        "title": "Open Source Builder",
        "category": "portfolio",
        "category_name": "Portfolio & Career",
        "icon": "git-branch",
        "lucide_icon": "git-branch",
        "description": "Portfolio GitHub project tasks marked Done.",
        "unit": "tasks",
        "tiers": [
            {"tier": "Bronze",   "threshold": 5,  "bonus": 100,  "badge": "Bronze"},
            {"tier": "Silver",   "threshold": 15, "bonus": 300,  "badge": "Silver"},
            {"tier": "Gold",     "threshold": 30, "bonus": 700,  "badge": "Gold"},
            {"tier": "Platinum", "threshold": 40, "bonus": 1800, "badge": "Platinum"},
        ]
    },

    # ── Category 6: Career & Job Applications ──
    "applications": {
        "title": "Career Hunter",
        "category": "portfolio",
        "category_name": "Portfolio & Career",
        "icon": "briefcase",
        "lucide_icon": "briefcase",
        "description": "Target job applications added and tracked.",
        "unit": "apps",
        "tiers": [
            {"tier": "Bronze",   "threshold": 2,  "bonus": 100,  "badge": "Bronze"},
            {"tier": "Silver",   "threshold": 8,  "bonus": 300,  "badge": "Silver"},
            {"tier": "Gold",     "threshold": 15, "bonus": 700,  "badge": "Gold"},
            {"tier": "Platinum", "threshold": 30, "bonus": 1800, "badge": "Platinum"},
            {"tier": "Diamond",  "threshold": 50, "bonus": 3500, "badge": "Diamond"},
        ]
    },
}


# ══════════════════════════════════════════════════════════════════════════════
# 3. HELPER FUNCTIONS
# ══════════════════════════════════════════════════════════════════════════════

def get_tier_info_for_level(level: int) -> dict:
    """Finds the Rank Tier metadata for a given level."""
    for rank in RANK_TIERS:
        if rank["min_level"] <= level <= rank["max_level"]:
            return rank
    return RANK_TIERS[-1]


def get_level_definition(level: int) -> dict:
    """Finds or builds level definition for any level."""
    for defn in LEVEL_DEFINITIONS:
        if defn["level"] == level:
            tier = get_tier_info_for_level(level)
            return {
                **defn,
                "tier": tier["name"],
                "tier_id": tier["id"],
                "tier_icon": tier["icon"],
                "tier_color": tier["color"],
                "tier_gradient": tier["bg_gradient"],
                "tier_tagline": tier["tagline"],
                "required_xp": 50 * (level - 1) * level,
            }
    
    # Fallback for levels beyond 30
    tier = get_tier_info_for_level(level)
    return {
        "level": level,
        "title": f"Mythic Legend Lv.{level}",
        "icon": "crown",
        "perk": "+30% Global XP Multiplier & Transcendent Aura",
        "tier": tier["name"],
        "tier_id": tier["id"],
        "tier_icon": tier["icon"],
        "tier_color": tier["color"],
        "tier_gradient": tier["bg_gradient"],
        "tier_tagline": tier["tagline"],
        "required_xp": 50 * (level - 1) * level,
    }


def get_level_data(xp: float) -> dict:
    """
    Calculates user level based on XP using quadratic formula:
    xp_boundary(L) = 50 * L * (L - 1).
    Level L starts at 50*(L-1)*L and reaches level L+1 at 50*L*(L+1).
    """
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
    pct_progress = max(0, min(100, pct_progress))
    
    current_defn = get_level_definition(level)
    next_defn = get_level_definition(level + 1)
    tier_info = get_tier_info_for_level(level)
    
    # Generate complete roadmap for levels 1 to max(30, level + 2)
    roadmap = []
    max_roadmap_level = max(30, level + 2)
    for lvl in range(1, max_roadmap_level + 1):
        ld = get_level_definition(lvl)
        status = "unlocked" if lvl < level else ("current" if lvl == level else "locked")
        roadmap.append({
            **ld,
            "status": status,
            "is_current": (lvl == level),
            "is_unlocked": (lvl <= level),
        })
        
    return {
        "level": level,
        "title": current_defn["title"],
        "icon": current_defn["icon"],
        "perk": current_defn["perk"],
        "next_title": next_defn["title"],
        "next_icon": next_defn["icon"],
        "next_perk": next_defn["perk"],
        "tier_name": tier_info["name"],
        "tier_id": tier_info["id"],
        "tier_icon": tier_info["icon"],
        "tier_color": tier_info["color"],
        "tier_gradient": tier_info["bg_gradient"],
        "tier_tagline": tier_info["tagline"],
        "tier_badge_class": tier_info["badge_class"],
        "total_xp": int(xp),
        "current_boundary": current_level_xp,
        "next_boundary": next_level_xp,
        "xp_in_level": int(xp_in_level),
        "xp_needed_for_next": int(next_level_xp - xp),
        "pct_progress": pct_progress,
        "roadmap": roadmap,
        "rank_tiers": RANK_TIERS,
    }


def get_streak_multiplier(streak: int) -> dict:
    """Calculates active streak multiplier based on consecutive days."""
    if streak >= 30:
        multiplier = 1.30
        label = "+30% Streak Multiplier"
    elif streak >= 14:
        multiplier = 1.20
        label = "+20% Streak Multiplier"
    elif streak >= 7:
        multiplier = 1.15
        label = "+15% Streak Multiplier"
    elif streak >= 3:
        multiplier = 1.05
        label = "+5% Streak Multiplier"
    else:
        multiplier = 1.0
        label = "Standard 1.0x XP"
        
    return {
        "multiplier": multiplier,
        "bonus_pct": int((multiplier - 1.0) * 100),
        "label": label,
        "is_active": multiplier > 1.0,
    }


def compute_daily_quests(db: Session, streak: int) -> dict:
    """Generates today's dynamic quests with real-time completion status and XP rewards."""
    today = date.today()
    
    # Today's hours spent
    today_hours = db.query(func.sum(DailyLog.hours_spent)).filter(DailyLog.date == today).scalar() or 0.0
    
    # Today's logs count
    today_logs_count = db.query(DailyLog).filter(DailyLog.date == today).count()
    
    # Solved DSA count
    total_dsa_solved = db.query(DSAProblem).filter(DSAProblem.status == "Solved").count()
    
    # System design & AI topics done count
    total_sd_done = db.query(SystemDesignSubConcept).filter(SystemDesignSubConcept.status == "Done").count()
    total_ai_done = db.query(AILLMTopic).filter(AILLMTopic.status == "Done").count()
    
    quests = [
        {
            "id": "quest_study",
            "title": "Deep Work Sprint",
            "desc": "Log at least 1.5 focused study hours today.",
            "icon": "clock",
            "lucide_icon": "clock",
            "reward_xp": 35,
            "target": 1.5,
            "unit": "hours",
            "current": round(today_hours, 1),
            "progress_pct": min(100, round((today_hours / 1.5) * 100)) if 1.5 > 0 else 0,
            "completed": today_hours >= 1.5,
        },
        {
            "id": "quest_dsa",
            "title": "Algorithm Drill",
            "desc": "Solve at least 1 LeetCode or DSA problem.",
            "icon": "code-2",
            "lucide_icon": "code-2",
            "reward_xp": 40,
            "target": 1,
            "unit": "problem",
            "current": 1 if total_dsa_solved > 0 else 0,
            "progress_pct": 100 if total_dsa_solved > 0 else 0,
            "completed": total_dsa_solved > 0,
        },
        {
            "id": "quest_architecture",
            "title": "System Architecture Mastery",
            "desc": "Review or master 1 System Design / AI concept.",
            "icon": "network",
            "lucide_icon": "network",
            "reward_xp": 45,
            "target": 1,
            "unit": "concept",
            "current": 1 if (total_sd_done + total_ai_done) > 0 else 0,
            "progress_pct": 100 if (total_sd_done + total_ai_done) > 0 else 0,
            "completed": (total_sd_done + total_ai_done) > 0,
        },
        {
            "id": "quest_streak",
            "title": "Streak Defender",
            "desc": "Maintain your active study streak by logging daily activity.",
            "icon": "flame",
            "lucide_icon": "flame",
            "reward_xp": 30,
            "target": 1,
            "unit": "log",
            "current": min(1, today_logs_count or (1 if streak > 0 else 0)),
            "progress_pct": 100 if (today_logs_count > 0 or streak > 0) else 0,
            "completed": (today_logs_count > 0 or streak > 0),
        },
    ]
    
    completed_count = sum(1 for q in quests if q["completed"])
    total_possible_xp = sum(q["reward_xp"] for q in quests)
    earned_quest_xp = sum(q["reward_xp"] for q in quests if q["completed"])
    
    return {
        "quests": quests,
        "completed_count": completed_count,
        "total_count": len(quests),
        "earned_xp": earned_quest_xp,
        "total_possible_xp": total_possible_xp,
        "all_completed": completed_count == len(quests),
    }


# ══════════════════════════════════════════════════════════════════════════════
# 4. MAIN GAMIFICATION STATE COMPUTATION
# ══════════════════════════════════════════════════════════════════════════════

def get_gamification_state(db: Session) -> dict:
    """Computes stats, XP breakdown, achievement tiers, daily quests, and leveling boundaries."""
    
    # 1. Gather raw inputs from database
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
    
    # AI/LLM Done Topics
    total_ai_llm = db.query(AILLMTopic).filter(AILLMTopic.status == "Done").count()
    
    # GitHub Done Tasks
    total_github = db.query(GithubTask).filter(GithubTask.done == True).count()
    
    # Applications added
    total_apps = db.query(Application).count()
    
    # Weekend hours calculation
    weekend_logs = db.query(DailyLog.hours_spent, DailyLog.date).all()
    weekend_hours = sum(h for h, d in weekend_logs if d.weekday() in (5, 6))
    
    # 2. Calculate Base XP from study vectors
    xp_hours = total_hours * 10.0
    xp_dsa_easy = solved_easy * 10.0
    xp_dsa_medium = solved_medium * 25.0
    xp_dsa_hard = solved_hard * 50.0
    xp_dsa_total = xp_dsa_easy + xp_dsa_medium + xp_dsa_hard
    
    xp_sd_concepts = sd_concepts_done * 20.0
    xp_sd_cases = sd_cases_done * 40.0
    xp_sys_design_total = xp_sd_concepts + xp_sd_cases
    
    xp_ai_llm = total_ai_llm * 20.0
    xp_github = total_github * 15.0
    xp_apps = total_apps * 10.0
    xp_streak = streak * 10.0
    
    base_xp = xp_hours + xp_dsa_total + xp_sys_design_total + xp_ai_llm + xp_github + xp_apps + xp_streak
    
    # Map key metric types to actual calculated values
    metrics_map = {
        "streak": streak,
        "hours": total_hours,
        "weekend_warrior": round(weekend_hours, 1),
        "dsa": total_dsa,
        "dsa_medium": solved_medium,
        "dsa_hard": solved_hard,
        "sys_concepts": sd_concepts_done,
        "sys_cases": sd_cases_done,
        "ai_llm": total_ai_llm,
        "github": total_github,
        "applications": total_apps,
    }
    
    # 3. Process achievements and sum bonuses
    achievements_list = []
    bonus_xp = 0
    total_tiers_count = 0
    unlocked_tiers_count = 0
    
    for key, schema in ACHIEVEMENT_SCHEMAS.items():
        current_value = metrics_map.get(key, 0)
        tiers_status = []
        active_tier = None
        next_tier = None
        
        for t in schema["tiers"]:
            total_tiers_count += 1
            unlocked = current_value >= t["threshold"]
            if unlocked:
                unlocked_tiers_count += 1
                bonus_xp += t["bonus"]
                active_tier = t
            elif next_tier is None:
                next_tier = t
                
            tiers_status.append({
                "tier": t["tier"],
                "threshold": t["threshold"],
                "bonus": t["bonus"],
                "badge": t["badge"],
                "unlocked": unlocked
            })
        
        # Calculate progress towards next tier
        if next_tier:
            prev_threshold = 0
            if active_tier:
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
            "category": schema.get("category", "grind"),
            "category_name": schema.get("category_name", "General"),
            "icon": schema["icon"],
            "lucide_icon": schema.get("lucide_icon", "award"),
            "description": schema["description"],
            "unit": schema["unit"],
            "current_value": current_value,
            "tiers": tiers_status,
            "active_tier": active_tier["tier"] if active_tier else "Locked",
            "active_badge": active_tier["badge"] if active_tier else "Locked",
            "is_unlocked": active_tier is not None,
            "next_tier_name": next_tier["tier"] if next_tier else "Maxed",
            "next_tier_threshold": next_tier["threshold"] if next_tier else current_value,
            "next_tier_badge": next_tier["badge"] if next_tier else "Max",
            "next_tier_bonus": next_tier["bonus"] if next_tier else 0,
            "progress_pct": progress_pct
        })
    
    # 4. Process Legendary Hall of Fame Badges
    legendary_badges = [
        {
            "id": "centurion",
            "title": "The Centurion",
            "description": "Solve 100+ total DSA problems across all difficulties.",
            "icon": "shield-check",
            "unlocked": total_dsa >= 100,
            "bonus_xp": 1000,
            "criteria": f"{total_dsa} / 100 Problems Solved",
            "tag": "Legendary",
        },
        {
            "id": "century_hours",
            "title": "Century Club",
            "description": "Log over 100+ focused hours of study time.",
            "icon": "clock",
            "unlocked": total_hours >= 100,
            "bonus_xp": 1000,
            "criteria": f"{total_hours} / 100 Hours Logged",
            "tag": "Legendary",
        },
        {
            "id": "polymath",
            "title": "The Polymath",
            "description": "Active progress across all 5 core vectors (DSA, SysDesign, AI, GitHub, Applications).",
            "icon": "sparkles",
            "unlocked": (total_dsa >= 5 and sd_concepts_done >= 2 and total_ai_llm >= 2 and total_github >= 2 and total_apps >= 2),
            "bonus_xp": 1200,
            "criteria": "5+ Solved, 2+ SysDesign, 2+ AI, 2+ GitHub, 2+ Apps",
            "tag": "Mythic",
        },
        {
            "id": "iron_will",
            "title": "Iron Will",
            "description": "Reach a legendary 14+ day continuous study streak.",
            "icon": "flame",
            "unlocked": streak >= 14,
            "bonus_xp": 1500,
            "criteria": f"{streak} / 14 Day Streak",
            "tag": "Mythic",
        },
    ]
    
    legendary_bonus = sum(b["bonus_xp"] for b in legendary_badges if b["unlocked"])
    total_legendary_unlocked = sum(1 for b in legendary_badges if b["unlocked"])
    
    # 5. Streak multiplier calculation
    streak_info = get_streak_multiplier(streak)
    streak_multiplier_bonus = int(base_xp * (streak_info["multiplier"] - 1.0))
    
    # 6. Daily Quests computation
    daily_quests = compute_daily_quests(db, streak)
    
    # Total combined XP
    total_xp = base_xp + bonus_xp + legendary_bonus + streak_multiplier_bonus
    
    # 7. Calculate Level details
    level_details = get_level_data(total_xp)
    
    # Detailed XP Breakdown dictionary for visual progress bars / charts
    xp_breakdown = [
        {"source": "DSA Problems",     "xp": int(xp_dsa_total),        "color": "#7C3AED", "icon": "code-2"},
        {"source": "System Design",    "xp": int(xp_sys_design_total), "color": "#0EA5E9", "icon": "network"},
        {"source": "AI & LLM Topics",  "xp": int(xp_ai_llm),           "color": "#F59E0B", "icon": "cpu"},
        {"source": "Study Hours",      "xp": int(xp_hours),            "color": "#10B981", "icon": "clock"},
        {"source": "GitHub Tasks",     "xp": int(xp_github),           "color": "#3B82F6", "icon": "git-branch"},
        {"source": "Job Applications", "xp": int(xp_apps),             "color": "#8B5CF6", "icon": "briefcase"},
        {"source": "Streak Bonuses",   "xp": int(xp_streak + streak_multiplier_bonus), "color": "#EF4444", "icon": "flame"},
        {"source": "Milestone Badges", "xp": int(bonus_xp + legendary_bonus), "color": "#EC4899", "icon": "award"},
    ]
    
    total_badges = sum(1 for a in achievements_list if a["is_unlocked"])
    
    return {
        "level_details": level_details,
        "achievements": achievements_list,
        "legendary_badges": legendary_badges,
        "legendary_unlocked_count": total_legendary_unlocked,
        "daily_quests": daily_quests,
        "streak_info": streak_info,
        "metrics": metrics_map,
        "base_xp": int(base_xp),
        "bonus_xp": int(bonus_xp + legendary_bonus),
        "streak_multiplier_bonus": streak_multiplier_bonus,
        "xp_breakdown": xp_breakdown,
        "total_badges_unlocked": total_badges,
        "total_badges_possible": len(ACHIEVEMENT_SCHEMAS),
        "total_tiers_unlocked": unlocked_tiers_count,
        "total_tiers_possible": total_tiers_count,
    }
