from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from datetime import date

from app.database import get_db
from app.models.user import UserProfile, SalaryTarget
from app.models.destination import RelocationDestination
from app.services.destination_seed_data import INDIA_BASELINE

router = APIRouter(prefix="/settings", tags=["settings"])
templates = Jinja2Templates(directory="app/templates")


@router.get("", response_class=HTMLResponse)
def settings_page(request: Request, db: Session = Depends(get_db)):
    user = db.query(UserProfile).first()
    salary_targets = db.query(SalaryTarget).all()
    destinations = db.query(RelocationDestination).order_by(RelocationDestination.rank.asc()).all()
    return templates.TemplateResponse("settings.html", {
        "request": request,
        "user": user,
        "today": date.today(),
        "salary_targets": salary_targets,
        "destinations": destinations,
        "india_baseline": INDIA_BASELINE,
        "active_page": "settings",
        "saved": False,
    })



@router.post("/profile")
def update_profile(
    name: str = Form(...),
    target_role: str = Form(...),
    start_date: str = Form(...),
    end_date: str = Form(...),
    current_company: str = Form(""),
    years_experience: int = Form(7),
    linkedin_url: str = Form(""),
    github_url: str = Form(""),
    weekday_target_hours: float = Form(1.5),
    saturday_target_hours: float = Form(4.0),
    sunday_target_hours: float = Form(3.5),
    db: Session = Depends(get_db),
):
    user = db.query(UserProfile).first()
    if user:
        user.name = name
        user.target_role = target_role
        user.start_date = date.fromisoformat(start_date)
        user.end_date = date.fromisoformat(end_date)
        user.current_company = current_company
        user.years_experience = years_experience
        user.linkedin_url = linkedin_url
        user.github_url = github_url
        user.weekday_target_hours = weekday_target_hours
        user.saturday_target_hours = saturday_target_hours
        user.sunday_target_hours = sunday_target_hours
        db.commit()
    return RedirectResponse(url="/settings?saved=1", status_code=303)
