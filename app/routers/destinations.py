from fastapi import APIRouter, Depends, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from datetime import date

from app.database import get_db
from app.models.user import UserProfile
from app.models.destination import RelocationDestination
from app.services.destination_seed_data import (
    DESTINATIONS_DATA,
    INDIA_BASELINE,
    TOP_10_HAPPINESS_COUNTRIES,
    TOP_10_LIVING_QUALITY_COUNTRIES,
    TOP_10_POLLUTION_FREE_SCENIC_COUNTRIES,
)

router = APIRouter(prefix="/destinations", tags=["destinations"])
templates = Jinja2Templates(directory="app/templates")


@router.get("", response_class=HTMLResponse)
def destinations_page(request: Request, db: Session = Depends(get_db)):
    user = db.query(UserProfile).first()
    destinations = db.query(RelocationDestination).order_by(RelocationDestination.rank.asc()).all()

    # Calculate summary metrics
    if destinations:
        top_pick = destinations[0]
        best_mother_fit = next((d for d in destinations if "LTVP" in d.family_mother_badge or "Outstanding" in d.family_mother_badge), destinations[1] if len(destinations) > 1 else destinations[0])
        max_savings_dest = max(destinations, key=lambda d: d.monthly_savings_inr)
        avg_gross_inr = sum(d.annual_gross_inr for d in destinations) / len(destinations)
    else:
        top_pick = None
        best_mother_fit = None
        max_savings_dest = None
        avg_gross_inr = 0.0

    return templates.TemplateResponse("destinations.html", {
        "request": request,
        "user": user,
        "today": date.today(),
        "destinations": destinations,
        "top_pick": top_pick,
        "best_mother_fit": best_mother_fit,
        "max_savings_dest": max_savings_dest,
        "avg_gross_inr": avg_gross_inr,
        "india_baseline": INDIA_BASELINE,
        "top_10_happiness": TOP_10_HAPPINESS_COUNTRIES,
        "top_10_living": TOP_10_LIVING_QUALITY_COUNTRIES,
        "top_10_pollution_free": TOP_10_POLLUTION_FREE_SCENIC_COUNTRIES,
        "active_page": "destinations",
    })


@router.post("/{dest_id}/edit")
def edit_destination(
    dest_id: int,
    salary_median: float = Form(...),
    salary_min: float = Form(...),
    salary_max: float = Form(...),
    estimated_tax_rate: float = Form(...),
    monthly_expense_local: float = Form(...),
    exchange_rate_inr: float = Form(...),
    summary_verdict: str = Form(None),
    db: Session = Depends(get_db),
):
    dest = db.query(RelocationDestination).filter(RelocationDestination.id == dest_id).first()
    if not dest:
        raise HTTPException(status_code=404, detail="Destination not found")

    dest.salary_median = salary_median
    dest.salary_min = salary_min
    dest.salary_max = salary_max
    dest.estimated_tax_rate = estimated_tax_rate
    dest.monthly_expense_local = monthly_expense_local
    dest.exchange_rate_inr = exchange_rate_inr
    if summary_verdict:
        dest.summary_verdict = summary_verdict

    db.commit()
    return RedirectResponse(url="/destinations?updated=1", status_code=303)


@router.post("/reset-defaults")
def reset_destinations_defaults(db: Session = Depends(get_db)):
    for d_data in DESTINATIONS_DATA:
        dest = db.query(RelocationDestination).filter(
            RelocationDestination.country_name == d_data["country_name"]
        ).first()
        if dest:
            for key, val in d_data.items():
                setattr(dest, key, val)
        else:
            db.add(RelocationDestination(**d_data))
    db.commit()
    return RedirectResponse(url="/destinations?reset=1", status_code=303)
