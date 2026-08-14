from datetime import date
from typing import Optional
from fastapi import APIRouter, Depends, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.personal_hub import PersonalHubItem
from app.models.user import UserProfile

router = APIRouter(prefix="/personal-hub", tags=["personal-hub"])
templates = Jinja2Templates(directory="app/templates")

CATEGORIES = ["Reminder", "Note", "Need to Ask", "Visa & Immigration"]


@router.get("", response_class=HTMLResponse)
def hub_page(
    request: Request,
    category: Optional[str] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db),
):
    user = db.query(UserProfile).first()
    query = db.query(PersonalHubItem)

    if category and category.strip():
        query = query.filter(PersonalHubItem.category == category)
    if search and search.strip():
        query = query.filter(
            PersonalHubItem.title.ilike(f"%{search}%") |
            PersonalHubItem.content.ilike(f"%{search}%") |
            PersonalHubItem.source.ilike(f"%{search}%")
        )

    items = query.order_by(
        PersonalHubItem.status.desc(),  # Pending first (assuming sorting)
        PersonalHubItem.due_date.asc().nullslast(),
        PersonalHubItem.created_at.desc()
    ).all()

    # Sort so Pending is before Completed
    pending_items = [i for i in items if i.status == "Pending"]
    completed_items = [i for i in items if i.status == "Completed"]
    sorted_items = pending_items + completed_items

    # Stats (always calculated on all active entries)
    total_reminders = db.query(PersonalHubItem).filter(
        PersonalHubItem.category == "Reminder",
        PersonalHubItem.status == "Pending"
    ).count()
    total_notes = db.query(PersonalHubItem).filter(
        PersonalHubItem.category == "Note"
    ).count()
    total_questions = db.query(PersonalHubItem).filter(
        PersonalHubItem.category == "Need to Ask",
        PersonalHubItem.status == "Pending"
    ).count()
    total_visa = db.query(PersonalHubItem).filter(
        PersonalHubItem.category == "Visa & Immigration"
    ).count()

    return templates.TemplateResponse("personal_hub.html", {
        "request": request,
        "user": user,
        "today": date.today(),
        "items": sorted_items,
        "categories": CATEGORIES,
        "total_reminders": total_reminders,
        "total_notes": total_notes,
        "total_questions": total_questions,
        "total_visa": total_visa,
        "selected_category": category or "",
        "selected_search": search or "",
        "active_page": "personal_hub",
    })


@router.post("/add")
def add_item(
    title: str = Form(...),
    category: str = Form(...),
    content: str = Form(""),
    source: str = Form(""),
    due_date: Optional[str] = Form(None),
    status: str = Form("Pending"),
    db: Session = Depends(get_db),
):
    parsed_due_date = None
    if due_date and due_date.strip():
        parsed_due_date = date.fromisoformat(due_date)

    item = PersonalHubItem(
        title=title,
        category=category,
        content=content,
        source=source,
        due_date=parsed_due_date,
        status=status,
    )
    db.add(item)
    db.commit()
    return RedirectResponse(url="/personal-hub", status_code=303)


@router.post("/update/{item_id}")
def update_item(
    item_id: int,
    title: str = Form(...),
    category: str = Form(...),
    content: str = Form(""),
    source: str = Form(""),
    due_date: Optional[str] = Form(None),
    status: str = Form(...),
    db: Session = Depends(get_db),
):
    item = db.query(PersonalHubItem).filter(PersonalHubItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    parsed_due_date = None
    if due_date and due_date.strip():
        parsed_due_date = date.fromisoformat(due_date)

    item.title = title
    item.category = category
    item.content = content
    item.source = source
    item.due_date = parsed_due_date
    item.status = status

    db.commit()
    return RedirectResponse(url="/personal-hub", status_code=303)


@router.post("/toggle/{item_id}")
def toggle_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(PersonalHubItem).filter(PersonalHubItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item.status = "Completed" if item.status == "Pending" else "Pending"
    db.commit()
    return RedirectResponse(url="/personal-hub", status_code=303)


@router.post("/delete/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(PersonalHubItem).filter(PersonalHubItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()
    return RedirectResponse(url="/personal-hub", status_code=303)
