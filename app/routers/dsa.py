from datetime import date
from typing import Optional, List, Dict, Any
from fastapi import APIRouter, Depends, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import or_

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
    category: Optional[str] = None,
    difficulty: Optional[str] = None,
    status: Optional[str] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db),
):
    user = db.query(UserProfile).first()
    topics = db.query(DSATopic).order_by(DSATopic.order_index).all()
    topic_names = [t.name for t in topics]

    # Normalize empty strings to None
    category = category.strip() if (category and category.strip()) else None
    difficulty = difficulty.strip() if (difficulty and difficulty.strip()) else None
    status = status.strip() if (status and status.strip()) else None
    search_term = search.strip() if (search and search.strip()) else None

    # Global Stats across all problems
    all_problems = db.query(DSAProblem).all()
    total = len(all_problems)
    solved = sum(1 for p in all_problems if p.status == "Solved")
    easy_solved = sum(1 for p in all_problems if p.status == "Solved" and p.difficulty == "Easy")
    medium_solved = sum(1 for p in all_problems if p.status == "Solved" and p.difficulty == "Medium")
    hard_solved = sum(1 for p in all_problems if p.status == "Solved" and p.difficulty == "Hard")

    easy_total = sum(1 for p in all_problems if p.difficulty == "Easy")
    medium_total = sum(1 for p in all_problems if p.difficulty == "Medium")
    hard_total = sum(1 for p in all_problems if p.difficulty == "Hard")

    # Distinct categories in DB plus standard topics
    db_categories = [c[0] for c in db.query(DSAProblem.category).distinct().all() if c[0]]
    all_categories_set = set(topic_names) | set(db_categories)
    
    # Maintain standard order for known topics, followed by any custom categories
    ordered_categories = [t for t in topic_names if t in all_categories_set]
    for c in sorted(all_categories_set):
        if c not in ordered_categories:
            ordered_categories.append(c)

    # Build query for filtered problems
    query = db.query(DSAProblem)
    if category:
        query = query.filter(DSAProblem.category == category)
    if difficulty:
        query = query.filter(DSAProblem.difficulty == difficulty)
    if status:
        query = query.filter(DSAProblem.status == status)
    if search_term:
        query = query.filter(
            or_(
                DSAProblem.title.ilike(f"%{search_term}%"),
                DSAProblem.alternate_title.ilike(f"%{search_term}%"),
                DSAProblem.category.ilike(f"%{search_term}%"),
                DSAProblem.pattern.ilike(f"%{search_term}%"),
                DSAProblem.mistake.ilike(f"%{search_term}%")
            )
        )
    filtered_problems = query.order_by(DSAProblem.id.desc()).all()

    # Pre-calculate category-level statistics from all problems (for merged Topic Progress)
    category_meta: Dict[str, Dict[str, Any]] = {}
    for cat_name in ordered_categories:
        cat_probs = [p for p in all_problems if p.category == cat_name]
        cat_total = len(cat_probs)
        cat_solved = sum(1 for p in cat_probs if p.status == "Solved")
        cat_pct = round((cat_solved / cat_total * 100) if cat_total > 0 else 0)
        
        category_meta[cat_name] = {
            "name": cat_name,
            "total": cat_total,
            "solved": cat_solved,
            "pct": cat_pct,
            "easy_count": sum(1 for p in cat_probs if p.difficulty == "Easy"),
            "easy_solved": sum(1 for p in cat_probs if p.difficulty == "Easy" and p.status == "Solved"),
            "medium_count": sum(1 for p in cat_probs if p.difficulty == "Medium"),
            "medium_solved": sum(1 for p in cat_probs if p.difficulty == "Medium" and p.status == "Solved"),
            "hard_count": sum(1 for p in cat_probs if p.difficulty == "Hard"),
            "hard_solved": sum(1 for p in cat_probs if p.difficulty == "Hard" and p.status == "Solved"),
        }

    # Build 3-Layer Hierarchical Data: Category -> Difficulty -> Problems
    # Group filtered problems
    grouped_data: Dict[str, Dict[str, List[DSAProblem]]] = {}
    for p in filtered_problems:
        cat = p.category or "Arrays and Strings"
        diff = p.difficulty if p.difficulty in DIFFICULTIES else "Medium"
        if cat not in grouped_data:
            grouped_data[cat] = {"Easy": [], "Medium": [], "Hard": []}
        grouped_data[cat][diff].append(p)

    # Prepare structured list for UI
    categories_view = []
    has_active_filters = bool(category or difficulty or status or search_term)

    # If filters are active, show only categories that have matching problems.
    # Otherwise, show all categories that either have problems or belong to the roadmap.
    target_cats = list(grouped_data.keys()) if has_active_filters else ordered_categories

    for cat_name in target_cats:
        meta = category_meta.get(cat_name, {
            "name": cat_name,
            "total": 0,
            "solved": 0,
            "pct": 0,
            "easy_count": 0,
            "easy_solved": 0,
            "medium_count": 0,
            "medium_solved": 0,
            "hard_count": 0,
            "hard_solved": 0,
        })
        diff_map = grouped_data.get(cat_name, {"Easy": [], "Medium": [], "Hard": []})
        filtered_cat_total = sum(len(plist) for plist in diff_map.values())
        
        # When no filters are active, we can show categories with 0 problems or with problems
        # If filters are active and filtered_cat_total == 0, skip
        if has_active_filters and filtered_cat_total == 0:
            continue

        categories_view.append({
            "name": cat_name,
            "meta": meta,
            "filtered_total": filtered_cat_total,
            "difficulties": [
                {
                    "difficulty": "Easy",
                    "problems": diff_map.get("Easy", []),
                    "count": len(diff_map.get("Easy", [])),
                    "solved": sum(1 for p in diff_map.get("Easy", []) if p.status == "Solved"),
                },
                {
                    "difficulty": "Medium",
                    "problems": diff_map.get("Medium", []),
                    "count": len(diff_map.get("Medium", [])),
                    "solved": sum(1 for p in diff_map.get("Medium", []) if p.status == "Solved"),
                },
                {
                    "difficulty": "Hard",
                    "problems": diff_map.get("Hard", []),
                    "count": len(diff_map.get("Hard", [])),
                    "solved": sum(1 for p in diff_map.get("Hard", []) if p.status == "Solved"),
                },
            ]
        })

    return templates.TemplateResponse("dsa.html", {
        "request": request,
        "user": user,
        "today": date.today(),
        "topics": topics,
        "all_categories": ordered_categories,
        "categories_view": categories_view,
        "filtered_problems_count": len(filtered_problems),
        "difficulties": DIFFICULTIES,
        "statuses": STATUSES,
        "selected_category": category,
        "selected_difficulty": difficulty,
        "selected_status": status,
        "selected_search": search_term or "",
        "total": total,
        "solved": solved,
        "easy_solved": easy_solved,
        "medium_solved": medium_solved,
        "hard_solved": hard_solved,
        "easy_total": easy_total,
        "medium_total": medium_total,
        "hard_total": hard_total,
        "active_page": "dsa",
    })


def sanitize_str(val: Optional[str]) -> str:
    if not val:
        return ""
    val_clean = val.strip()
    if val_clean.lower() in ("none", "null"):
        return ""
    return val_clean


@router.post("/add")
def add_problem(
    category: str = Form("Arrays and Strings"),
    title: str = Form(...),
    difficulty: str = Form("Medium"),
    status: str = Form("Not Started"),
    pattern: str = Form(""),
    mistake: str = Form(""),
    time_complexity: str = Form(""),
    space_complexity: str = Form(""),
    solution_snippet: str = Form(""),
    confidence: int = Form(3),
    problem_url: str = Form(""),
    alternate_title: str = Form(""),
    alternate_url: str = Form(""),
    topic_ids: List[int] = Form(default=[]),
    db: Session = Depends(get_db),
):
    category = sanitize_str(category) or "Arrays and Strings"
    title = sanitize_str(title)
    problem_url = sanitize_str(problem_url)
    alternate_title = sanitize_str(alternate_title)
    alternate_url = sanitize_str(alternate_url)
    pattern = sanitize_str(pattern)
    mistake = sanitize_str(mistake)
    time_complexity = sanitize_str(time_complexity)
    space_complexity = sanitize_str(space_complexity)
    solution_snippet = sanitize_str(solution_snippet)

    if title.startswith("http://") or title.startswith("https://"):
        if not problem_url:
            problem_url = title
        from app.models.dsa import clean_title_from_url
        title = clean_title_from_url(title)

    if alternate_title.startswith("http://") or alternate_title.startswith("https://"):
        if not alternate_url:
            alternate_url = alternate_title
        from app.models.dsa import clean_title_from_url
        alternate_title = clean_title_from_url(alternate_title)
    elif alternate_url and not alternate_title:
        from app.models.dsa import clean_title_from_url
        alternate_title = clean_title_from_url(alternate_url)

    topics = []
    if topic_ids:
        topics = db.query(DSATopic).filter(DSATopic.id.in_(topic_ids)).all()
    else:
        # Auto-link matching DSATopic by category name if present
        matching_topic = db.query(DSATopic).filter(DSATopic.name == category).first()
        if matching_topic:
            topics = [matching_topic]

    p = DSAProblem(
        category=category,
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
        alternate_title=alternate_title,
        alternate_url=alternate_url,
        solved_date=date.today() if status == "Solved" else None,
        topics=topics,
    )
    db.add(p)
    db.commit()
    return RedirectResponse(url="/dsa", status_code=303)


@router.post("/update/{problem_id}")
def update_problem(
    problem_id: int,
    category: str = Form("Arrays and Strings"),
    title: str = Form(...),
    difficulty: str = Form("Medium"),
    problem_url: str = Form(""),
    alternate_title: str = Form(""),
    alternate_url: str = Form(""),
    status: str = Form(...),
    pattern: str = Form(""),
    mistake: str = Form(""),
    time_complexity: str = Form(""),
    space_complexity: str = Form(""),
    solution_snippet: str = Form(""),
    confidence: int = Form(3),
    topic_ids: List[int] = Form(default=[]),
    db: Session = Depends(get_db),
):
    p = db.query(DSAProblem).filter(DSAProblem.id == problem_id).first()
    if not p:
        raise HTTPException(status_code=404)

    category = sanitize_str(category) or "Arrays and Strings"
    title = sanitize_str(title)
    problem_url = sanitize_str(problem_url)
    alternate_title = sanitize_str(alternate_title)
    alternate_url = sanitize_str(alternate_url)
    pattern = sanitize_str(pattern)
    mistake = sanitize_str(mistake)
    time_complexity = sanitize_str(time_complexity)
    space_complexity = sanitize_str(space_complexity)
    solution_snippet = sanitize_str(solution_snippet)

    if title.startswith("http://") or title.startswith("https://"):
        if not problem_url:
            problem_url = title
        from app.models.dsa import clean_title_from_url
        title = clean_title_from_url(title)

    if alternate_title.startswith("http://") or alternate_title.startswith("https://"):
        if not alternate_url:
            alternate_url = alternate_title
        from app.models.dsa import clean_title_from_url
        alternate_title = clean_title_from_url(alternate_title)
    elif alternate_url and not alternate_title:
        from app.models.dsa import clean_title_from_url
        alternate_title = clean_title_from_url(alternate_url)
    
    topics = db.query(DSATopic).filter(DSATopic.id.in_(topic_ids)).all() if topic_ids else []
    p.topics = topics

    p.category = category
    p.title = title
    p.difficulty = difficulty
    p.problem_url = problem_url
    p.alternate_title = alternate_title
    p.alternate_url = alternate_url
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
