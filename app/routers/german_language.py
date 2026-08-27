"""
German Language Learning router — /german-language
CRUD for tracking CEFR skill levels and certifications.
"""
from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import Optional

from app.database import get_db
from app.models.user import UserProfile
from app.models.german_lang import GermanLangSkill, GermanLangCert, GERMAN_SKILLS, CEFR_LEVELS, CEFR_METADATA

router = APIRouter(prefix="/german-language", tags=["german_language"])
templates = Jinja2Templates(directory="app/templates")


def _seed_default_skills(db: Session):
    """Create default skill rows if they don't exist."""
    for skill_name in GERMAN_SKILLS:
        existing = db.query(GermanLangSkill).filter(GermanLangSkill.skill == skill_name).first()
        if not existing:
            db.add(GermanLangSkill(skill=skill_name, current_level="A1", target_level="B1"))
    db.commit()


@router.get("", response_class=HTMLResponse)
def german_page(request: Request, db: Session = Depends(get_db)):
    user = db.query(UserProfile).first()
    _seed_default_skills(db)
    skills = db.query(GermanLangSkill).order_by(GermanLangSkill.id).all()
    certs  = db.query(GermanLangCert).order_by(GermanLangCert.id).all()

    # Compute overall score
    level_scores = {"A1": 10, "A2": 25, "B1": 55, "B2": 80, "C1": 100}
    skill_scores = [level_scores.get(s.current_level, 0) for s in skills]
    avg_score = round(sum(skill_scores) / len(skill_scores)) if skill_scores else 0
    cert_bonus = min(10, sum(1 for c in certs if c.passed) * 5)
    overall_score = min(100, avg_score + cert_bonus)

    return templates.TemplateResponse("german_language.html", {
        "request": request,
        "user": user,
        "skills": skills,
        "certs": certs,
        "cefr_levels": CEFR_LEVELS,
        "cefr_meta": CEFR_METADATA,
        "overall_score": overall_score,
        "active_page": "german_language",
    })


@router.post("/skill/update", response_class=RedirectResponse)
def update_skill(
    request: Request,
    skill_id: int = Form(...),
    current_level: str = Form(...),
    target_level: str = Form(...),
    notes: str = Form(""),
    resources: str = Form(""),
    db: Session = Depends(get_db),
):
    skill = db.query(GermanLangSkill).filter(GermanLangSkill.id == skill_id).first()
    if skill:
        if current_level in CEFR_LEVELS:
            skill.current_level = current_level
        if target_level in CEFR_LEVELS:
            skill.target_level = target_level
        skill.notes = notes
        skill.resources = resources
        db.commit()
    return RedirectResponse("/german-language?updated=1", status_code=303)


@router.post("/cert/add", response_class=RedirectResponse)
def add_cert(
    request: Request,
    cert_name: str = Form(...),
    level: str = Form(...),
    passed: Optional[str] = Form(None),
    score: str = Form(""),
    exam_date: str = Form(""),
    notes: str = Form(""),
    db: Session = Depends(get_db),
):
    cert = GermanLangCert(
        cert_name=cert_name,
        level=level,
        passed=(passed == "on"),
        score=score,
        exam_date=exam_date,
        notes=notes,
    )
    db.add(cert)
    db.commit()
    return RedirectResponse("/german-language?cert_added=1", status_code=303)


@router.post("/cert/delete/{cert_id}", response_class=RedirectResponse)
def delete_cert(cert_id: int, db: Session = Depends(get_db)):
    cert = db.query(GermanLangCert).filter(GermanLangCert.id == cert_id).first()
    if cert:
        db.delete(cert)
        db.commit()
    return RedirectResponse("/german-language", status_code=303)
