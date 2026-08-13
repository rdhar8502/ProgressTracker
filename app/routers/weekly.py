from datetime import date
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.models.user import UserProfile, WeeklySchedule
from app.models.daily_log import DailyLog
from app.services.week_utils import generate_weeks, get_current_week_number
from app.services.analytics import get_week_hours, CATEGORY_COLORS

router = APIRouter(prefix="/weekly", tags=["weekly"])
templates = Jinja2Templates(directory="app/templates")


@router.get("", response_class=HTMLResponse)
def weekly_page(request: Request, db: Session = Depends(get_db)):
    user = db.query(UserProfile).first()
    today = date.today()
    weeks_raw = generate_weeks(user.start_date, user.end_date)
    current_week_num = get_current_week_number(weeks_raw, today)

    weeks_data = []
    for wn, ws, we in weeks_raw:
        schedule = db.query(WeeklySchedule).filter(WeeklySchedule.week_number == wn).first()
        actual_hours = get_week_hours(db, ws, we)
        target_hours = schedule.target_hours if schedule else 15.0
        theme = schedule.theme if schedule else ""

        # Actual category breakdown from daily logs this week
        cat_rows = (
            db.query(DailyLog.category, func.sum(DailyLog.hours_spent).label("hours"))
            .filter(DailyLog.date >= ws, DailyLog.date <= we)
            .group_by(DailyLog.category)
            .order_by(func.sum(DailyLog.hours_spent).desc())
            .all()
        )
        cat_breakdown = [
            {
                "category": r.category,
                "hours": round(r.hours, 1),
                "color": CATEGORY_COLORS.get(r.category, "#9CA3AF"),
                "pct": round((r.hours / actual_hours * 100) if actual_hours else 0),
            }
            for r in cat_rows
        ]

        # Day-by-day breakdown (PostgreSQL compatible)
        daily_rows = (
            db.query(
                DailyLog.date,
                func.sum(DailyLog.hours_spent).label("hours"),
                func.count(DailyLog.id).label("sessions"),
            )
            .filter(DailyLog.date >= ws, DailyLog.date <= we)
            .group_by(DailyLog.date)
            .order_by(DailyLog.date)
            .all()
        )

        # Per-day category breakdown (for tooltip/detail)
        day_cats = {}
        day_logs_raw = (
            db.query(DailyLog.date, DailyLog.category, DailyLog.sub_topic,
                     DailyLog.hours_spent)
            .filter(DailyLog.date >= ws, DailyLog.date <= we)
            .order_by(DailyLog.date, DailyLog.created_at)
            .all()
        )
        for row in day_logs_raw:
            day_cats.setdefault(row.date, []).append({
                "category": row.category,
                "sub_topic": row.sub_topic,
                "hours": row.hours_spent,
            })

        pct = round((actual_hours / target_hours) * 100) if target_hours else 0
        is_current = (wn == current_week_num)
        is_past = we < today

        weeks_data.append({
            "week_number": wn,
            "week_start": ws,
            "week_end": we,
            "theme": theme,           # Soft suggestion only, not a constraint
            "actual_hours": actual_hours,
            "target_hours": target_hours,
            "pct": min(pct, 100),
            "is_current": is_current,
            "is_past": is_past,
            "cat_breakdown": cat_breakdown,   # What you actually studied
            "daily_logs": [
                {
                    "date": r.date,
                    "hours": round(r.hours, 1),
                    "sessions": r.sessions,
                    "cats": day_cats.get(r.date, []),
                }
                for r in daily_rows
            ],
        })

    return templates.TemplateResponse("weekly.html", {
        "request": request,
        "user": user,
        "today": today,
        "weeks": weeks_data,
        "current_week_num": current_week_num,
        "total_weeks": len(weeks_raw),
        "active_page": "weekly",
        "category_colors": CATEGORY_COLORS,
    })

