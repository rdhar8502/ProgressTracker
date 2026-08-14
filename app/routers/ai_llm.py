from datetime import date
from typing import Optional
from fastapi import APIRouter, Depends, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.database import get_db
from app.models.ai_llm import AILLMTopic
from app.models.user import UserProfile

router = APIRouter(prefix="/ai-llm", tags=["ai-llm"])
templates = Jinja2Templates(directory="app/templates")

STATUSES = ["Not Started", "In Progress", "Done"]
DEPTH_LABELS = {1: "Surface", 2: "Comfortable", 3: "Deep"}


@router.get("", response_class=HTMLResponse)
def ai_page(
    request: Request,
    search: Optional[str] = None,
    db: Session = Depends(get_db),
):
    user = db.query(UserProfile).first()
    query = db.query(AILLMTopic)

    if search and search.strip():
        query = query.filter(
            or_(
                AILLMTopic.topic_name.ilike(f"%{search.strip()}%"),
                AILLMTopic.notes.ilike(f"%{search.strip()}%")
            )
        )

    topics = query.order_by(AILLMTopic.order_index).all()

    done = sum(1 for t in topics if t.status == "Done")
    in_progress = sum(1 for t in topics if t.status == "In Progress")
    pct = round((done / len(topics) * 100) if topics else 0)

    by_category = {}
    for t in topics:
        by_category.setdefault(t.category, []).append(t)

    return templates.TemplateResponse("ai_llm.html", {
        "request": request,
        "user": user,
        "today": date.today(),
        "topics": topics,
        "by_category": by_category,
        "done": done,
        "in_progress": in_progress,
        "total": len(topics),
        "pct": pct,
        "statuses": STATUSES,
        "depth_labels": DEPTH_LABELS,
        "selected_search": search or "",
        "active_page": "ai_llm",
    })


@router.post("/update/{topic_id}")
def update_topic(
    topic_id: int,
    status: str = Form(...),
    depth: int = Form(1),
    notes: str = Form(""),
    resources: str = Form(""),
    sources: str = Form(""),
    interview_talking_point: str = Form(""),
    db: Session = Depends(get_db),
):
    t = db.query(AILLMTopic).filter(AILLMTopic.id == topic_id).first()
    if not t:
        raise HTTPException(status_code=404)
    t.status = status
    t.depth = depth
    t.notes = notes
    t.resources = resources
    t.sources = sources
    t.interview_talking_point = interview_talking_point
    db.commit()
    return RedirectResponse(url="/ai-llm", status_code=303)
