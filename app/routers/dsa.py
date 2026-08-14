from datetime import date
from typing import Optional, List
from fastapi import APIRouter, Depends, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.dsa import DSATopic, DSAProblem
from app.models.user import UserProfile

router = APIRouter(prefix="/dsa", tags=["dsa"])
templates = Jinja2Templates(directory="app/templates")

DIFFICULTIES = ["Easy", "Medium", "Hard"]
STATUSES = ["Not Started", "In Progress", "Solved", "Needs Review"]


@router.get("", response_class=HTMLResponse)
def dsa_page(
    request: Request,
    topic_id: Optional[str] = None,
    difficulty: Optional[str] = None,
    status: Optional[str] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db),
):
    user = db.query(UserProfile).first()
    topics = db.query(DSATopic).order_by(DSATopic.order_index).all()

    # Safely convert topic_id to int if present and not empty
    parsed_topic_id = None
    if topic_id and topic_id.strip():
        try:
            parsed_topic_id = int(topic_id)
        except ValueError:
            pass

    # Normalize empty strings to None
    difficulty = difficulty if (difficulty and difficulty.strip()) else None
    status = status if (status and status.strip()) else None

    query = db.query(DSAProblem)
    if parsed_topic_id:
        query = query.filter(DSAProblem.topics.any(id=parsed_topic_id))
    if difficulty:
        query = query.filter(DSAProblem.difficulty == difficulty)
    if status:
        query = query.filter(DSAProblem.status == status)
    if search and search.strip():
        query = query.filter(
            DSAProblem.title.ilike(f"%{search.strip()}%") |
            DSAProblem.pattern.ilike(f"%{search.strip()}%") |
            DSAProblem.mistake.ilike(f"%{search.strip()}%")
        )
    problems = query.order_by(DSAProblem.id.desc()).all()

    # Stats
    total = db.query(DSAProblem).count()
    solved = db.query(DSAProblem).filter(DSAProblem.status == "Solved").count()
    easy_solved = db.query(DSAProblem).filter(DSAProblem.status == "Solved", DSAProblem.difficulty == "Easy").count()
    medium_solved = db.query(DSAProblem).filter(DSAProblem.status == "Solved", DSAProblem.difficulty == "Medium").count()
    hard_solved = db.query(DSAProblem).filter(DSAProblem.status == "Solved", DSAProblem.difficulty == "Hard").count()

    topic_stats = []
    for t in topics:
        t_solved = sum(1 for p in t.problems if p.status == "Solved")
        t_total = len(t.problems)
        topic_stats.append({
            "id": t.id,
            "name": t.name,
            "total": t_total,
            "solved": t_solved,
            "pct": round((t_solved / t_total * 100) if t_total else 0),
        })

    return templates.TemplateResponse("dsa.html", {
        "request": request,
        "user": user,
        "today": date.today(),
        "topics": topics,
        "topic_stats": topic_stats,
        "problems": problems,
        "difficulties": DIFFICULTIES,
        "statuses": STATUSES,
        "selected_topic_id": parsed_topic_id,
        "selected_difficulty": difficulty,
        "selected_status": status,
        "selected_search": search or "",
        "total": total,
        "solved": solved,
        "easy_solved": easy_solved,
        "medium_solved": medium_solved,
        "hard_solved": hard_solved,
        "active_page": "dsa",
    })


@router.post("/add")
def add_problem(
    topic_ids: List[int] = Form(...),
    title: str = Form(...),
    difficulty: str = Form(...),
    status: str = Form("Not Started"),
    pattern: str = Form(""),
    mistake: str = Form(""),
    time_complexity: str = Form(""),
    space_complexity: str = Form(""),
    solution_snippet: str = Form(""),
    confidence: int = Form(3),
    problem_url: str = Form(""),
    db: Session = Depends(get_db),
):
    if title.startswith("http://") or title.startswith("https://"):
        if not problem_url:
            problem_url = title
        from app.models.dsa import clean_title_from_url
        title = clean_title_from_url(title)

    topics = db.query(DSATopic).filter(DSATopic.id.in_(topic_ids)).all()

    p = DSAProblem(
        title=title,
        difficulty=difficulty,
        status=status,
        pattern=pattern,
        mistake=mistake,
        time_complexity=time_complexity,
        space_complexity=space_complexity,
        solution_snippet=solution_snippet,
        confidence=confidence,
        problem_url=problem_url,
        solved_date=date.today() if status == "Solved" else None,
        topics=topics,
    )
    db.add(p)
    db.commit()
    return RedirectResponse(url="/dsa", status_code=303)


@router.post("/update/{problem_id}")
def update_problem(
    problem_id: int,
    status: str = Form(...),
    pattern: str = Form(""),
    mistake: str = Form(""),
    time_complexity: str = Form(""),
    space_complexity: str = Form(""),
    solution_snippet: str = Form(""),
    confidence: int = Form(3),
    topic_ids: List[int] = Form(...),
    db: Session = Depends(get_db),
):
    p = db.query(DSAProblem).filter(DSAProblem.id == problem_id).first()
    if not p:
        raise HTTPException(status_code=404)
    
    topics = db.query(DSATopic).filter(DSATopic.id.in_(topic_ids)).all()
    p.topics = topics

    p.status = status
    p.pattern = pattern
    p.mistake = mistake
    p.time_complexity = time_complexity
    p.space_complexity = space_complexity
    p.solution_snippet = solution_snippet
    p.confidence = confidence
    if status == "Solved" and not p.solved_date:
        p.solved_date = date.today()
    db.commit()
    return RedirectResponse(url="/dsa", status_code=303)


@router.post("/delete/{problem_id}")
def delete_problem(problem_id: int, db: Session = Depends(get_db)):
    p = db.query(DSAProblem).filter(DSAProblem.id == problem_id).first()
    if not p:
        raise HTTPException(status_code=404)
    db.delete(p)
    db.commit()
    return RedirectResponse(url="/dsa", status_code=303)
