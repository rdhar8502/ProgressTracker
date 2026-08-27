"""
EU Readiness page router — /eu-readiness
Serves the standalone EU Interview Readiness Radar page with Germany & Netherlands standards.
"""
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import UserProfile
from app.models.german_lang import GermanLangSkill, GermanLangCert, CEFR_LEVELS, CEFR_METADATA
from app.models.dutch_lang import DutchLangSkill, DutchLangCert, CEFR_LEVELS_DUTCH, CEFR_METADATA_DUTCH
from app.services.gamification import get_gamification_state

router = APIRouter(prefix="/eu-readiness", tags=["eu_readiness"])
templates = Jinja2Templates(directory="app/templates")


def _get_german_score(db: Session) -> dict:
    """Compute a 0-100 German language readiness score from skills in DB."""
    skills = db.query(GermanLangSkill).all()
    certs  = db.query(GermanLangCert).filter(GermanLangCert.passed == True).all()

    if not skills:
        return {
            "score": 0,
            "skills": [],
            "certs": [],
            "avg_level": "A1",
            "highest_cert": None,
            "status_label": "Not Started",
            "status_color": "#6B7280",
        }

    level_scores = {"A1": 10, "A2": 25, "B1": 55, "B2": 80, "C1": 100}
    skill_scores = [level_scores.get(s.current_level, 0) for s in skills]
    raw_score = round(sum(skill_scores) / len(skill_scores)) if skill_scores else 0

    # Certification bonus (max +10)
    cert_bonus = min(10, len(certs) * 5)
    score = min(100, raw_score + cert_bonus)

    avg_val = sum(skill_scores) / len(skill_scores) if skill_scores else 0
    if avg_val >= 80:   avg_level = "B2"
    elif avg_val >= 55: avg_level = "B1"
    elif avg_val >= 25: avg_level = "A2"
    else:               avg_level = "A1"

    cert_order = {v: i for i, v in enumerate(CEFR_LEVELS)}
    passed_certs = [c for c in certs]
    highest_cert = max(passed_certs, key=lambda c: cert_order.get(c.level, 0)) if passed_certs else None

    if score >= 75:    status_label, status_color = "Job-Interview Ready",  "#10B981"
    elif score >= 50:  status_label, status_color = "Blue Card Eligible",    "#F59E0B"
    elif score >= 25:  status_label, status_color = "Building Foundation",   "#F97316"
    else:              status_label, status_color = "Just Started",           "#EF4444"

    return {
        "score": score,
        "skills": skills,
        "certs": certs,
        "avg_level": avg_level,
        "highest_cert": highest_cert,
        "status_label": status_label,
        "status_color": status_color,
        "cefr_levels": CEFR_LEVELS,
        "cefr_meta": CEFR_METADATA,
    }


def _get_dutch_score(db: Session) -> dict:
    """Compute a 0-100 Dutch language readiness score from skills in DB."""
    skills = db.query(DutchLangSkill).all()
    certs  = db.query(DutchLangCert).filter(DutchLangCert.passed == True).all()

    if not skills:
        return {
            "score": 0,
            "skills": [],
            "certs": [],
            "avg_level": "A1",
            "highest_cert": None,
            "status_label": "Not Started",
            "status_color": "#6B7280",
        }

    level_scores = {"A1": 10, "A2": 25, "B1": 55, "B2": 80, "C1": 100}
    skill_scores = [level_scores.get(s.current_level, 0) for s in skills]
    raw_score = round(sum(skill_scores) / len(skill_scores)) if skill_scores else 0

    # Certification bonus (max +10)
    cert_bonus = min(10, len(certs) * 5)
    score = min(100, raw_score + cert_bonus)

    avg_val = sum(skill_scores) / len(skill_scores) if skill_scores else 0
    if avg_val >= 80:   avg_level = "B2"
    elif avg_val >= 55: avg_level = "B1"
    elif avg_val >= 25: avg_level = "A2"
    else:               avg_level = "A1"

    cert_order = {v: i for i, v in enumerate(CEFR_LEVELS_DUTCH)}
    passed_certs = [c for c in certs]
    highest_cert = max(passed_certs, key=lambda c: cert_order.get(c.level, 0)) if passed_certs else None

    if score >= 75:    status_label, status_color = "Workplace Fluent",      "#10B981"
    elif score >= 50:  status_label, status_color = "NT2-I / Inburgering",   "#F59E0B"
    elif score >= 25:  status_label, status_color = "Basic Conversational",  "#F97316"
    else:              status_label, status_color = "Just Started",          "#EF4444"

    return {
        "score": score,
        "skills": skills,
        "certs": certs,
        "avg_level": avg_level,
        "highest_cert": highest_cert,
        "status_label": status_label,
        "status_color": status_color,
        "cefr_levels": CEFR_LEVELS_DUTCH,
        "cefr_meta": CEFR_METADATA_DUTCH,
    }


@router.get("", response_class=HTMLResponse)
def eu_readiness_page(request: Request, db: Session = Depends(get_db)):
    user = db.query(UserProfile).first()
    gamification = get_gamification_state(db)
    eu = gamification["eu_readiness"]
    german = _get_german_score(db)
    dutch = _get_dutch_score(db)

    # Enhanced combined score incorporating both German & Dutch languages
    german_weight = 0.06   # 6% German weight for overall EU
    dutch_weight = 0.04    # 4% Dutch weight for overall EU
    base_combined = eu["combined_score"]
    enhanced_combined = round(
        base_combined * (1 - german_weight - dutch_weight) + 
        german["score"] * german_weight + 
        dutch["score"] * dutch_weight, 
        1
    )
    enhanced_combined = min(100, enhanced_combined)

    # Enhanced individual country scores incorporating language
    de_score_enhanced = min(100, round(eu["de_score"] * 0.90 + german["score"] * 0.10, 1))
    nl_score_enhanced = min(100, round(eu["nl_score"] * 0.93 + dutch["score"] * 0.07, 1))

    # Build radar chart data (7 axes)
    radar_labels = [
        "System Design",
        "DSA (Medium+Hard)",
        "Database Mastery",
        "AI / LLM",
        "GitHub Portfolio",
        "🇩🇪 German Lang",
        "🇳🇱 Dutch Lang",
    ]
    de_radar = [
        round(eu["dimensions"][0]["pct"]),   # System Design
        round(eu["dimensions"][1]["pct"]),   # DSA Medium
        round(eu["dimensions"][2]["pct"]),   # DB
        round(eu["dimensions"][3]["pct"]),   # AI
        round(eu["dimensions"][4]["pct"]),   # GitHub
        german["score"],
        min(dutch["score"], 40),             # Minor presence for DE
    ]
    nl_radar = [
        round(eu["dimensions"][0]["pct"]),   # System Design
        round(eu["dimensions"][1]["pct"]),   # DSA Medium
        round(eu["dimensions"][2]["pct"]),   # DB
        round(eu["dimensions"][3]["pct"]),   # AI
        round(eu["dimensions"][4]["pct"]),   # GitHub
        min(german["score"], 40),            # Minor presence for NL
        dutch["score"],
    ]

    return templates.TemplateResponse("eu_readiness.html", {
        "request": request,
        "user": user,
        "gamification": gamification,
        "eu": eu,
        "german": german,
        "dutch": dutch,
        "de_score_enhanced": de_score_enhanced,
        "nl_score_enhanced": nl_score_enhanced,
        "enhanced_combined": enhanced_combined,
        "radar_labels_json": str(radar_labels).replace("'", '"'),
        "de_radar_json": str(de_radar),
        "nl_radar_json": str(nl_radar),
        "active_page": "eu_readiness",
    })
