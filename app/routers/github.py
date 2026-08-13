from datetime import date
from fastapi import APIRouter, Depends, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.github import GithubProject, GithubTask
from app.models.user import UserProfile

router = APIRouter(prefix="/github", tags=["github"])
templates = Jinja2Templates(directory="app/templates")

STATUSES = ["Not Started", "In Progress", "Done"]


@router.get("", response_class=HTMLResponse)
def github_page(request: Request, db: Session = Depends(get_db)):
    user = db.query(UserProfile).first()
    projects = db.query(GithubProject).order_by(GithubProject.order_index).all()

    projects_data = []
    for p in projects:
        total = len(p.tasks)
        done = sum(1 for t in p.tasks if t.done)
        pct = round((done / total * 100) if total else 0)
        by_cat = {}
        for t in p.tasks:
            by_cat.setdefault(t.category, []).append(t)
        projects_data.append({
            "project": p,
            "total": total,
            "done": done,
            "pct": pct,
            "by_cat": by_cat,
        })

    return templates.TemplateResponse("github.html", {
        "request": request,
        "user": user,
        "today": date.today(),
        "projects_data": projects_data,
        "statuses": STATUSES,
        "active_page": "github",
    })


@router.post("/task/toggle/{task_id}")
def toggle_task(task_id: int, db: Session = Depends(get_db)):
    t = db.query(GithubTask).filter(GithubTask.id == task_id).first()
    if not t:
        raise HTTPException(status_code=404)
    t.done = not t.done
    db.commit()
    return RedirectResponse(url="/github", status_code=303)


@router.post("/project/update/{project_id}")
def update_project(
    project_id: int,
    status: str = Form(...),
    github_url: str = Form(""),
    demo_url: str = Form(""),
    db: Session = Depends(get_db),
):
    p = db.query(GithubProject).filter(GithubProject.id == project_id).first()
    if not p:
        raise HTTPException(status_code=404)
    p.status = status
    p.github_url = github_url
    p.demo_url = demo_url
    db.commit()
    return RedirectResponse(url="/github", status_code=303)
