from datetime import date
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import json

from app.database import get_db
from app.models.user import UserProfile, WeeklySchedule
from app.services import analytics
from app.services.week_utils import generate_weeks, get_current_week_number, days_remaining
from app.services.gamification import get_gamification_state
from app.services.motivation import get_daily_spark

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def dashboard(request: Request, db: Session = Depends(get_db)):
    user = db.query(UserProfile).first()
    if not user:
        return templates.TemplateResponse("dashboard.html", {"request": request, "user": None})

    weeks_raw = generate_weeks(user.start_date, user.end_date)
    today = date.today()
    current_week_num = get_current_week_number(weeks_raw, today)

    # Find this week's schedule
    this_week = None
    for wn, ws, we in weeks_raw:
        if wn == current_week_num:
            this_week = (wn, ws, we)
            break

    week_start = this_week[1] if this_week else today
    week_end = this_week[2] if this_week else today

    # Stats
    total_hours = analytics.get_total_hours(db)
    week_hours = analytics.get_week_hours(db, week_start, week_end)
    week_schedule = db.query(WeeklySchedule).filter(WeeklySchedule.week_number == current_week_num).first()
    week_target = week_schedule.target_hours if week_schedule else 15.0
    week_theme = week_schedule.theme if week_schedule else ""

    streak = analytics.get_streak(db)
    dsa_stats = analytics.get_dsa_stats(db)
    sd_stats = analytics.get_system_design_stats(db)
    ai_stats = analytics.get_ai_llm_stats(db)
    gh_stats = analytics.get_github_stats(db)
    hours_by_cat = analytics.get_hours_by_category(db)
    daily_chart = analytics.get_daily_hours_last_n_days(db, 14)
    weekly_chart = analytics.get_weekly_hours_chart(db, weeks_raw, current_week_num)
    cat_chart = analytics.get_category_hours_for_chart(db)

    gamification = get_gamification_state(db)
    spark = get_daily_spark()

    # Progress for category rings
    category_progress = [
        {"name": "DSA", "pct": dsa_stats["pct"], "solved": dsa_stats["solved"], "target": dsa_stats["total"], "color": "#7C3AED"},
        {"name": "System Design", "pct": sd_stats["pct"], "done": sd_stats["topics_done"] + sd_stats["cases_done"],
         "target": sd_stats["topics_total"] + sd_stats["cases_total"], "color": "#0EA5E9"},
        {"name": "AI/LLM", "pct": ai_stats["pct"], "done": ai_stats["done"], "target": ai_stats["total"], "color": "#F59E0B"},
        {"name": "GitHub", "pct": gh_stats["pct"], "done": gh_stats["done_tasks"], "target": gh_stats["total_tasks"], "color": "#10B981"},
    ]

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "user": user,
        "today": today,
        "total_hours": total_hours,
        "week_hours": week_hours,
        "week_target": week_target,
        "week_theme": week_theme,
        "current_week_num": current_week_num,
        "total_weeks": len(weeks_raw),
        "week_start": week_start,
        "week_end": week_end,
        "streak": streak,
        "days_remaining": days_remaining(user.end_date),
        "dsa_stats": dsa_stats,
        "sd_stats": sd_stats,
        "ai_stats": ai_stats,
        "gh_stats": gh_stats,
        "hours_by_cat": hours_by_cat,
        "category_progress": category_progress,
        "daily_chart_json": json.dumps(daily_chart),
        "weekly_chart_json": json.dumps(weekly_chart),
        "cat_chart_json": json.dumps(cat_chart),
        "gamification": gamification,
        "spark": spark,
        "active_page": "dashboard",
    })

