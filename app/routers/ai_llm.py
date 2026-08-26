from datetime import date
from typing import Optional
from fastapi import APIRouter, Depends, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import or_, func

from app.database import get_db
from app.models.ai_llm import AILLMTopic
from app.models.user import UserProfile

router = APIRouter(prefix="/ai-llm", tags=["ai-llm"])
templates = Jinja2Templates(directory="app/templates")

STATUSES = ["Not Started", "In Progress", "Done"]
DEPTH_LABELS = {1: "Surface", 2: "Comfortable", 3: "Deep"}
DEFAULT_CATEGORIES = ["Core", "RAG", "Agents", "Production"]


@router.get("", response_class=HTMLResponse)
def ai_page(
    request: Request,
    search: Optional[str] = None,
    category: Optional[str] = None,
    status_filter: Optional[str] = None,
    depth_filter: Optional[str] = None,
    db: Session = Depends(get_db),
):
    user = db.query(UserProfile).first()
    all_topics = db.query(AILLMTopic).order_by(AILLMTopic.order_index, AILLMTopic.id).all()

    # All unique categories in DB
    existing_categories = [c[0] for c in db.query(AILLMTopic.category).distinct().all() if c[0]]
    categories = sorted(list(set(DEFAULT_CATEGORIES + existing_categories)))

    # Stats based on all topics
    total = len(all_topics)
    done = sum(1 for t in all_topics if t.status == "Done")
    in_progress = sum(1 for t in all_topics if t.status == "In Progress")
    not_started = sum(1 for t in all_topics if t.status == "Not Started")
    pct = round((done / total * 100) if total else 0)

    # Filtered query
    query = db.query(AILLMTopic)

    if category and category != "all":
        query = query.filter(AILLMTopic.category == category)

    if status_filter and status_filter != "all":
        query = query.filter(AILLMTopic.status == status_filter)

    if depth_filter and depth_filter != "all":
        try:
            depth_val = int(depth_filter)
            query = query.filter(AILLMTopic.depth == depth_val)
        except ValueError:
            pass

    if search and search.strip():
        term = f"%{search.strip()}%"
        query = query.filter(
            or_(
                AILLMTopic.topic_name.ilike(term),
                AILLMTopic.notes.ilike(term),
                AILLMTopic.interview_talking_point.ilike(term),
                AILLMTopic.category.ilike(term),
                AILLMTopic.sources.ilike(term),
            )
        )

    filtered_topics = query.order_by(AILLMTopic.order_index, AILLMTopic.id).all()

    by_category = {}
    for t in filtered_topics:
        by_category.setdefault(t.category or "General", []).append(t)

    return templates.TemplateResponse("ai_llm.html", {
        "request": request,
        "user": user,
        "today": date.today(),
        "topics": filtered_topics,
        "all_topics_count": total,
        "by_category": by_category,
        "categories": categories,
        "done": done,
        "in_progress": in_progress,
        "not_started": not_started,
        "total": total,
        "pct": pct,
        "statuses": STATUSES,
        "depth_labels": DEPTH_LABELS,
        "selected_search": search or "",
        "selected_category": category or "all",
        "selected_status": status_filter or "all",
        "selected_depth": depth_filter or "all",
        "active_page": "ai_llm",
    })


@router.post("/update/{topic_id}")
def update_or_create_topic(
    topic_id: int,
    topic_name: Optional[str] = Form(None),
    category: Optional[str] = Form(None),
    status: str = Form("Not Started"),
    depth: int = Form(1),
    notes: str = Form(""),
    resources: str = Form(""),
    sources: str = Form(""),
    interview_talking_point: str = Form(""),
    db: Session = Depends(get_db),
):
    if topic_id == 0:
        # Create new topic
        max_order = db.query(func.max(AILLMTopic.order_index)).scalar() or 0
        t = AILLMTopic(
            topic_name=topic_name or "New Topic",
            category=category or "Core",
            order_index=max_order + 1,
            status=status,
            depth=depth,
            notes=notes,
            resources=resources,
            sources=sources,
            interview_talking_point=interview_talking_point,
        )
        db.add(t)
    else:
        t = db.query(AILLMTopic).filter(AILLMTopic.id == topic_id).first()
        if not t:
            raise HTTPException(status_code=404, detail="Topic not found")
        if topic_name:
            t.topic_name = topic_name
        if category:
            t.category = category
        t.status = status
        t.depth = depth
        t.notes = notes
        t.resources = resources
        t.sources = sources
        t.interview_talking_point = interview_talking_point

    db.commit()
    return RedirectResponse(url="/ai-llm", status_code=303)


@router.post("/toggle-status/{topic_id}")
def toggle_topic_status(
    topic_id: int,
    db: Session = Depends(get_db),
):
    t = db.query(AILLMTopic).filter(AILLMTopic.id == topic_id).first()
    if not t:
        raise HTTPException(status_code=404, detail="Topic not found")

    cycle = {"Not Started": "In Progress", "In Progress": "Done", "Done": "Not Started"}
    t.status = cycle.get(t.status, "In Progress")
    db.commit()

    return JSONResponse({
        "success": True,
        "id": t.id,
        "status": t.status
    })


@router.post("/delete/{topic_id}")
def delete_topic(
    topic_id: int,
    db: Session = Depends(get_db),
):
    t = db.query(AILLMTopic).filter(AILLMTopic.id == topic_id).first()
    if not t:
        raise HTTPException(status_code=404, detail="Topic not found")
    db.delete(t)
    db.commit()
    return RedirectResponse(url="/ai-llm", status_code=303)

