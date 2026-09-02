from datetime import date
from typing import Optional, List, Dict, Any
from fastapi import APIRouter, Depends, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.database import get_db
from app.models.dsa import DSATopic, DSAProblem, DSACompany
from app.models.user import UserProfile
from app.services.gamification import get_gamification_state

router = APIRouter(prefix="/dsa", tags=["dsa"])
templates = Jinja2Templates(directory="app/templates")

DIFFICULTIES = ["Easy", "Medium", "Hard"]
STATUSES = ["Not Started", "In Progress", "Solved", "Needs Review"]

# Regional Market Targets & Strategy Profiles
REGION_CONFIGS = {
    "eu": {
        "id": "eu",
        "name": "EU Standard",
        "flag": "🇪🇺",
        "subtitle": "Germany 🇩🇪 & Netherlands 🇳🇱 Tier-1 Tech Priority",
        "badge_text": "🇪🇺 EU Standard · 🇩🇪 🇳🇱 Priority",
        "target_total": 200,
        "target_easy": 40,
        "target_medium": 120,
        "target_hard": 40,
        "primary_focus": "Medium-Heavy Focus (60% weight on clean, modular LeetCode Mediums)",
        "companies": [
            "Booking.com", "Adyen", "Zalando", "SAP", "ASML",
            "Delivery Hero", "Klarna", "Spotify", "Revolut", "Celonis", "Personio"
        ],
        "strategy_notes": "EU hiring bars (Booking.com, Zalando, Adyen, SAP) prioritize clean code architecture, maintainability, and thorough explanations over trick problems. Medium problems dominate rounds with emphasis on concurrency and database integration.",
        "readiness_route": "/eu-readiness",
        "readiness_label": "EU Readiness Radar",
    },
    "us": {
        "id": "us",
        "name": "US / Canada Standard",
        "flag": "🇺🇸 🇨🇦",
        "subtitle": "Silicon Valley FAANG & Canadian Tier-1 Tech Bar",
        "badge_text": "🇺🇸 🇨🇦 US / Canada Standard · FAANG Focus",
        "target_total": 300,
        "target_easy": 50,
        "target_medium": 175,
        "target_hard": 75,
        "primary_focus": "Medium + Hard High-Scale Bar (38% DSA weight in US hiring)",
        "companies": [
            "Google", "Meta", "Amazon", "Apple", "Microsoft",
            "Netflix", "Uber", "Shopify", "Stripe", "Databricks", "Airbnb", "Bloomberg"
        ],
        "strategy_notes": "US Big Tech (Google, Meta, Amazon, Apple, Netflix) & Canadian Scale-ups (Shopify, 1Password) require rapid 35-min bug-free problem solving with rigorous edge-case analysis, Hard DP/Graph patterns, and optimal Big-O bounds.",
        "readiness_route": "/na-readiness",
        "readiness_label": "North America Readiness Radar",
    },
    "non_faang": {
        "id": "non_faang",
        "name": "Non-FAANG / Enterprise",
        "flag": "🏢",
        "subtitle": "Fortune 500, FinTech, Healthcare & AllianceTek Clients",
        "badge_text": "🏢 Non-FAANG & Enterprise · Practical Applied Focus",
        "target_total": 125,
        "target_easy": 50,
        "target_medium": 65,
        "target_hard": 10,
        "primary_focus": "Practical Problem Solving + OOP/SOLID & Clean APIs (Easy/Medium Focus)",
        "companies": [
            "Capital One", "Walmart", "JPMorgan", "Fidelity", "Optum",
            "Salesforce", "ServiceNow", "Atlassian", "Cisco", "Dell", "Workday", "PayPal", "Adobe"
        ],
        "strategy_notes": "Non-FAANG enterprises (Fortune 500, Healthcare, FinTech, and consulting clients like AllianceTek) emphasize practical problem solving: Arrays, HashMaps, String parsing, and clean OOP/REST architecture over complex DP puzzles. Code maintainability, boundary checks, and SQL/database integration are key.",
        "readiness_route": "/eu-readiness",
        "readiness_label": "Enterprise Readiness Radar",
    },
    "global": {
        "id": "global",
        "name": "Global / Comprehensive",
        "flag": "🌐",
        "subtitle": "Universal 350+ LeetCode & Big Tech Benchmark",
        "badge_text": "🌐 Global Standard · All Tech Hubs",
        "target_total": 350,
        "target_easy": 60,
        "target_medium": 200,
        "target_hard": 90,
        "primary_focus": "Comprehensive Mastery across all Algorithm Paradigms",
        "companies": [
            "Google", "Meta", "Amazon", "Booking.com", "Adyen", "Zalando",
            "Apple", "Microsoft", "Shopify", "Uber", "Stripe", "SAP"
        ],
        "strategy_notes": "Comprehensive coverage of all 18 algorithmic paradigms across worldwide tech hubs, ensuring fluency for both US FAANG speed rounds and EU architectural deep-dives.",
        "readiness_route": "/eu-readiness",
        "readiness_label": "Global Readiness Overview",
    }
}


@router.get("", response_class=HTMLResponse)
def dsa_page(
    request: Request,
    region: Optional[str] = "eu",
    category: Optional[str] = None,
    topic: Optional[str] = None,
    difficulty: Optional[str] = None,
    company: Optional[str] = None,
    status: Optional[str] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db),
):
    user = db.query(UserProfile).first()
    gamification = get_gamification_state(db)
    topics = db.query(DSATopic).order_by(DSATopic.order_index).all()
    all_topics = db.query(DSATopic).order_by(DSATopic.name).all()
    all_companies = db.query(DSACompany).order_by(DSACompany.name).all()

    # Normalize inputs
    region_key = (region.strip().lower() if region else "eu")
    if region_key not in REGION_CONFIGS:
        region_key = "eu"
    active_region_config = REGION_CONFIGS[region_key]

    category = category.strip() if (category and category.strip()) else None
    topic = topic.strip() if (topic and topic.strip()) else None
    difficulty = difficulty.strip() if (difficulty and difficulty.strip()) else None
    company = company.strip() if (company and company.strip()) else None
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
    from app.services.seed import DSA_TOPICS
    db_categories = [c[0] for c in db.query(DSAProblem.category).distinct().all() if c[0]]
    all_categories_set = set(DSA_TOPICS) | set(db_categories)
    
    # Maintain standard order for known roadmap topics, followed by any custom categories that have problems
    ordered_categories = [t for t in DSA_TOPICS if t in all_categories_set]
    for c in sorted(all_categories_set):
        if c not in ordered_categories and c in db_categories:
            ordered_categories.append(c)

    # Build query for filtered problems
    query = db.query(DSAProblem)
    if category:
        query = query.filter(DSAProblem.category == category)
    if topic:
        query = query.filter(DSAProblem.topics.any(DSATopic.name == topic))
    if difficulty:
        query = query.filter(DSAProblem.difficulty == difficulty)
    if company:
        query = query.filter(DSAProblem.companies.any(DSACompany.name == company))
    if status:
        query = query.filter(DSAProblem.status == status)
    if search_term:
        query = query.filter(
            or_(
                DSAProblem.title.ilike(f"%{search_term}%"),
                DSAProblem.alternate_title.ilike(f"%{search_term}%"),
                DSAProblem.category.ilike(f"%{search_term}%"),
                DSAProblem.pattern.ilike(f"%{search_term}%"),
                DSAProblem.mistake.ilike(f"%{search_term}%"),
                DSAProblem.topics.any(DSATopic.name.ilike(f"%{search_term}%")),
                DSAProblem.companies.any(DSACompany.name.ilike(f"%{search_term}%"))
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
    has_active_filters = bool(category or topic or difficulty or company or status or search_term)

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
        
        if (has_active_filters and filtered_cat_total == 0) or meta["total"] == 0:
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

    # EU and NA readiness summaries from gamification
    eu_readiness = gamification.get("eu_readiness", {})
    na_readiness = gamification.get("na_readiness", {})

    return templates.TemplateResponse("dsa.html", {
        "request": request,
        "user": user,
        "gamification": gamification,
        "eu_readiness": eu_readiness,
        "na_readiness": na_readiness,
        "region_configs": REGION_CONFIGS,
        "selected_region": region_key,
        "active_region_config": active_region_config,
        "today": date.today(),
        "topics": topics,
        "all_topics": all_topics,
        "all_companies": all_companies,
        "all_categories": ordered_categories,
        "categories_view": categories_view,
        "filtered_problems_count": len(filtered_problems),
        "difficulties": DIFFICULTIES,
        "statuses": STATUSES,
        "selected_category": category,
        "selected_topic": topic,
        "selected_difficulty": difficulty,
        "selected_company": company,
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


def resolve_topics(db: Session, topic_ids: List[int], new_topics_str: Optional[str], default_category: str) -> List[DSATopic]:
    topics = []
    if topic_ids:
        topics.extend(db.query(DSATopic).filter(DSATopic.id.in_(topic_ids)).all())
    if new_topics_str and new_topics_str.strip():
        names = [n.strip() for n in new_topics_str.split(",") if n.strip()]
        for name in names:
            existing_t = db.query(DSATopic).filter(DSATopic.name.ilike(name)).first()
            if existing_t:
                if existing_t not in topics:
                    topics.append(existing_t)
            else:
                max_o = max([t.order_index for t in db.query(DSATopic).all()], default=0)
                new_t = DSATopic(name=name, order_index=max_o + 1)
                db.add(new_t)
                db.flush()
                topics.append(new_t)
    if not topics and default_category:
        cat_t = db.query(DSATopic).filter(DSATopic.name.ilike(default_category)).first()
        if cat_t and cat_t not in topics:
            topics.append(cat_t)
    return topics


def resolve_companies(db: Session, company_ids: List[int], new_companies_str: Optional[str]) -> List[DSACompany]:
    comps = []
    if company_ids:
        comps.extend(db.query(DSACompany).filter(DSACompany.id.in_(company_ids)).all())
    if new_companies_str and new_companies_str.strip():
        names = [n.strip() for n in new_companies_str.split(",") if n.strip()]
        for name in names:
            existing_c = db.query(DSACompany).filter(DSACompany.name.ilike(name)).first()
            if existing_c:
                if existing_c not in comps:
                    comps.append(existing_c)
            else:
                max_o = max([c.order_index for c in db.query(DSACompany).all()], default=0)
                new_c = DSACompany(name=name, order_index=max_o + 1)
                db.add(new_c)
                db.flush()
                comps.append(new_c)
    return comps


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
    new_topics: Optional[str] = Form(""),
    company_ids: List[int] = Form(default=[]),
    new_companies: Optional[str] = Form(""),
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

    topics = resolve_topics(db, topic_ids, new_topics, category)
    companies = resolve_companies(db, company_ids, new_companies)

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
        companies=companies,
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
    new_topics: Optional[str] = Form(""),
    company_ids: List[int] = Form(default=[]),
    new_companies: Optional[str] = Form(""),
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
    
    topics = resolve_topics(db, topic_ids, new_topics, category)
    companies = resolve_companies(db, company_ids, new_companies)

    p.topics = topics
    p.companies = companies

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

