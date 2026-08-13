"""
Seed script — populates the database with initial prep plan data.
Safe to run multiple times (checks for existing data first).
"""
from datetime import date
from sqlalchemy.orm import Session

from app.models.user import UserProfile, SalaryTarget, WeeklySchedule
from app.models.dsa import DSATopic
from app.models.system_design import SystemDesignTopic, SystemDesignCase
from app.models.ai_llm import AILLMTopic
from app.models.github import GithubProject, GithubTask
from app.services.week_utils import generate_weeks, week_target_hours


START_DATE = date(2026, 8, 12)
END_DATE = date(2027, 3, 31)

DSA_TOPICS = [
    "Arrays and Strings",
    "HashMap / HashSet",
    "Two Pointers",
    "Sliding Window",
    "Stack / Monotonic Stack",
    "Queue / Deque",
    "Binary Search",
    "Linked List",
    "Recursion and Backtracking",
    "Trees / BST",
    "Heap / Priority Queue",
    "Graph BFS/DFS",
    "Topological Sort",
    "Union Find",
    "Tries",
    "Dynamic Programming Basics",
    "DP on Strings",
    "DP on Grids",
    "Intervals",
    "Bit Manipulation",
]

WEEK_THEMES = [
    "Arrays, Strings & HashMap",
    "Two Pointers & Sliding Window",
    "Stack, Queue & Deque",
    "Binary Search",
    "Linked List & Recursion",
    "Trees & BST",
    "Heap & Priority Queue",
    "Graph BFS/DFS",
    "System Design: HTTP, REST, Load Balancers",
    "System Design: Caching & Rate Limiting",
    "Topological Sort & Union Find",
    "Tries & DP Basics",
    "DP on Strings & Grids",
    "Intervals & Bit Manipulation",
    "System Design: Databases & Queues",
    "AI/LLM: Embeddings, Chunking, Vector DBs",
    "AI/LLM: RAG Pipeline & Evaluation",
    "AI/LLM: Agents, Memory & Tool Calling",
    "System Design: Observability & Deployment",
    "GitHub Project 1: Production RAG System",
    "GitHub Project 2: AI Agent Workflow",
    "GitHub Project 3: Scalable Backend API",
    "System Design: Full System Designs (URL, Chat)",
    "System Design: Full System Designs (Payment, Ride)",
    "AI/LLM: Production & Optimization",
    "LinkedIn & Resume Polish",
    "Mock Interviews & Review Week",
    "Applications — Active Apply Week",
    "Applications + Mock Interviews",
    "Applications + Final Review",
    "Applications + Mock Interviews",
    "Final Sprint — Applications",
    "Final Sprint — Mock Interviews",
]

SYSTEM_DESIGN_TOPICS = [
    ("Core", "HTTP, REST, WebSockets"),
    ("Core", "Load Balancers"),
    ("Core", "API Gateway"),
    ("Core", "Rate Limiting"),
    ("Core", "Caching: Redis, CDN, Browser Cache"),
    ("Core", "SQL vs NoSQL"),
    ("Core", "PostgreSQL Indexing, Transactions, Isolation"),
    ("Core", "Message Queues: Kafka, RabbitMQ, SQS"),
    ("Core", "Background Jobs: Celery, Workers"),
    ("Core", "Object Storage: S3-Style Systems"),
    ("Advanced", "Search: Elasticsearch / Vector Search"),
    ("Advanced", "Authentication: JWT, OAuth, Sessions"),
    ("Advanced", "Observability: Logs, Metrics, Tracing"),
    ("Advanced", "Deployment: Docker, CI/CD, Kubernetes Basics"),
    ("Advanced", "Scalability, Sharding, Replication"),
    ("Advanced", "Reliability, Retries, Circuit Breakers"),
    ("Advanced", "Security Basics"),
    ("Advanced", "Cost-Aware Design"),
]

SYSTEM_DESIGN_CASES = [
    "URL Shortener",
    "WhatsApp / Chat System",
    "Notification System",
    "File Upload System",
    "Payment / Order System",
    "Ride Booking System",
    "Log Ingestion System",
    "RAG Document Chatbot",
    "AI Agent Workflow Platform",
    "Multi-Tenant SaaS Backend",
]

AI_LLM_TOPICS = [
    ("Core", "Embeddings"),
    ("Core", "Chunking Strategies"),
    ("Core", "Vector Databases"),
    ("RAG", "Hybrid Search"),
    ("RAG", "Reranking"),
    ("RAG", "RAG Evaluation"),
    ("RAG", "Hallucination Control"),
    ("RAG", "Prompt Injection"),
    ("RAG", "Guardrails"),
    ("Agents", "LangChain vs LangGraph"),
    ("Agents", "Agent Memory"),
    ("Agents", "Tool Calling"),
    ("Agents", "Human-in-the-Loop"),
    ("Agents", "LangGraph Persistence / Checkpoints"),
    ("Agents", "Multi-Agent Systems"),
    ("Production", "Async FastAPI Serving"),
    ("Production", "Streaming Responses"),
    ("Production", "Background Processing"),
    ("Production", "Model Latency / Cost Optimization"),
    ("Production", "Production AI Monitoring"),
]

GITHUB_PROJECTS = [
    {
        "name": "Production RAG System",
        "description": "FastAPI + PostgreSQL + vector DB + background ingestion + auth + Docker + tests",
        "tech_stack": "FastAPI, PostgreSQL, pgvector, Celery, Redis, Docker, pytest",
        "tasks": [
            ("Architecture", "Design architecture diagram"),
            ("Core", "FastAPI app skeleton with auth"),
            ("Core", "PostgreSQL + pgvector integration"),
            ("Core", "Document ingestion pipeline"),
            ("Core", "Chunking and embedding service"),
            ("Core", "Vector retrieval + reranking"),
            ("Core", "Answer generation with LLM"),
            ("Core", "Background processing with Celery"),
            ("DevOps", "Docker + docker-compose setup"),
            ("Testing", "Unit + integration tests"),
            ("Docs", "Clean README with setup guide"),
            ("Docs", "API documentation"),
            ("Docs", "Architecture diagram in README"),
            ("Docs", "Trade-offs section"),
            ("Docs", "Deployment notes"),
        ],
    },
    {
        "name": "AI Agent Workflow Platform",
        "description": "LangGraph agent with tools, memory, human approval step, logging, retry handling",
        "tech_stack": "LangGraph, FastAPI, PostgreSQL, Redis, Docker",
        "tasks": [
            ("Architecture", "Design agent workflow diagram"),
            ("Core", "LangGraph graph definition"),
            ("Core", "Tool implementations"),
            ("Core", "Agent memory with persistence"),
            ("Core", "Human-in-the-loop approval step"),
            ("Core", "Retry handling and error recovery"),
            ("Core", "Logging and observability"),
            ("Core", "FastAPI serving layer"),
            ("DevOps", "Docker + docker-compose setup"),
            ("Testing", "Unit + integration tests"),
            ("Docs", "Clean README with setup guide"),
            ("Docs", "Architecture diagram in README"),
            ("Docs", "Trade-offs section"),
        ],
    },
    {
        "name": "Scalable Backend API",
        "description": "Multi-tenant FastAPI/Django app with RBAC, Celery, Redis, PostgreSQL, Docker, CI",
        "tech_stack": "FastAPI, PostgreSQL, Redis, Celery, Docker, GitHub Actions",
        "tasks": [
            ("Architecture", "Design multi-tenant architecture"),
            ("Core", "Multi-tenant data isolation"),
            ("Core", "RBAC implementation"),
            ("Core", "REST API with FastAPI"),
            ("Core", "Celery background tasks"),
            ("Core", "Redis caching layer"),
            ("Core", "PostgreSQL schema with migrations"),
            ("DevOps", "Docker + docker-compose"),
            ("DevOps", "GitHub Actions CI pipeline"),
            ("Testing", "Unit + integration tests"),
            ("Docs", "Clean README with setup guide"),
            ("Docs", "API documentation"),
            ("Docs", "Trade-offs section"),
        ],
    },
]

SALARY_TARGETS = [
    ("United States", "USD", 120000, 160000, "year"),
    ("United States (Strong AI)", "USD", 160000, 190000, "year"),
    ("Canada", "CAD", 110000, 150000, "year"),
    ("United Kingdom", "GBP", 70000, 100000, "year"),
    ("Germany / Netherlands", "EUR", 75000, 110000, "year"),
    ("UAE", "AED", 300000, 540000, "year"),  # 25k-45k/month × 12
]


def seed_database(db: Session):
    """Seed all initial data. Safe to call multiple times."""

    # --- User Profile ---
    if not db.query(UserProfile).first():
        user = UserProfile(
            name="Rahul Dhar",
            target_role="Lead AI Engineer / Senior Python Backend Engineer",
            start_date=START_DATE,
            end_date=END_DATE,
            current_company="AllianceTek",
            years_experience=7,
            weekday_target_hours=1.5,
            saturday_target_hours=4.0,
            sunday_target_hours=3.5,
        )
        db.add(user)

    # --- Salary Targets ---
    if not db.query(SalaryTarget).first():
        for region, currency, s_min, s_max, unit in SALARY_TARGETS:
            db.add(SalaryTarget(
                region=region, currency=currency,
                salary_min=s_min, salary_max=s_max, salary_unit=unit
            ))

    # --- Weekly Schedule ---
    if not db.query(WeeklySchedule).first():
        weeks = generate_weeks(START_DATE, END_DATE)
        user = db.query(UserProfile).first()
        wkday = user.weekday_target_hours if user else 1.5
        sat = user.saturday_target_hours if user else 4.0
        sun = user.sunday_target_hours if user else 3.5
        target = week_target_hours(wkday, sat, sun)

        for i, (wn, ws, we) in enumerate(weeks):
            theme = WEEK_THEMES[i] if i < len(WEEK_THEMES) else "Study & Practice"
            db.add(WeeklySchedule(
                week_number=wn,
                week_start=ws,
                week_end=we,
                target_hours=target,
                theme=theme,
            ))

    # --- DSA Topics ---
    if not db.query(DSATopic).first():
        for i, name in enumerate(DSA_TOPICS):
            db.add(DSATopic(name=name, order_index=i + 1))

    # --- System Design Topics ---
    if not db.query(SystemDesignTopic).first():
        for i, (cat, name) in enumerate(SYSTEM_DESIGN_TOPICS):
            db.add(SystemDesignTopic(category=cat, topic_name=name, order_index=i + 1))

    # --- System Design Cases ---
    if not db.query(SystemDesignCase).first():
        for i, name in enumerate(SYSTEM_DESIGN_CASES):
            db.add(SystemDesignCase(system_name=name, order_index=i + 1))

    # --- AI/LLM Topics ---
    if not db.query(AILLMTopic).first():
        for i, (cat, name) in enumerate(AI_LLM_TOPICS):
            db.add(AILLMTopic(topic_name=name, category=cat, order_index=i + 1))

    # --- GitHub Projects ---
    if not db.query(GithubProject).first():
        for i, proj in enumerate(GITHUB_PROJECTS):
            p = GithubProject(
                name=proj["name"],
                description=proj["description"],
                tech_stack=proj["tech_stack"],
                order_index=i + 1,
            )
            db.add(p)
            db.flush()  # get p.id
            for cat, task_name in proj["tasks"]:
                db.add(GithubTask(project_id=p.id, task_name=task_name, category=cat))

    db.commit()
    print("✅ Database seeded successfully.")
