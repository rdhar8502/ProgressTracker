from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List, Dict, Any

from app.database import get_db
from app.models.dsa import DSAProblem, DSATopic
from app.models.system_design import SystemDesignSubConcept, SystemDesignCase
from app.models.ai_llm import AILLMTopic
from app.models.daily_log import DailyLog
from app.models.application import Application
from app.models.personal_hub import PersonalHubItem

router = APIRouter(prefix="/api", tags=["search"])


@router.get("/search")
def search_api(q: str = "", db: Session = Depends(get_db)):
    if not q or not q.strip():
        return {"results": []}

    q_clean = q.strip()
    like_query = f"%{q_clean}%"
    results = []

    # 1. DSA Problems
    dsa_problems = db.query(DSAProblem).filter(
        or_(
            DSAProblem.title.ilike(like_query),
            DSAProblem.alternate_title.ilike(like_query),
            DSAProblem.pattern.ilike(like_query),
            DSAProblem.mistake.ilike(like_query)
        )
    ).limit(8).all()
    for p in dsa_problems:
        results.append({
            "category": "DSA Problem",
            "title": p.clean_title,
            "snippet": f"Pattern: {p.pattern}" if p.pattern else f"Difficulty: {p.difficulty} ({p.status})",
            "url": f"/dsa?search={p.clean_title}",
            "icon": "💻",
            "badge_class": "badge-purple" if p.difficulty == "Hard" else ("badge-amber" if p.difficulty == "Medium" else "badge-green")
        })

    # 2. DSA Topics
    dsa_topics = db.query(DSATopic).filter(DSATopic.name.ilike(like_query)).limit(4).all()
    for t in dsa_topics:
        results.append({
            "category": "DSA Topic",
            "title": t.name,
            "snippet": t.description or "Topic in Data Structures & Algorithms",
            "url": f"/dsa?topic_id={t.id}",
            "icon": "📁",
            "badge_class": "badge-gray"
        })

    # 3. System Design SubConcepts
    sd_subconcepts = db.query(SystemDesignSubConcept).filter(
        or_(
            SystemDesignSubConcept.subconcept_name.ilike(like_query),
            SystemDesignSubConcept.notes.ilike(like_query)
        )
    ).limit(8).all()
    for sc in sd_subconcepts:
        results.append({
            "category": "System Design Concept",
            "title": sc.subconcept_name,
            "snippet": sc.notes[:100] + "..." if len(sc.notes) > 100 else sc.notes,
            "url": f"/system-design?search={sc.subconcept_name}",
            "icon": "🏗️",
            "badge_class": "badge-blue"
        })

    # 4. System Design Cases
    sd_cases = db.query(SystemDesignCase).filter(
        or_(
            SystemDesignCase.system_name.ilike(like_query),
            SystemDesignCase.notes.ilike(like_query),
            SystemDesignCase.key_components.ilike(like_query)
        )
    ).limit(4).all()
    for c in sd_cases:
        results.append({
            "category": "System Design Case Study",
            "title": c.system_name,
            "snippet": f"Components: {c.key_components[:80]}..." if c.key_components else "Case study details",
            "url": f"/system-design?search={c.system_name}",
            "icon": "📦",
            "badge_class": "badge-blue"
        })

    # 5. AI / LLM Topics
    ai_topics = db.query(AILLMTopic).filter(
        or_(
            AILLMTopic.topic_name.ilike(like_query),
            AILLMTopic.notes.ilike(like_query)
        )
    ).limit(8).all()
    for t in ai_topics:
        results.append({
            "category": "AI / LLM Topic",
            "title": t.topic_name,
            "snippet": t.notes[:100] + "..." if len(t.notes) > 100 else t.notes,
            "url": f"/ai-llm?search={t.topic_name}",
            "icon": "🤖",
            "badge_class": "badge-amber"
        })

    # 6. Daily Logs
    daily_logs = db.query(DailyLog).filter(
        or_(
            DailyLog.sub_topic.ilike(like_query),
            DailyLog.notes.ilike(like_query)
        )
    ).limit(4).all()
    for log in daily_logs:
        results.append({
            "category": "Daily Log",
            "title": f"Log for {log.date.strftime('%b %d, %Y')}",
            "snippet": f"{log.category}: {log.sub_topic or log.notes[:80]}",
            "url": f"/daily?log_date={log.date.isoformat()}",
            "icon": "📝",
            "badge_class": "badge-gray"
        })

    # 7. Job Applications
    apps = db.query(Application).filter(
        or_(
            Application.company.ilike(like_query),
            Application.role.ilike(like_query),
            Application.notes.ilike(like_query)
        )
    ).limit(4).all()
    for a in apps:
        results.append({
            "category": "Job Application",
            "title": f"{a.company} — {a.role}",
            "snippet": f"Stage: {a.stage} | Location: {a.location or 'Remote'}",
            "url": f"/applications?search={a.company}",
            "icon": "📤",
            "badge_class": "badge-green"
        })

    # 8. Personal Hub (Notes / Reminders)
    hub_items = db.query(PersonalHubItem).filter(
        or_(
            PersonalHubItem.title.ilike(like_query),
            PersonalHubItem.content.ilike(like_query),
            PersonalHubItem.source.ilike(like_query)
        )
    ).limit(8).all()
    for item in hub_items:
        # Determine icon and badge based on category
        item_icon = "💡"
        item_badge = "badge-gray"
        if item.category == "Reminder":
            item_icon = "⏰"
            item_badge = "badge-amber"
        elif item.category == "Need to Ask":
            item_icon = "❓"
            item_badge = "badge-blue"
        elif item.category == "Visa & Immigration":
            item_icon = "✈️"
            item_badge = "badge-purple"
        elif item.category == "Note":
            item_icon = "💡"
            item_badge = "badge-green"

        results.append({
            "category": f"Notes & Reminders ({item.category})",
            "title": item.title,
            "snippet": item.content[:100] + "..." if len(item.content) > 100 else item.content,
            "url": f"/personal-hub?search={item.title}",
            "icon": item_icon,
            "badge_class": item_badge
        })

    return {"results": results[:20]}
