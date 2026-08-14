from datetime import date
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import UserProfile
from app.services.gamification import get_gamification_state

router = APIRouter(prefix="/achievements", tags=["achievements"])
templates = Jinja2Templates(directory="app/templates")


@router.get("", response_class=HTMLResponse)
def achievements_page(request: Request, db: Session = Depends(get_db)):
    user = db.query(UserProfile).first()
    gamification = get_gamification_state(db)
    
    return templates.TemplateResponse("achievements.html", {
        "request": request,
        "user": user,
        "today": date.today(),
        "gamification": gamification,
        "active_page": "achievements",
    })
