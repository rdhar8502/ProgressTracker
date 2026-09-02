"""
North America Readiness page router — /na-readiness
Serves the standalone North America (USA 🇺🇸 & Canada 🇨🇦) Interview Readiness Radar page.
"""
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import UserProfile
from app.services.gamification import get_gamification_state

router = APIRouter(prefix="/na-readiness", tags=["na_readiness"])
templates = Jinja2Templates(directory="app/templates")


from app.services.na_company_profiles import get_na_company_profiles, get_company_stats


@router.get("", response_class=HTMLResponse)
def na_readiness_page(request: Request, db: Session = Depends(get_db)):
    user = db.query(UserProfile).first()
    gamification = get_gamification_state(db)
    na = gamification.get("na_readiness") or gamification["eu_readiness"]

    us_score = na["us_score"]
    ca_score = na["ca_score"]
    combined_score = na["combined_score"]

    # 7-Axis Radar Chart calibrated for US FAANG & Canadian Tier-1 Tech
    # Dimensions:
    # 0: System Design (HLD)
    # 1: DSA (LeetCode Med+Hard)
    # 2: AI / LLM Engineering
    # 3: Database & Storage
    # 4: GitHub & OSS Portfolio
    sd_pct = round(na["dimensions"][0]["pct"])
    dsa_pct = round(na["dimensions"][1]["pct"])
    ai_pct = round(na["dimensions"][2]["pct"])
    db_pct = round(na["dimensions"][3]["pct"])
    gh_pct = round(na["dimensions"][4]["pct"])

    # Behavioral & Leadership (STAR Method & Amazon Leadership Principles / Google Googliness)
    # Derived from overall consistency, achievements unlocked, and application metrics
    unlocked_count = gamification.get("total_badges_unlocked", 0)
    behavioral_pct = min(100, round(min(unlocked_count * 5 + 30, 95)))

    # Cloud & Distributed Concurrency
    cloud_pct = min(100, round(sd_pct * 0.75 + db_pct * 0.25))

    radar_labels = [
        "System Design (HLD)",
        "DSA (Med + Hard)",
        "AI / LLM Systems",
        "Database & Storage",
        "GitHub & OSS",
        "Behavioral / LP (STAR)",
        "Cloud & Concurrency",
    ]

    us_radar = [
        sd_pct,
        dsa_pct,
        ai_pct,
        db_pct,
        gh_pct,
        behavioral_pct,
        cloud_pct,
    ]

    ca_radar = [
        sd_pct,
        dsa_pct,
        ai_pct,
        db_pct,
        gh_pct,
        min(100, behavioral_pct + 5),
        cloud_pct,
    ]

    companies = get_na_company_profiles()
    company_stats = get_company_stats()

    return templates.TemplateResponse("na_readiness.html", {
        "request": request,
        "user": user,
        "gamification": gamification,
        "na": na,
        "us_score": us_score,
        "ca_score": ca_score,
        "combined_score": combined_score,
        "radar_labels_json": str(radar_labels).replace("'", '"'),
        "us_radar_json": str(us_radar),
        "ca_radar_json": str(ca_radar),
        "companies": companies,
        "company_stats": company_stats,
        "active_page": "na_readiness",
    })


# Route alias for /north-america-readiness
alias_router = APIRouter(prefix="/north-america-readiness", tags=["na_readiness"])

@alias_router.get("", response_class=RedirectResponse)
def north_america_readiness_redirect():
    return RedirectResponse(url="/na-readiness", status_code=301)
