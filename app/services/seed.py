"""
Seed script — populates the database with initial prep plan data.
Safe to run multiple times (checks for existing data first).
"""
from datetime import date
from sqlalchemy.orm import Session

from app.models.user import UserProfile, SalaryTarget, WeeklySchedule
from app.models.dsa import DSATopic
from app.models.system_design import SystemDesignConcept, SystemDesignSubConcept, SystemDesignCase
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
    ("Core", "HTTP, REST, WebSockets", ["HTTP", "REST", "WebSockets"]),
    ("Core", "Load Balancers", ["Load Balancers"]),
    ("Core", "API Gateway", ["API Gateway"]),
    ("Core", "Rate Limiting", ["Rate Limiting"]),
    ("Core", "Caching", ["Redis", "CDN", "Browser Cache"]),
    ("Core", "SQL vs NoSQL", ["SQL", "NoSQL"]),
    ("Core", "PostgreSQL", ["Indexing", "Transactions", "Isolation"]),
    ("Core", "Message Queues", ["Kafka", "RabbitMQ", "SQS"]),
    ("Core", "Background Jobs", ["Celery", "Workers"]),
    ("Core", "Object Storage", ["S3-Style Systems"]),
    ("Advanced", "Search", ["Elasticsearch", "Vector Search"]),
    ("Advanced", "Authentication", ["JWT", "OAuth", "Sessions"]),
    ("Advanced", "Observability", ["Logs", "Metrics", "Tracing"]),
    ("Advanced", "Deployment", ["Docker", "CI/CD", "Kubernetes Basics"]),
    ("Advanced", "Scalability", ["Sharding", "Replication"]),
    ("Advanced", "Reliability", ["Retries", "Circuit Breakers"]),
    ("Advanced", "Security Basics", ["Security Basics"]),
    ("Advanced", "Cost-Aware Design", ["Cost-Aware Design"]),
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
        "name": "Production-Grade RAG with RBAC",
        "description": "Enterprise-grade RAG system with Role-Based Access Control (RBAC), hybrid search, re-ranking, and citation enforcement.",
        "tech_stack": "FastAPI, PostgreSQL, pgvector, Redis, Celery, Cohere (Rerank), Docker, pytest, LangChain",
        "tasks": [
            ("Architecture", "Design architecture & security model diagram"),
            ("Core", "FastAPI app skeleton with OAuth2 + RBAC authorization"),
            ("Core", "PostgreSQL + pgvector setup for document storage"),
            ("Core", "Document ingestion pipeline with semantic chunking"),
            ("Core", "Implement Role-Based Access Control (RBAC) metadata filtering in pgvector queries"),
            ("Core", "Hybrid Search integration (vector semantic search + BM25 keyword search)"),
            ("Core", "Re-ranking service integration using Cohere/Cross-Encoder"),
            ("Core", "Answer generation engine with verifiable citations & hallucination check"),
            ("Core", "Background asynchronous document parsing via Celery & Redis"),
            ("DevOps", "Docker & docker-compose configuration for all services"),
            ("Testing", "Unit & integration testing with pytest"),
            ("Testing", "RAG evaluation pipeline measuring faithfulness & answer relevance"),
            ("Docs", "Clean README with architecture trade-offs, security, and setup guide"),
        ],
    },
    {
        "name": "Local Agentic Workflow Platform (Ollama + MCP)",
        "description": "Local-first AI agent using LangGraph, Ollama, and Model Context Protocol (MCP) to interact with local tools securely.",
        "tech_stack": "LangGraph, Ollama, MCP SDK, FastAPI, SQLite, Docker",
        "tasks": [
            ("Architecture", "Design agent workflow state machine & MCP tool mappings"),
            ("Core", "LangGraph workflow state machine using local LLMs (e.g., Llama 3)"),
            ("Core", "Custom MCP Server development to interact with local directories and database"),
            ("Core", "Persistent agent state and conversational memory using SQLite checkpointer"),
            ("Core", "Interactive human-in-the-loop approval step for destructive actions"),
            ("Core", "Resilience layer with self-correction and LLM tool-calling error recovery"),
            ("Core", "Local model performance benchmarking (latency vs accuracy)"),
            ("Core", "FastAPI wrapper for agent orchestration APIs"),
            ("DevOps", "Docker compose setup with Ollama GPU acceleration configuration"),
            ("Testing", "Agent trajectory testing and mock MCP tool integration tests"),
            ("Docs", "Detailed README with MCP installation, Ollama configuration, and system trade-offs"),
        ],
    },
    {
        "name": "Text-to-SQL Clarification Agent",
        "description": "Robust Text-to-SQL converter that prompts users for clarification on ambiguous intents and runs in a sandbox.",
        "tech_stack": "FastAPI, PostgreSQL, SQL Alchemy, Pydantic, Gemini/OpenAI, Docker",
        "tasks": [
            ("Architecture", "Design Text-to-SQL architecture, parser schema, and clarification flows"),
            ("Core", "Database schema metadata ingestion & representation generator"),
            ("Core", "Pydantic structured output model for query parsing & intent classification"),
            ("Core", "Ambiguity detector to evaluate if user query requires clarification"),
            ("Core", "Interactive clarification API to ask clarifying questions and merge user feedback"),
            ("Core", "Secure read-only SQL execution sandbox with query execution timeout guardrails"),
            ("Core", "Self-healing loop that retries/corrects generated SQL on syntax or schema errors"),
            ("DevOps", "Docker compose with sandbox PostgreSQL container"),
            ("Testing", "SQL generation evaluation suite with ground truth test cases"),
            ("Docs", "Detailed README documenting schema security, sandbox isolation, and trade-offs"),
        ],
    },
    {
        "name": "AI Observability & Evaluation Pipeline",
        "description": "Continuous monitoring and tracing pipeline for AI metrics like cost, latency (p50/p95), and regression gating in CI.",
        "tech_stack": "FastAPI, Prometheus, Grafana, OpenTelemetry, LangSmith/Phoenix, GitHub Actions",
        "tasks": [
            ("Architecture", "Design telemetry collection architecture and Prometheus metrics mapping"),
            ("Core", "Instrumentation of LLM calls with OpenTelemetry tracing spans"),
            ("Core", "FastAPI middleware to track p50/p95 latency, prompt/completion token count, and cost"),
            ("Core", "Telemetry dashboard setup for tracking cached token ratios and cost efficiency"),
            ("Core", "Continuous evaluation service running accuracy and faithfulness metrics on live logs"),
            ("DevOps", "Prometheus configuration and Grafana dashboards for visual monitoring"),
            ("DevOps", "GitHub Actions CI pipeline with evaluation gating (build fails if accuracy drops below threshold)"),
            ("Testing", "Automated traffic generator simulating user queries and edge cases"),
            ("Docs", "README outlining latency budget, dashboard setup, and evaluation criteria"),
        ],
    },
    {
        "name": "Real-Time Multimodal Streaming Pipeline",
        "description": "WebSocket-based live streaming audio/video assistant with speech-to-text, text-to-speech, and latency profiling.",
        "tech_stack": "FastAPI, WebSockets, WebRTC, Ollama/Gemini Live API, PyRTC, Docker",
        "tasks": [
            ("Architecture", "Design real-time audio/video streaming flow and latency budget breakdown"),
            ("Core", "FastAPI WebSocket and WebRTC signaling servers for low-latency streaming"),
            ("Core", "Streaming Speech-to-Text (STT) ingestion with silence detection"),
            ("Core", "Streaming LLM inference with sentence/phrase-based chunking"),
            ("Core", "Streaming Text-to-Speech (TTS) synthesis engine for real-time response generation"),
            ("Core", "Latency profiling module measuring end-to-end audio roundtrip latency"),
            ("DevOps", "Docker configuration optimized for media stream processing and GPU passthrough"),
            ("Testing", "Websocket connection load tests and audio streaming latency benchmarks"),
            ("Docs", "Detailed README with streaming architecture, latency metrics, and performance optimizations"),
        ],
    },
    {
        "name": "Scalable Multi-Tenant Backend API",
        "description": "Enterprise-grade multi-tenant API framework featuring row-level schema isolation and Celery task execution.",
        "tech_stack": "FastAPI, PostgreSQL, SQLAlchemy, Redis, Celery, GitHub Actions, Docker",
        "tasks": [
            ("Architecture", "Design multi-tenant row-level security and schema isolation model"),
            ("Core", "FastAPI multi-tenant middleware detecting tenant context via subdomain/header"),
            ("Core", "Dynamic database schema creation and connection pooling per tenant"),
            ("Core", "Granular Role-Based Access Control (RBAC) validation decorator layer"),
            ("Core", "Asynchronous background task runner with Celery, Redis, and flower monitor"),
            ("Core", "Caching strategy using Redis for high-throughput endpoint optimization"),
            ("DevOps", "Docker compose orchestration and database migration setup using Alembic"),
            ("DevOps", "GitHub Actions CI/CD deployment pipeline with database migrations"),
            ("Testing", "Concurrent tenant access isolation tests and API performance testing"),
            ("Docs", "Clean README with multi-tenancy trade-offs, scaling, and database migration docs"),
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
    weeks = generate_weeks(START_DATE, END_DATE)
    existing_weeks = db.query(WeeklySchedule).order_by(WeeklySchedule.week_number).all()

    if not existing_weeks or len(existing_weeks) != len(weeks) or existing_weeks[0].week_start != weeks[0][1]:
        # Delete existing weekly schedules and re-create them
        db.query(WeeklySchedule).delete()
        db.commit()

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

    # --- System Design Concepts & Sub-concepts ---
    if not db.query(SystemDesignConcept).first():
        for i, (cat, concept_name, sub_list) in enumerate(SYSTEM_DESIGN_TOPICS):
            concept = SystemDesignConcept(category=cat, concept_name=concept_name, order_index=i + 1)
            db.add(concept)
            db.flush()
            for j, sub_name in enumerate(sub_list):
                db.add(SystemDesignSubConcept(
                    concept_id=concept.id,
                    subconcept_name=sub_name,
                    order_index=j + 1,
                    status="Not Started"
                ))

    # --- System Design Cases ---
    if not db.query(SystemDesignCase).first():
        for i, name in enumerate(SYSTEM_DESIGN_CASES):
            db.add(SystemDesignCase(system_name=name, order_index=i + 1))

    # --- AI/LLM Topics ---
    if not db.query(AILLMTopic).first():
        for i, (cat, name) in enumerate(AI_LLM_TOPICS):
            db.add(AILLMTopic(topic_name=name, category=cat, order_index=i + 1))

    # --- GitHub Projects ---
    # Delete existing GitHub projects and tasks to reset/re-seed the updated portfolio
    db.query(GithubTask).delete()
    db.query(GithubProject).delete()
    db.commit()

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
