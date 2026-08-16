from datetime import date
from typing import Optional
from fastapi import APIRouter, Depends, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import func, or_

from app.database import get_db
from app.models.database_track import DatabaseConcept, DatabaseItem, DatabaseChallenge
from app.models.user import UserProfile

router = APIRouter(prefix="/database", tags=["database"])
templates = Jinja2Templates(directory="app/templates")

STATUSES = ["Not Started", "In Progress", "Done"]
DEPTH_LABELS = {1: "Surface", 2: "Comfortable", 3: "Deep"}
TRACK_NAMES = {
    "all": "All Database Tracks",
    "sql": "SQL Mastery",
    "joins_functions": "Joins & Advanced Functions",
    "nosql": "NoSQL & Modern Storage",
    "internals": "Performance, Indexing & Internals",
    "challenges": "Real-World Query Challenges",
}


@router.get("", response_class=HTMLResponse)
def database_page(
    request: Request,
    track: Optional[str] = "all",
    category: Optional[str] = None,
    status_filter: Optional[str] = "all",
    difficulty_filter: Optional[str] = "all",
    search: Optional[str] = None,
    db: Session = Depends(get_db),
):
    user = db.query(UserProfile).first()

    all_concepts = db.query(DatabaseConcept).order_by(DatabaseConcept.order_index).all()
    all_items = db.query(DatabaseItem).order_by(DatabaseItem.order_index).all()
    all_challenges = db.query(DatabaseChallenge).order_by(DatabaseChallenge.order_index).all()

    # Track-wise concept mapping
    sql_concept_ids = [c.id for c in all_concepts if (c.track or "").upper() == "SQL"]
    joins_concept_ids = [c.id for c in all_concepts if (c.track or "").upper() == "JOINS_FUNCTIONS"]
    nosql_concept_ids = [c.id for c in all_concepts if (c.track or "").upper() == "NOSQL"]
    internals_concept_ids = [c.id for c in all_concepts if (c.track or "").upper() == "INTERNALS"]

    # Track-wise items
    sql_items = [it for it in all_items if it.concept_id in sql_concept_ids]
    joins_items = [it for it in all_items if it.concept_id in joins_concept_ids]
    nosql_items = [it for it in all_items if it.concept_id in nosql_concept_ids]
    internals_items = [it for it in all_items if it.concept_id in internals_concept_ids]

    # Calculate SQL track stats
    sql_done = sum(1 for it in sql_items if it.status == "Done")
    sql_in_progress = sum(1 for it in sql_items if it.status == "In Progress")
    sql_pct = round((sql_done / len(sql_items) * 100) if sql_items else 0)

    # Calculate Joins/Functions track stats
    joins_done = sum(1 for it in joins_items if it.status == "Done")
    joins_in_progress = sum(1 for it in joins_items if it.status == "In Progress")
    joins_pct = round((joins_done / len(joins_items) * 100) if joins_items else 0)

    # Calculate NoSQL track stats
    nosql_done = sum(1 for it in nosql_items if it.status == "Done")
    nosql_in_progress = sum(1 for it in nosql_items if it.status == "In Progress")
    nosql_pct = round((nosql_done / len(nosql_items) * 100) if nosql_items else 0)

    # Calculate Internals track stats
    internals_done = sum(1 for it in internals_items if it.status == "Done")
    internals_in_progress = sum(1 for it in internals_items if it.status == "In Progress")
    internals_pct = round((internals_done / len(internals_items) * 100) if internals_items else 0)

    # Calculate Challenges stats
    challenges_done = sum(1 for ch in all_challenges if ch.status == "Done")
    challenges_in_progress = sum(1 for ch in all_challenges if ch.status == "In Progress")
    challenges_pct = round((challenges_done / len(all_challenges) * 100) if all_challenges else 0)

    # Overall Metrics
    total_items = len(all_items)
    total_items_done = sum(1 for it in all_items if it.status == "Done")
    total_items_in_progress = sum(1 for it in all_items if it.status == "In Progress")
    reading_done_count = sum(1 for it in all_items if it.reading_done)
    practical_done_count = sum(1 for it in all_items if it.practical_done)

    overall_total = total_items + len(all_challenges)
    overall_done = total_items_done + challenges_done
    overall_pct = round((overall_done / overall_total * 100) if overall_total > 0 else 0)

    # --- Filtering Logic ---
    selected_track = (track or "all").strip().lower()
    concepts_query = db.query(DatabaseConcept)
    challenges_query = db.query(DatabaseChallenge)

    if selected_track != "all" and selected_track != "challenges":
        concepts_query = concepts_query.filter(func.lower(DatabaseConcept.track) == selected_track)

    if category and category.strip() and category.strip() != "all":
        concepts_query = concepts_query.filter(DatabaseConcept.category == category.strip())
        challenges_query = challenges_query.filter(DatabaseChallenge.category == category.strip())

    if difficulty_filter and difficulty_filter.strip() and difficulty_filter.strip() != "all":
        concepts_query = concepts_query.filter(DatabaseConcept.difficulty == difficulty_filter.strip())
        challenges_query = challenges_query.filter(DatabaseChallenge.difficulty == difficulty_filter.strip())

    if search and search.strip():
        search_term = search.strip()
        matching_concept_ids = db.query(DatabaseItem.concept_id).filter(
            or_(
                DatabaseItem.title.ilike(f"%{search_term}%"),
                DatabaseItem.syntax_example.ilike(f"%{search_term}%"),
                DatabaseItem.notes.ilike(f"%{search_term}%"),
            )
        ).subquery()

        concepts_query = concepts_query.filter(
            or_(
                DatabaseConcept.title.ilike(f"%{search_term}%"),
                DatabaseConcept.category.ilike(f"%{search_term}%"),
                DatabaseConcept.description.ilike(f"%{search_term}%"),
                DatabaseConcept.id.in_(matching_concept_ids)
            )
        )

        challenges_query = challenges_query.filter(
            or_(
                DatabaseChallenge.title.ilike(f"%{search_term}%"),
                DatabaseChallenge.category.ilike(f"%{search_term}%"),
                DatabaseChallenge.scenario.ilike(f"%{search_term}%"),
                DatabaseChallenge.solution_query.ilike(f"%{search_term}%"),
                DatabaseChallenge.explanation.ilike(f"%{search_term}%"),
            )
        )

    filtered_concepts = concepts_query.order_by(DatabaseConcept.order_index).all()
    filtered_challenges = challenges_query.order_by(DatabaseChallenge.order_index).all()

    # If status filter is applied, filter items within concepts
    filtered_concepts_with_items = []
    for c in filtered_concepts:
        items = c.items
        if status_filter and status_filter.strip() != "all":
            items = [it for it in items if it.status == status_filter.strip()]
        if items or (status_filter == "all"):
            # Attach filtered items for view
            filtered_concepts_with_items.append((c, items))

    # Group concepts by track and category for structured layout
    by_track_and_cat = {}
    for c, items in filtered_concepts_with_items:
        t = (c.track or "SQL").upper()
        by_track_and_cat.setdefault(t, {}).setdefault(c.category, []).append((c, items))

    return templates.TemplateResponse("database.html", {
        "request": request,
        "user": user,
        "today": date.today(),
        "selected_track": selected_track,
        "selected_category": category or "all",
        "selected_status": status_filter or "all",
        "selected_difficulty": difficulty_filter or "all",
        "selected_search": search or "",
        "track_names": TRACK_NAMES,
        "statuses": STATUSES,
        "depth_labels": DEPTH_LABELS,

        # Grouped Data
        "concepts_with_items": filtered_concepts_with_items,
        "by_track_and_cat": by_track_and_cat,
        "challenges": filtered_challenges,

        # Track Stats
        "sql_total": len(sql_items),
        "sql_done": sql_done,
        "sql_in_progress": sql_in_progress,
        "sql_pct": sql_pct,

        "joins_total": len(joins_items),
        "joins_done": joins_done,
        "joins_in_progress": joins_in_progress,
        "joins_pct": joins_pct,

        "nosql_total": len(nosql_items),
        "nosql_done": nosql_done,
        "nosql_in_progress": nosql_in_progress,
        "nosql_pct": nosql_pct,

        "internals_total": len(internals_items),
        "internals_done": internals_done,
        "internals_in_progress": internals_in_progress,
        "internals_pct": internals_pct,

        "challenges_total": len(all_challenges),
        "challenges_done": challenges_done,
        "challenges_in_progress": challenges_in_progress,
        "challenges_pct": challenges_pct,

        # Overall Stats
        "total_items": total_items,
        "total_items_done": total_items_done,
        "total_items_in_progress": total_items_in_progress,
        "reading_done_count": reading_done_count,
        "practical_done_count": practical_done_count,
        "overall_total": overall_total,
        "overall_done": overall_done,
        "overall_pct": overall_pct,

        "active_page": "database",
    })


# ══════════════════════════════════════════════════════════════════════════
# Concept CRUD
# ══════════════════════════════════════════════════════════════════════════

@router.post("/concept/add")
def add_concept(
    track: str = Form("SQL"),
    category: str = Form(...),
    title: str = Form(...),
    difficulty: str = Form("Medium"),
    description: Optional[str] = Form(None),
    db: Session = Depends(get_db),
):
    max_order = db.query(func.max(DatabaseConcept.order_index)).scalar() or 0
    concept = DatabaseConcept(
        track=track.upper(),
        category=category.strip(),
        title=title.strip(),
        difficulty=difficulty,
        description=description.strip() if description else None,
        order_index=max_order + 1,
    )
    db.add(concept)
    db.commit()
    return RedirectResponse(f"/database?track={track.lower()}", status_code=303)


@router.post("/concept/{concept_id}/delete")
def delete_concept(concept_id: int, db: Session = Depends(get_db)):
    concept = db.query(DatabaseConcept).filter(DatabaseConcept.id == concept_id).first()
    if not concept:
        raise HTTPException(status_code=404, detail="Concept not found")
    track = concept.track.lower()
    db.delete(concept)
    db.commit()
    return RedirectResponse(f"/database?track={track}", status_code=303)


# ══════════════════════════════════════════════════════════════════════════
# Item CRUD & Quick Actions
# ══════════════════════════════════════════════════════════════════════════

@router.post("/item/add")
def add_item(
    concept_id: int = Form(...),
    title: str = Form(...),
    syntax_example: Optional[str] = Form(None),
    notes: Optional[str] = Form(None),
    depth: int = Form(1),
    db: Session = Depends(get_db),
):
    concept = db.query(DatabaseConcept).filter(DatabaseConcept.id == concept_id).first()
    if not concept:
        raise HTTPException(status_code=404, detail="Concept not found")

    max_order = db.query(func.max(DatabaseItem.order_index)).filter(DatabaseItem.concept_id == concept_id).scalar() or 0
    item = DatabaseItem(
        concept_id=concept_id,
        title=title.strip(),
        syntax_example=syntax_example.strip() if syntax_example else None,
        notes=notes.strip() if notes else None,
        depth=depth,
        order_index=max_order + 1,
    )
    db.add(item)
    db.commit()
    return RedirectResponse(f"/database?track={concept.track.lower()}", status_code=303)


@router.post("/item/{item_id}/update-status")
def update_item_status(
    item_id: int,
    status: str = Form(...),
    db: Session = Depends(get_db),
):
    item = db.query(DatabaseItem).filter(DatabaseItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item.status = status
    if status == "Done":
        item.reading_done = True
        item.practical_done = True
    db.commit()
    return JSONResponse({"success": True, "status": item.status})


@router.post("/item/{item_id}/toggle-reading")
def toggle_item_reading(item_id: int, db: Session = Depends(get_db)):
    item = db.query(DatabaseItem).filter(DatabaseItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item.reading_done = not item.reading_done
    if item.reading_done and item.practical_done:
        item.status = "Done"
    elif item.reading_done or item.practical_done:
        if item.status == "Not Started":
            item.status = "In Progress"
    db.commit()
    return JSONResponse({"success": True, "reading_done": item.reading_done, "status": item.status})


@router.post("/item/{item_id}/toggle-practical")
def toggle_item_practical(item_id: int, db: Session = Depends(get_db)):
    item = db.query(DatabaseItem).filter(DatabaseItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item.practical_done = not item.practical_done
    if item.reading_done and item.practical_done:
        item.status = "Done"
    elif item.reading_done or item.practical_done:
        if item.status == "Not Started":
            item.status = "In Progress"
    db.commit()
    return JSONResponse({"success": True, "practical_done": item.practical_done, "status": item.status})


@router.post("/item/{item_id}/edit-notes")
def edit_item_notes(
    item_id: int,
    notes: Optional[str] = Form(""),
    syntax_example: Optional[str] = Form(""),
    depth: int = Form(1),
    sources: Optional[str] = Form(""),
    db: Session = Depends(get_db),
):
    item = db.query(DatabaseItem).filter(DatabaseItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item.notes = notes or ""
    item.syntax_example = syntax_example or ""
    item.depth = depth
    item.sources = sources or ""
    db.commit()
    return JSONResponse({"success": True})


@router.post("/item/{item_id}/delete")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(DatabaseItem).filter(DatabaseItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    concept = item.concept
    track = concept.track.lower() if concept else "all"
    db.delete(item)
    db.commit()
    return RedirectResponse(f"/database?track={track}", status_code=303)


# ══════════════════════════════════════════════════════════════════════════
# Challenges CRUD
# ══════════════════════════════════════════════════════════════════════════

@router.post("/challenge/add")
def add_challenge(
    track: str = Form("SQL"),
    title: str = Form(...),
    category: str = Form(...),
    difficulty: str = Form("Medium"),
    scenario: str = Form(...),
    schema_definition: Optional[str] = Form(""),
    solution_query: Optional[str] = Form(""),
    explanation: Optional[str] = Form(""),
    db: Session = Depends(get_db),
):
    max_order = db.query(func.max(DatabaseChallenge.order_index)).scalar() or 0
    challenge = DatabaseChallenge(
        track=track.upper(),
        title=title.strip(),
        category=category.strip(),
        difficulty=difficulty,
        scenario=scenario.strip(),
        schema_definition=schema_definition.strip() if schema_definition else None,
        solution_query=solution_query.strip() if solution_query else None,
        explanation=explanation.strip() if explanation else None,
        order_index=max_order + 1,
    )
    db.add(challenge)
    db.commit()
    return RedirectResponse("/database?track=challenges", status_code=303)


@router.post("/challenge/{challenge_id}/update-status")
def update_challenge_status(
    challenge_id: int,
    status: str = Form(...),
    db: Session = Depends(get_db),
):
    ch = db.query(DatabaseChallenge).filter(DatabaseChallenge.id == challenge_id).first()
    if not ch:
        raise HTTPException(status_code=404, detail="Challenge not found")
    ch.status = status
    db.commit()
    return JSONResponse({"success": True, "status": ch.status})


@router.post("/challenge/{challenge_id}/edit-notes")
def edit_challenge_notes(
    challenge_id: int,
    notes: Optional[str] = Form(""),
    solution_query: Optional[str] = Form(""),
    db: Session = Depends(get_db),
):
    ch = db.query(DatabaseChallenge).filter(DatabaseChallenge.id == challenge_id).first()
    if not ch:
        raise HTTPException(status_code=404, detail="Challenge not found")
    ch.notes = notes or ""
    if solution_query:
        ch.solution_query = solution_query
    db.commit()
    return JSONResponse({"success": True})


@router.post("/challenge/{challenge_id}/delete")
def delete_challenge(challenge_id: int, db: Session = Depends(get_db)):
    ch = db.query(DatabaseChallenge).filter(DatabaseChallenge.id == challenge_id).first()
    if not ch:
        raise HTTPException(status_code=404, detail="Challenge not found")
    db.delete(ch)
    db.commit()
    return RedirectResponse("/database?track=challenges", status_code=303)
