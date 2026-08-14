from datetime import date, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Dict, List
from app.models.daily_log import DailyLog
from app.models.dsa import DSAProblem, DSATopic
from app.models.system_design import SystemDesignConcept, SystemDesignSubConcept, SystemDesignCase
from app.models.ai_llm import AILLMTopic
from app.models.github import GithubProject
from app.models.user import UserProfile, WeeklySchedule


CATEGORY_COLORS = {
    "DSA": "#7C3AED",
    "System Design": "#0EA5E9",
    "AI/LLM": "#F59E0B",
    "GitHub": "#10B981",
    "LinkedIn/Resume": "#EF4444",
    "Applications": "#8B5CF6",
    "Mock Interview": "#EC4899",
    "Reading": "#6B7280",
    "Other": "#9CA3AF",
}


def get_total_hours(db: Session) -> float:
    result = db.query(func.sum(DailyLog.hours_spent)).scalar()
    return round(result or 0.0, 1)


def get_week_hours(db: Session, week_start: date, week_end: date) -> float:
    result = db.query(func.sum(DailyLog.hours_spent)).filter(
        DailyLog.date >= week_start,
        DailyLog.date <= week_end,
    ).scalar()
    return round(result or 0.0, 1)


def get_hours_by_category(db: Session) -> Dict[str, float]:
    rows = db.query(DailyLog.category, func.sum(DailyLog.hours_spent)).group_by(DailyLog.category).all()
    return {row[0]: round(row[1], 1) for row in rows}


def get_hours_by_category_this_week(db: Session, week_start: date, week_end: date) -> Dict[str, float]:
    rows = db.query(DailyLog.category, func.sum(DailyLog.hours_spent)).filter(
        DailyLog.date >= week_start,
        DailyLog.date <= week_end,
    ).group_by(DailyLog.category).all()
    return {row[0]: round(row[1], 1) for row in rows}


def get_daily_hours_last_n_days(db: Session, n: int = 14) -> List[Dict]:
    start = date.today() - timedelta(days=n - 1)
    rows = db.query(DailyLog.date, func.sum(DailyLog.hours_spent)).filter(
        DailyLog.date >= start
    ).group_by(DailyLog.date).order_by(DailyLog.date).all()
    
    # Fill in zeros for days with no data
    date_map = {row[0]: round(row[1], 1) for row in rows}
    result = []
    for i in range(n):
        d = start + timedelta(days=i)
        result.append({"date": d.strftime("%b %d"), "hours": date_map.get(d, 0)})
    return result


def get_streak(db: Session) -> int:
    """Count consecutive days with at least some study time ending today or yesterday."""
    today = date.today()
    streak = 0
    check_date = today
    
    for _ in range(365):
        hours = db.query(func.sum(DailyLog.hours_spent)).filter(
            DailyLog.date == check_date
        ).scalar() or 0
        if hours > 0:
            streak += 1
            check_date -= timedelta(days=1)
        else:
            # Allow one day gap (yesterday might not be logged yet)
            if check_date == today:
                check_date -= timedelta(days=1)
                continue
            break
    return streak


def get_dsa_stats(db: Session) -> Dict:
    total = db.query(DSAProblem).count()
    solved = db.query(DSAProblem).filter(DSAProblem.status == "Solved").count()
    easy = db.query(DSAProblem).filter(DSAProblem.status == "Solved", DSAProblem.difficulty == "Easy").count()
    medium = db.query(DSAProblem).filter(DSAProblem.status == "Solved", DSAProblem.difficulty == "Medium").count()
    hard = db.query(DSAProblem).filter(DSAProblem.status == "Solved", DSAProblem.difficulty == "Hard").count()
    
    topics = db.query(DSATopic).order_by(DSATopic.order_index).all()
    topic_stats = []
    for t in topics:
        t_total = len(t.problems)
        t_solved = sum(1 for p in t.problems if p.status == "Solved")
        topic_stats.append({
            "name": t.name,
            "total": t_total,
            "solved": t_solved,
            "pct": round((t_solved / t_total * 100) if t_total > 0 else 0),
        })
    
    return {
        "total": total,
        "solved": solved,
        "easy": easy,
        "medium": medium,
        "hard": hard,
        "easy_target": 60,
        "medium_target": 150,
        "hard_target": 40,
        "total_target": 250,
        "pct": round((solved / 250) * 100) if solved else 0,
        "topic_stats": topic_stats,
    }


def get_system_design_stats(db: Session) -> Dict:
    topics_total = db.query(SystemDesignSubConcept).count()
    topics_done = db.query(SystemDesignSubConcept).filter(SystemDesignSubConcept.status == "Done").count()
    cases_total = db.query(SystemDesignCase).count()
    cases_done = db.query(SystemDesignCase).filter(SystemDesignCase.status == "Done").count()
    total = topics_total + cases_total
    done = topics_done + cases_done
    return {
        "topics_total": topics_total,
        "topics_done": topics_done,
        "cases_total": cases_total,
        "cases_done": cases_done,
        "pct": round((done / total * 100) if total > 0 else 0),
    }


def get_ai_llm_stats(db: Session) -> Dict:
    total = db.query(AILLMTopic).count()
    done = db.query(AILLMTopic).filter(AILLMTopic.status == "Done").count()
    return {
        "total": total,
        "done": done,
        "pct": round((done / total * 100) if total > 0 else 0),
    }


def get_github_stats(db: Session) -> Dict:
    projects = db.query(GithubProject).all()
    total_tasks = 0
    done_tasks = 0
    for p in projects:
        total_tasks += len(p.tasks)
        done_tasks += sum(1 for t in p.tasks if t.done)
    return {
        "projects": len(projects),
        "total_tasks": total_tasks,
        "done_tasks": done_tasks,
        "pct": round((done_tasks / total_tasks * 100) if total_tasks > 0 else 0),
    }


def get_weekly_hours_chart(db: Session, weeks: List, current_week_num: int = None) -> List[Dict]:
    """Return hours per week for chart display (last 10 weeks max, aligned to current week)."""
    if current_week_num is None:
        current_week_num = len(weeks)

    if current_week_num <= 10:
        display_weeks = weeks[:10]
    else:
        start_idx = max(0, current_week_num - 10)
        display_weeks = weeks[start_idx:current_week_num]

    result = []
    for wn, ws, we in display_weeks:
        hours = get_week_hours(db, ws, we)
        result.append({"week": f"W{wn}", "hours": hours})
    return result


def get_category_hours_for_chart(db: Session) -> Dict:
    """Return hours by category formatted for Chart.js pie/doughnut."""
    by_cat = get_hours_by_category(db)
    categories = list(by_cat.keys())
    hours = list(by_cat.values())
    colors = [CATEGORY_COLORS.get(c, "#9CA3AF") for c in categories]
    return {"labels": categories, "data": hours, "colors": colors}
