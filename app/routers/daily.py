from datetime import date
from typing import Optional
from fastapi import APIRouter, Depends, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.models.daily_log import DailyLog
from app.models.user import UserProfile

router = APIRouter(prefix="/daily", tags=["daily"])
templates = Jinja2Templates(directory="app/templates")

CATEGORIES = [
    "DSA", "System Design", "AI/LLM", "GitHub",
    "LinkedIn/Resume", "Applications", "Mock Interview", "Reading", "Other"
]


@router.get("", response_class=HTMLResponse)
def daily_page(request: Request, log_date: Optional[str] = None, db: Session = Depends(get_db)):
    user = db.query(UserProfile).first()
    today = date.today()
    selected_date = date.fromisoformat(log_date) if log_date else today

    logs = db.query(DailyLog).filter(DailyLog.date == selected_date).order_by(DailyLog.created_at).all()

    # Daily summary
    total_hours = sum(l.hours_spent for l in logs)
    problems_solved = sum(l.problems_solved for l in logs)
    by_category = {}
    for l in logs:
        by_category[l.category] = round(by_category.get(l.category, 0) + l.hours_spent, 1)

    return templates.TemplateResponse("daily.html", {
        "request": request,
        "user": user,
        "today": today,
        "selected_date": selected_date,
        "logs": logs,
        "total_hours": round(total_hours, 1),
        "problems_solved": problems_solved,
        "by_category": by_category,
        "categories": CATEGORIES,
        "active_page": "daily",
    })


@router.post("/add")
def add_log(
    request: Request,
    log_date: str = Form(...),
    category: str = Form(...),
    sub_topic: str = Form(...),
    hours_spent: float = Form(...),
    notes: str = Form(""),
    sources: str = Form(""),
    problems_solved: int = Form(0),
    confidence: int = Form(3),
    db: Session = Depends(get_db),
):
    log = DailyLog(
        date=date.fromisoformat(log_date),
        category=category,
        sub_topic=sub_topic,
        hours_spent=hours_spent,
        notes=notes,
        sources=sources,
        problems_solved=problems_solved,
        confidence=confidence,
    )
    db.add(log)
    db.commit()
    return RedirectResponse(url=f"/daily?log_date={log_date}", status_code=303)


@router.post("/delete/{log_id}")
def delete_log(log_id: int, log_date: str = Form(""), db: Session = Depends(get_db)):
    log = db.query(DailyLog).filter(DailyLog.id == log_id).first()
    if not log:
        raise HTTPException(status_code=404, detail="Log not found")
    log_date_str = log.date.isoformat()
    db.delete(log)
    db.commit()
    return RedirectResponse(url=f"/daily?log_date={log_date_str}", status_code=303)


@router.get("/api/logs")
def api_logs(log_date: str, db: Session = Depends(get_db)):
    d = date.fromisoformat(log_date)
    logs = db.query(DailyLog).filter(DailyLog.date == d).all()
    return [{"id": l.id, "category": l.category, "sub_topic": l.sub_topic,
             "hours_spent": l.hours_spent, "notes": l.notes, "sources": l.sources,
             "problems_solved": l.problems_solved, "confidence": l.confidence} for l in logs]
