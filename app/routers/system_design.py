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
    track: Optional[str] = "all",
    category: Optional[str] = None,
    status_filter: Optional[str] = "all",
    search: Optional[str] = None,
    db: Session = Depends(get_db),
):
    user = db.query(UserProfile).first()

    # Base queries for full counts across database
    all_concepts = db.query(SystemDesignConcept).order_by(SystemDesignConcept.order_index).all()
    all_sub_concepts = db.query(SystemDesignSubConcept).order_by(SystemDesignSubConcept.order_index).all()
    all_cases = db.query(SystemDesignCase).order_by(SystemDesignCase.order_index).all()

    # --- Compute HLD Metrics ---
    hld_concept_ids = [c.id for c in all_concepts if (c.track or "HLD").upper() == "HLD"]
    hld_subs = [sc for sc in all_sub_concepts if sc.concept_id in hld_concept_ids]
    hld_cases = [c for c in all_cases if (c.track or "HLD").upper() == "HLD"]

    hld_subs_done = sum(1 for sc in hld_subs if sc.status == "Done")
    hld_subs_in_progress = sum(1 for sc in hld_subs if sc.status == "In Progress")
    hld_cases_done = sum(1 for c in hld_cases if c.status == "Done")
    hld_cases_in_progress = sum(1 for c in hld_cases if c.status == "In Progress")

    hld_total_items = len(hld_subs) + len(hld_cases)
    hld_done_items = hld_subs_done + hld_cases_done
    hld_pct = round((hld_done_items / hld_total_items * 100) if hld_total_items > 0 else 0)

    # --- Compute LLD Metrics ---
    lld_concept_ids = [c.id for c in all_concepts if (c.track or "").upper() == "LLD"]
    lld_subs = [sc for sc in all_sub_concepts if sc.concept_id in lld_concept_ids]
    lld_cases = [c for c in all_cases if (c.track or "").upper() == "LLD"]

    lld_subs_done = sum(1 for sc in lld_subs if sc.status == "Done")
    lld_subs_in_progress = sum(1 for sc in lld_subs if sc.status == "In Progress")
    lld_cases_done = sum(1 for c in lld_cases if c.status == "Done")
    lld_cases_in_progress = sum(1 for c in lld_cases if c.status == "In Progress")

    lld_total_items = len(lld_subs) + len(lld_cases)
    lld_done_items = lld_subs_done + lld_cases_done
    lld_pct = round((lld_done_items / lld_total_items * 100) if lld_total_items > 0 else 0)

    # --- Compute AI System Design Metrics ---
    ai_concept_ids = [c.id for c in all_concepts if (c.track or "").upper() in ["AI", "AI SD", "AI_SD"]]
    ai_subs = [sc for sc in all_sub_concepts if sc.concept_id in ai_concept_ids]
    ai_cases = [c for c in all_cases if (c.track or "").upper() in ["AI", "AI SD", "AI_SD"]]

    ai_subs_done = sum(1 for sc in ai_subs if sc.status == "Done")
    ai_subs_in_progress = sum(1 for sc in ai_subs if sc.status == "In Progress")
    ai_cases_done = sum(1 for c in ai_cases if c.status == "Done")
    ai_cases_in_progress = sum(1 for c in ai_cases if c.status == "In Progress")

    ai_total_items = len(ai_subs) + len(ai_cases)
    ai_done_items = ai_subs_done + ai_cases_done
    ai_pct = round((ai_done_items / ai_total_items * 100) if ai_total_items > 0 else 0)

    # --- Overall Combined Metrics ---
    total_subs = len(all_sub_concepts)
    total_subs_done = sum(1 for sc in all_sub_concepts if sc.status == "Done")
    total_subs_in_progress = sum(1 for sc in all_sub_concepts if sc.status == "In Progress")
    
    total_cases = len(all_cases)
    total_cases_done = sum(1 for c in all_cases if c.status == "Done")
    total_cases_in_progress = sum(1 for c in all_cases if c.status == "In Progress")

    reading_done_count = sum(1 for sc in all_sub_concepts if sc.reading_done)
    practical_done_count = sum(1 for sc in all_sub_concepts if sc.practical_done)

    overall_total = total_subs + total_cases
    overall_done = total_subs_done + total_cases_done
    overall_pct = round((overall_done / overall_total * 100) if overall_total > 0 else 0)

    # --- Filtered Concept and Case Queries ---
    concepts_query = db.query(SystemDesignConcept)
    cases_query = db.query(SystemDesignCase)

    # Apply Track Filter
    selected_track = (track or "all").strip().lower()
    if selected_track in ["hld", "lld", "ai", "ai_sd", "ai-sd"]:
        if selected_track in ["ai", "ai_sd", "ai-sd"]:
            concepts_query = concepts_query.filter(func.upper(SystemDesignConcept.track).in_(["AI", "AI SD", "AI_SD"]))
            cases_query = cases_query.filter(func.upper(SystemDesignCase.track).in_(["AI", "AI SD", "AI_SD"]))
        else:
            concepts_query = concepts_query.filter(func.upper(SystemDesignConcept.track) == selected_track.upper())
            cases_query = cases_query.filter(func.upper(SystemDesignCase.track) == selected_track.upper())

    # Apply Category Filter
    if category and category.strip() and category.strip() != "all":
        concepts_query = concepts_query.filter(SystemDesignConcept.category == category.strip())
        cases_query = cases_query.filter(SystemDesignCase.category == category.strip())

    # Apply Search Filter
    if search and search.strip():
        search_clean = search.strip()
        matching_subconcept_ids = db.query(SystemDesignSubConcept.concept_id).filter(
            or_(
                SystemDesignSubConcept.subconcept_name.ilike(f"%{search_clean}%"),
                SystemDesignSubConcept.notes.ilike(f"%{search_clean}%"),
                SystemDesignSubConcept.sources.ilike(f"%{search_clean}%")
            )
        ).subquery()

        concepts_query = concepts_query.filter(
            or_(
                SystemDesignConcept.concept_name.ilike(f"%{search_clean}%"),
                SystemDesignConcept.category.ilike(f"%{search_clean}%"),
                SystemDesignConcept.id.in_(matching_subconcept_ids)
            )
        )

        cases_query = cases_query.filter(
            or_(
                SystemDesignCase.system_name.ilike(f"%{search_clean}%"),
                SystemDesignCase.category.ilike(f"%{search_clean}%"),
                SystemDesignCase.notes.ilike(f"%{search_clean}%"),
                SystemDesignCase.key_components.ilike(f"%{search_clean}%")
            )
        )

    filtered_concepts = concepts_query.order_by(SystemDesignConcept.order_index).all()
    filtered_cases = cases_query.order_by(SystemDesignCase.order_index).all()

    # Group concepts by category, preserving track separation
    by_category_hld = {}
    by_category_lld = {}
    by_category_ai = {}
    for c in filtered_concepts:
        c_track = (c.track or "HLD").upper()
        if c_track in ["AI", "AI SD", "AI_SD"]:
            by_category_ai.setdefault(c.category, []).append(c)
        elif c_track == "LLD":
            by_category_lld.setdefault(c.category, []).append(c)
        else:
            by_category_hld.setdefault(c.category, []).append(c)

    # Group cases by track
    cases_hld = [c for c in filtered_cases if (c.track or "HLD").upper() == "HLD"]
    cases_lld = [c for c in filtered_cases if (c.track or "").upper() == "LLD"]
    cases_ai = [c for c in filtered_cases if (c.track or "").upper() in ["AI", "AI SD", "AI_SD"]]

    return templates.TemplateResponse("system_design.html", {
        "request": request,
        "user": user,
        "today": date.today(),
        "selected_track": selected_track,
        "selected_category": category or "all",
        "selected_status": status_filter or "all",
        "selected_search": search or "",
        
        # Concepts & Groupings
        "concepts": filtered_concepts,
        "by_category_hld": by_category_hld,
        "by_category_lld": by_category_lld,
        "by_category_ai": by_category_ai,
        
        # Cases & Groupings
        "cases": filtered_cases,
        "cases_hld": cases_hld,
        "cases_lld": cases_lld,
        "cases_ai": cases_ai,
        
        # HLD Stats
        "hld_subs_total": len(hld_subs),
        "hld_subs_done": hld_subs_done,
        "hld_subs_in_progress": hld_subs_in_progress,
        "hld_cases_total": len(hld_cases),
        "hld_cases_done": hld_cases_done,
        "hld_cases_in_progress": hld_cases_in_progress,
        "hld_pct": hld_pct,
        
        # LLD Stats
        "lld_subs_total": len(lld_subs),
        "lld_subs_done": lld_subs_done,
        "lld_subs_in_progress": lld_subs_in_progress,
        "lld_cases_total": len(lld_cases),
        "lld_cases_done": lld_cases_done,
        "lld_cases_in_progress": lld_cases_in_progress,
        "lld_pct": lld_pct,

        # AI Stats
        "ai_subs_total": len(ai_subs),
        "ai_subs_done": ai_subs_done,
        "ai_subs_in_progress": ai_subs_in_progress,
        "ai_cases_total": len(ai_cases),
        "ai_cases_done": ai_cases_done,
        "ai_cases_in_progress": ai_cases_in_progress,
        "ai_pct": ai_pct,
        
        # Overall Stats
        "topics_total": total_subs,
        "topics_done": total_subs_done,
        "topics_in_progress": total_subs_in_progress,
        "cases_total": total_cases,
        "cases_done": total_cases_done,
        "cases_in_progress": total_cases_in_progress,
        "reading_done_count": reading_done_count,
        "practical_done_count": practical_done_count,
        "overall_total": overall_total,
        "overall_done": overall_done,
        "overall_pct": overall_pct,
        
        "statuses": STATUSES,
        "active_page": "system_design",
    })


@router.post("/concept/add")
def add_concept(
    concept_name: str = Form(...),
    track: str = Form("HLD"),
    category: str = Form(...),
    sources: str = Form(""),
    db: Session = Depends(get_db),
):
    max_order = db.query(func.max(SystemDesignConcept.order_index)).scalar() or 0
    concept = SystemDesignConcept(
        track=track.strip().upper(),
        concept_name=concept_name.strip(),
        category=category.strip(),
        sources=sources.strip(),
        order_index=max_order + 1
    )
    db.add(concept)
    db.commit()
    return RedirectResponse(url=f"/system-design?track={track.lower()}", status_code=303)


@router.post("/concept/update/{concept_id}")
def update_concept(
    concept_id: int,
    concept_name: str = Form(...),
    track: str = Form("HLD"),
    category: str = Form(...),
    sources: str = Form(""),
    db: Session = Depends(get_db),
):
    concept = db.query(SystemDesignConcept).filter(SystemDesignConcept.id == concept_id).first()
    if not concept:
        raise HTTPException(status_code=404, detail="Concept not found")
    concept.concept_name = concept_name.strip()
    concept.track = track.strip().upper()
    concept.category = category.strip()
    concept.sources = sources.strip()
    db.commit()
    return RedirectResponse(url=f"/system-design?track={track.lower()}", status_code=303)


@router.post("/concept/delete/{concept_id}")
def delete_concept(
    concept_id: int,
    db: Session = Depends(get_db),
):
    concept = db.query(SystemDesignConcept).filter(SystemDesignConcept.id == concept_id).first()
    if not concept:
        raise HTTPException(status_code=404, detail="Concept not found")
    track = (concept.track or "all").lower()
    db.delete(concept)
    db.commit()
    return RedirectResponse(url=f"/system-design?track={track}", status_code=303)


@router.post("/subconcept/add")
def add_subconcept(
    concept_id: int = Form(...),
    subconcept_name: str = Form(...),
    db: Session = Depends(get_db),
):
    max_order = db.query(func.max(SystemDesignSubConcept.order_index)).filter(SystemDesignSubConcept.concept_id == concept_id).scalar() or 0
    sub = SystemDesignSubConcept(
        concept_id=concept_id,
        subconcept_name=subconcept_name.strip(),
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
    sub.resources = resources.strip()
    sub.sources = sources.strip()
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


@router.post("/case/add")
def add_case(
    system_name: str = Form(...),
    track: str = Form("HLD"),
    category: str = Form("Distributed Systems"),
    key_components: str = Form(""),
    diagram_url: str = Form(""),
    notes: str = Form(""),
    db: Session = Depends(get_db),
):
    max_order = db.query(func.max(SystemDesignCase.order_index)).scalar() or 0
    c = SystemDesignCase(
        track=track.strip().upper(),
        category=category.strip(),
        system_name=system_name.strip(),
        key_components=key_components.strip(),
        diagram_url=diagram_url.strip(),
        notes=notes,
        order_index=max_order + 1,
        status="Not Started"
    )
    db.add(c)
    db.commit()
    return RedirectResponse(url=f"/system-design?track={track.lower()}", status_code=303)


@router.post("/case/update/{case_id}")
def update_case(
    case_id: int,
    status: str = Form(...),
    track: str = Form("HLD"),
    category: str = Form("Distributed Systems"),
    key_components: str = Form(""),
    diagram_url: str = Form(""),
    notes: str = Form(""),
    db: Session = Depends(get_db),
):
    c = db.query(SystemDesignCase).filter(SystemDesignCase.id == case_id).first()
    if not c:
        raise HTTPException(status_code=404, detail="Case study not found")
    c.status = status
    c.track = track.strip().upper()
    c.category = category.strip()
    c.key_components = key_components.strip()
    c.diagram_url = diagram_url.strip()
    c.notes = notes
    db.commit()
    return RedirectResponse(url=f"/system-design?track={track.lower()}", status_code=303)


@router.post("/case/quick-update/{case_id}")
def quick_update_case(
    case_id: int,
    status: str = Form(...),
    db: Session = Depends(get_db),
):
    c = db.query(SystemDesignCase).filter(SystemDesignCase.id == case_id).first()
    if not c:
        raise HTTPException(status_code=404, detail="Case study not found")
    c.status = status
    db.commit()
    return RedirectResponse(url="/system-design", status_code=303)


@router.post("/case/delete/{case_id}")
def delete_case(
    case_id: int,
    db: Session = Depends(get_db),
):
    c = db.query(SystemDesignCase).filter(SystemDesignCase.id == case_id).first()
    if not c:
        raise HTTPException(status_code=404, detail="Case study not found")
    track = (c.track or "all").lower()
    db.delete(c)
    db.commit()
    return RedirectResponse(url=f"/system-design?track={track}", status_code=303)

