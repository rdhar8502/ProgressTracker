from datetime import date
from typing import Optional
from fastapi import APIRouter, Depends, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.application import Application
from app.models.user import UserProfile

router = APIRouter(prefix="/applications", tags=["applications"])
templates = Jinja2Templates(directory="app/templates")

STAGES = [
    "Saved", "Applied", "OA", "Phone Screen",
    "Technical", "Final Round", "Offer", "Rejected", "Withdrawn"
]
ACTIVE_STAGES = ["Saved", "Applied", "OA", "Phone Screen", "Technical", "Final Round"]
CURRENCIES = ["USD", "CAD", "GBP", "EUR", "AED", "INR"]
COUNTRIES = ["United States", "Canada", "United Kingdom", "Germany", "Netherlands", "UAE", "Remote"]


@router.get("", response_class=HTMLResponse)
def applications_page(
    request: Request,
    stage: Optional[str] = None,
    country: Optional[str] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db),
):
    user = db.query(UserProfile).first()
    query = db.query(Application)
    if stage:
        query = query.filter(Application.stage == stage)
    if country:
        query = query.filter(Application.country == country)
    if search and search.strip():
        search_clean = search.strip()
        query = query.filter(
            Application.company.ilike(f"%{search_clean}%") |
            Application.role.ilike(f"%{search_clean}%") |
            Application.notes.ilike(f"%{search_clean}%")
        )
    apps = query.order_by(Application.applied_date.desc().nullslast(), Application.created_at.desc()).all()

    # Stage counts
    stage_counts = {}
    all_apps = db.query(Application).all()
    for s in STAGES:
        stage_counts[s] = sum(1 for a in all_apps if a.stage == s)

    total = len(all_apps)
    active = sum(1 for a in all_apps if a.stage in ACTIVE_STAGES)
    offers = stage_counts.get("Offer", 0)

    return templates.TemplateResponse("applications.html", {
        "request": request,
        "user": user,
        "apps": apps,
        "stages": STAGES,
        "stage_counts": stage_counts,
        "total": total,
        "active": active,
        "offers": offers,
        "currencies": CURRENCIES,
        "countries": COUNTRIES,
        "selected_stage": stage,
        "selected_country": country,
        "selected_search": search or "",
        "today": date.today(),
        "active_page": "applications",
    })


@router.post("/add")
def add_application(
    company: str = Form(...),
    role: str = Form(...),
    location: str = Form(""),
    country: str = Form(""),
    visa_sponsor: bool = Form(False),
    salary_min: Optional[float] = Form(None),
    salary_max: Optional[float] = Form(None),
    currency: str = Form("USD"),
    stage: str = Form("Saved"),
    job_url: str = Form(""),
    notes: str = Form(""),
    applied_date: Optional[str] = Form(None),
    db: Session = Depends(get_db),
):
    app = Application(
        company=company,
        role=role,
        location=location,
        country=country,
        visa_sponsor=visa_sponsor,
        salary_min=salary_min,
        salary_max=salary_max,
        currency=currency,
        stage=stage,
        job_url=job_url,
        notes=notes,
        applied_date=date.fromisoformat(applied_date) if applied_date else None,
    )
    db.add(app)
    db.commit()
    return RedirectResponse(url="/applications", status_code=303)


@router.post("/update/{app_id}")
def update_application(
    app_id: int,
    stage: str = Form(...),
    notes: str = Form(""),
    response_date: Optional[str] = Form(None),
    follow_up_date: Optional[str] = Form(None),
    db: Session = Depends(get_db),
):
    a = db.query(Application).filter(Application.id == app_id).first()
    if not a:
        raise HTTPException(status_code=404)
    a.stage = stage
    a.notes = notes
    if response_date:
        a.response_date = date.fromisoformat(response_date)
    if follow_up_date:
        a.follow_up_date = date.fromisoformat(follow_up_date)
    db.commit()
    return RedirectResponse(url="/applications", status_code=303)


@router.post("/delete/{app_id}")
def delete_application(app_id: int, db: Session = Depends(get_db)):
    a = db.query(Application).filter(Application.id == app_id).first()
    if not a:
        raise HTTPException(status_code=404)
    db.delete(a)
    db.commit()
    return RedirectResponse(url="/applications", status_code=303)
