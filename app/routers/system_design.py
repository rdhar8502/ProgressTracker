from datetime import date
from fastapi import APIRouter, Depends, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.system_design import SystemDesignTopic, SystemDesignCase
from app.models.user import UserProfile

router = APIRouter(prefix="/system-design", tags=["system-design"])
templates = Jinja2Templates(directory="app/templates")

STATUSES = ["Not Started", "In Progress", "Done"]


@router.get("", response_class=HTMLResponse)
def sd_page(request: Request, db: Session = Depends(get_db)):
    user = db.query(UserProfile).first()
    topics = db.query(SystemDesignTopic).order_by(SystemDesignTopic.order_index).all()
    cases = db.query(SystemDesignCase).order_by(SystemDesignCase.order_index).all()

    topics_done = sum(1 for t in topics if t.status == "Done")
    topics_in_progress = sum(1 for t in topics if t.status == "In Progress")
    cases_done = sum(1 for c in cases if c.status == "Done")
    cases_in_progress = sum(1 for c in cases if c.status == "In Progress")

    by_category = {}
    for t in topics:
        by_category.setdefault(t.category, []).append(t)

    return templates.TemplateResponse("system_design.html", {
        "request": request,
        "user": user,
        "today": date.today(),
        "topics": topics,
        "cases": cases,
        "by_category": by_category,
        "topics_done": topics_done,
        "topics_in_progress": topics_in_progress,
        "topics_total": len(topics),
        "cases_done": cases_done,
        "cases_in_progress": cases_in_progress,
        "cases_total": len(cases),
        "statuses": STATUSES,
        "active_page": "system_design",
    })


@router.post("/topic/update/{topic_id}")
def update_topic(
    topic_id: int,
    status: str = Form(...),
    reading_done: bool = Form(False),
    practical_done: bool = Form(False),
    notes: str = Form(""),
    db: Session = Depends(get_db),
):
    t = db.query(SystemDesignTopic).filter(SystemDesignTopic.id == topic_id).first()
    if not t:
        raise HTTPException(status_code=404)
    t.status = status
    t.reading_done = reading_done
    t.practical_done = practical_done
    t.notes = notes
    db.commit()
    return RedirectResponse(url="/system-design", status_code=303)


@router.post("/case/update/{case_id}")
def update_case(
    case_id: int,
    status: str = Form(...),
    key_components: str = Form(""),
    diagram_url: str = Form(""),
    notes: str = Form(""),
    db: Session = Depends(get_db),
):
    c = db.query(SystemDesignCase).filter(SystemDesignCase.id == case_id).first()
    if not c:
        raise HTTPException(status_code=404)
    c.status = status
    c.key_components = key_components
    c.diagram_url = diagram_url
    c.notes = notes
    db.commit()
    return RedirectResponse(url="/system-design", status_code=303)
