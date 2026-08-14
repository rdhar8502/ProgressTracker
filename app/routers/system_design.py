from datetime import date
from typing import Optional
from fastapi import APIRouter, Depends, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import func, or_

from app.database import get_db
from app.models.system_design import SystemDesignConcept, SystemDesignSubConcept, SystemDesignCase
from app.models.user import UserProfile

router = APIRouter(prefix="/system-design", tags=["system-design"])
templates = Jinja2Templates(directory="app/templates")

STATUSES = ["Not Started", "In Progress", "Done"]


@router.get("", response_class=HTMLResponse)
def sd_page(
    request: Request,
    search: Optional[str] = None,
    db: Session = Depends(get_db),
):
    user = db.query(UserProfile).first()

    concepts_query = db.query(SystemDesignConcept)
    sub_concepts_query = db.query(SystemDesignSubConcept)
    cases_query = db.query(SystemDesignCase)

    if search and search.strip():
        search_clean = search.strip()
        # Find concept_ids that match subconcepts
        matching_subconcept_ids = db.query(SystemDesignSubConcept.concept_id).filter(
            or_(
                SystemDesignSubConcept.subconcept_name.ilike(f"%{search_clean}%"),
                SystemDesignSubConcept.notes.ilike(f"%{search_clean}%")
            )
        ).subquery()

        concepts_query = concepts_query.filter(
            or_(
                SystemDesignConcept.concept_name.ilike(f"%{search_clean}%"),
                SystemDesignConcept.id.in_(matching_subconcept_ids)
            )
        )

        sub_concepts_query = sub_concepts_query.filter(
            or_(
                SystemDesignSubConcept.subconcept_name.ilike(f"%{search_clean}%"),
                SystemDesignSubConcept.notes.ilike(f"%{search_clean}%")
            )
        )

        cases_query = cases_query.filter(
            or_(
                SystemDesignCase.system_name.ilike(f"%{search_clean}%"),
                SystemDesignCase.notes.ilike(f"%{search_clean}%"),
                SystemDesignCase.key_components.ilike(f"%{search_clean}%")
            )
        )

    concepts = concepts_query.order_by(SystemDesignConcept.order_index).all()
    sub_concepts = sub_concepts_query.order_by(SystemDesignSubConcept.order_index).all()
    cases = cases_query.order_by(SystemDesignCase.order_index).all()

    # Re-calculate counts based on full set if search is active or just keep search-filtered metrics
    topics_done = sum(1 for sc in sub_concepts if sc.status == "Done")
    topics_in_progress = sum(1 for sc in sub_concepts if sc.status == "In Progress")
    topics_total = len(sub_concepts)

    cases_done = sum(1 for c in cases if c.status == "Done")
    cases_in_progress = sum(1 for c in cases if c.status == "In Progress")

    by_category = {}
    for c in concepts:
        by_category.setdefault(c.category, []).append(c)

    return templates.TemplateResponse("system_design.html", {
        "request": request,
        "user": user,
        "today": date.today(),
        "concepts": concepts,
        "cases": cases,
        "by_category": by_category,
        "topics_done": topics_done,
        "topics_in_progress": topics_in_progress,
        "topics_total": topics_total,
        "cases_done": cases_done,
        "cases_in_progress": cases_in_progress,
        "cases_total": len(cases),
        "statuses": STATUSES,
        "selected_search": search or "",
        "active_page": "system_design",
    })


@router.post("/concept/add")
def add_concept(
    concept_name: str = Form(...),
    category: str = Form(...),
    sources: str = Form(""),
    db: Session = Depends(get_db),
):
    max_order = db.query(func.max(SystemDesignConcept.order_index)).scalar() or 0
    concept = SystemDesignConcept(
        concept_name=concept_name,
        category=category,
        sources=sources,
        order_index=max_order + 1
    )
    db.add(concept)
    db.commit()
    return RedirectResponse(url="/system-design", status_code=303)


@router.post("/concept/update/{concept_id}")
def update_concept(
    concept_id: int,
    concept_name: str = Form(...),
    category: str = Form(...),
    sources: str = Form(""),
    db: Session = Depends(get_db),
):
    concept = db.query(SystemDesignConcept).filter(SystemDesignConcept.id == concept_id).first()
    if not concept:
        raise HTTPException(status_code=404, detail="Concept not found")
    concept.concept_name = concept_name
    concept.category = category
    concept.sources = sources
    db.commit()
    return RedirectResponse(url="/system-design", status_code=303)


@router.post("/concept/delete/{concept_id}")
def delete_concept(
    concept_id: int,
    db: Session = Depends(get_db),
):
    concept = db.query(SystemDesignConcept).filter(SystemDesignConcept.id == concept_id).first()
    if not concept:
        raise HTTPException(status_code=404, detail="Concept not found")
    db.delete(concept)
    db.commit()
    return RedirectResponse(url="/system-design", status_code=303)


@router.post("/subconcept/add")
def add_subconcept(
    concept_id: int = Form(...),
    subconcept_name: str = Form(...),
    db: Session = Depends(get_db),
):
    max_order = db.query(func.max(SystemDesignSubConcept.order_index)).filter(SystemDesignSubConcept.concept_id == concept_id).scalar() or 0
    sub = SystemDesignSubConcept(
        concept_id=concept_id,
        subconcept_name=subconcept_name,
        order_index=max_order + 1,
        status="Not Started"
    )
    db.add(sub)
    db.commit()
    return RedirectResponse(url="/system-design", status_code=303)


@router.post("/subconcept/update/{sub_id}")
def update_subconcept(
    sub_id: int,
    status: str = Form(...),
    reading_done: bool = Form(False),
    practical_done: bool = Form(False),
    notes: str = Form(""),
    resources: str = Form(""),
    sources: str = Form(""),
    db: Session = Depends(get_db),
):
    sub = db.query(SystemDesignSubConcept).filter(SystemDesignSubConcept.id == sub_id).first()
    if not sub:
        raise HTTPException(status_code=404, detail="Subconcept not found")
    sub.status = status
    sub.reading_done = reading_done
    sub.practical_done = practical_done
    sub.notes = notes
    sub.resources = resources
    sub.sources = sources
    db.commit()
    return RedirectResponse(url="/system-design", status_code=303)


@router.post("/subconcept/delete/{sub_id}")
def delete_subconcept(
    sub_id: int,
    db: Session = Depends(get_db),
):
    sub = db.query(SystemDesignSubConcept).filter(SystemDesignSubConcept.id == sub_id).first()
    if not sub:
        raise HTTPException(status_code=404, detail="Subconcept not found")
    db.delete(sub)
    db.commit()
    return RedirectResponse(url="/system-design", status_code=303)


@router.post("/subconcept/quick-update/{sub_id}")
def quick_update_subconcept(
    sub_id: int,
    status: str = Form(...),
    db: Session = Depends(get_db),
):
    sub = db.query(SystemDesignSubConcept).filter(SystemDesignSubConcept.id == sub_id).first()
    if not sub:
        raise HTTPException(status_code=404, detail="Subconcept not found")
    sub.status = status
    db.commit()
    return RedirectResponse(url="/system-design", status_code=303)


# Compatibility/Legacy endpoint
@router.post("/topic/update/{topic_id}")
def update_topic(
    topic_id: int,
    status: str = Form(...),
    reading_done: bool = Form(False),
    practical_done: bool = Form(False),
    notes: str = Form(""),
    db: Session = Depends(get_db),
):
    return update_subconcept(
        sub_id=topic_id,
        status=status,
        reading_done=reading_done,
        practical_done=practical_done,
        notes=notes,
        db=db
    )


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
