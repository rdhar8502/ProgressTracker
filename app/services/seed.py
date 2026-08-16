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
    # --- Category: Core ---
    (
        "Core",
        "Basics & Scaling Fundamentals",
        [
            "What is System Design & Interview Framework",
            "Horizontal vs. Vertical Scaling",
            "Capacity Estimation & Back-of-the-Envelope Calculations",
            "Latency Numbers Every Engineer Should Know",
            "Single Point of Failure (SPOF) & High Availability",
            "Concurrency, Threads & OS Processes",
            "Thrashing & OS Memory Management",
        ],
    ),
    (
        "Core",
        "Networking & Web Protocols",
        [
            "HTTP, HTTPS & HTTP/2 vs HTTP/3 (QUIC)",
            "Internet TCP/IP Stack & UDP",
            "What Happens When You Enter google.com (DNS, Handshake, TLS)",
            "WebSockets & Server-Sent Events (SSE)",
            "Polling vs Long Polling vs WebSockets vs WebRTC",
        ],
    ),
    (
        "Core",
        "Load Balancing & Traffic Management",
        [
            "Load Balancing Algorithms (Round Robin, Least Connections, IP Hash)",
            "Layer 4 vs Layer 7 Load Balancing & SSL Termination",
            "Consistent Hashing & Virtual Nodes / Hash Ring",
            "Reverse Proxy vs Forward Proxy (Nginx / HAProxy)",
            "DNS Load Balancing & Anycast Routing",
        ],
    ),
    (
        "Core",
        "API Design & Gateways",
        [
            "RESTful API Design & Best Practices",
            "API Gateway Architecture (Routing, Aggregation, Rate Limiting, Auth)",
            "GraphQL Architecture & Trade-offs",
            "gRPC & Protocol Buffers (Protobuf)",
            "Asynchronous APIs & Webhook Architecture",
        ],
    ),
    (
        "Core",
        "Rate Limiting & Traffic Shaping",
        [
            "Token Bucket Algorithm",
            "Leaky Bucket Algorithm",
            "Fixed Window & Sliding Window Counter",
            "Distributed Rate Limiting (Redis & Lua Scripting)",
            "Throttling & DDoS Protection",
        ],
    ),
    (
        "Core",
        "Caching Deep Dive",
        [
            "Distributed Caching (Redis vs Memcached)",
            "Content Delivery Networks (CDN) & Edge Caching (Push vs Pull)",
            "Cache Write Policies (Write-Through, Write-Around, Write-Back / Write-Behind)",
            "Cache Eviction & Replacement Policies (LRU, LFU, Segmented LRU, ARC)",
            "Cache Invalidation & Pitfalls (Cache Avalanche, Stampede, Penetration)",
        ],
    ),
    (
        "Core",
        "Relational Databases (SQL & PostgreSQL)",
        [
            "RDBMS Fundamentals & Normalization",
            "Database Indexes (B-Tree, B+Tree, Composite, Hash)",
            "Transaction Isolation Levels (Read Uncommitted, Read Committed, Repeatable Read, Serializable)",
            "Query Optimization & EXPLAIN ANALYZE",
            "Database Connection Pooling (PgBouncer, SQLAlchemy Pool)",
            "Postgres Pooling",
            "Database Migrations & Zero-Downtime Schema Evolution",
        ],
    ),
    (
        "Core",
        "NoSQL Databases & Internals",
        [
            "Key-Value & Document Stores (DynamoDB, MongoDB)",
            "Wide-Column & Columnar Stores (Cassandra, ClickHouse)",
            "Storage Engine Internals (LSM-Trees, SSTables, WAL vs B-Trees)",
            "Bloom Filters & Counting Bloom Filters",
            "Location-Based Databases & Spatial Indexing (Geohash, QuadTree, Google S2)",
            "Time-Series Databases (Gorilla Compression, InfluxDB, TimescaleDB)",
        ],
    ),

    # --- Category: Advanced ---
    (
        "Advanced",
        "Message Queues & Event Streaming",
        [
            "Message Queues (RabbitMQ, AWS SQS)",
            "Event Streaming & Distributed Log (Apache Kafka Architecture, Partitions, Offsets)",
            "Publisher-Subscriber (Pub/Sub) Model",
            "Event-Driven Architecture & Event Sourcing",
            "Database as a Message Queue Anti-Pattern & Transactional Outbox Pattern",
        ],
    ),
    (
        "Advanced",
        "Background Jobs & Stream Processing",
        [
            "Task Queues & Asynchronous Workers (Celery, BullMQ)",
            "Distributed Workflow Orchestration (Temporal, Airflow, Netflix Conductor)",
            "Batch Processing vs Stream Processing (Apache Spark, Apache Flink)",
        ],
    ),
    (
        "Advanced",
        "Search & Specialized Storage",
        [
            "Inverted Indexes & Full-Text Search (Elasticsearch, Lucene)",
            "Vector Search & Vector Databases (pgvector, Milvus, HNSW)",
            "Distributed Object Storage (S3 Architecture, Multipart Uploads, Blob Store)",
        ],
    ),
    (
        "Advanced",
        "Microservices Architecture & Migration",
        [
            "Microservices vs Monoliths & Modular Monolith",
            "Monolith to Microservices Migration (Strangler Fig Pattern)",
            "Service-to-Service Communication (Synchronous vs Asynchronous)",
            "Domain-Driven Design (DDD) & Bounded Contexts",
        ],
    ),

    # --- Category: Distributed Systems ---
    (
        "Distributed Systems",
        "Distributed Consistency & Theorems",
        [
            "CAP Theorem & PACELC Theorem",
            "Data Consistency Models (Strong / Linearizability, Causal, Eventual Consistency)",
            "Optimistic Concurrency Control (OCC) vs Pessimistic Locking",
            "Vector Clocks & Conflict Resolution",
        ],
    ),
    (
        "Distributed Systems",
        "Distributed Transactions & Consensus",
        [
            "Two-Phase Commit (2PC) & Three-Phase Commit (3PC)",
            "Saga Pattern (Choreography vs Orchestration)",
            "Distributed Consensus Protocols (Raft, Paxos)",
            "Distributed Locking (Redis Redlock, ZooKeeper, etcd)",
            "Quorum Reads & Writes (Leaderless Replication / Dynamo-style)",
        ],
    ),
    (
        "Distributed Systems",
        "Scalability & Data Partitioning",
        [
            "Master-Slave (Leader-Follower) Replication & Read Replicas",
            "Multi-Leader Replication & Conflict Handling",
            "Database Sharding Strategies (Range, Hash, Directory-Based)",
            "Cross-Shard Transactions & Resharding",
        ],
    ),

    # --- Category: Infrastructure ---
    (
        "Infrastructure",
        "Observability, SRE & Monitoring",
        [
            "Three Pillars of Observability: Logs, Metrics, Traces",
            "Distributed Tracing (OpenTelemetry, Jaeger)",
            "Metrics Collection & Dashboards (Prometheus, Grafana)",
            "Centralized Structured Logging (ELK / EFK / Vector)",
            "Anomaly Detection, Alerting & SLO / SLA / SLI Tracking",
        ],
    ),
    (
        "Infrastructure",
        "Reliability & Fault Tolerance",
        [
            "Circuit Breaker Pattern & Fallback Mechanisms",
            "Retry Strategies with Exponential Backoff & Jitter",
            "Bulkhead Pattern & Cascading Failure Prevention",
            "Dead Letter Queues (DLQ) & Poison Message Handling",
            "Graceful Degradation & Load Shedding",
        ],
    ),
    (
        "Infrastructure",
        "Deployment, Containers & Service Mesh",
        [
            "Docker & Containerization Internals",
            "Kubernetes Architecture & Pod Orchestration",
            "Service Discovery & Heartbeats (Consul, Eureka, ZooKeeper)",
            "Service Mesh & Sidecar Pattern (Envoy, Istio, Data Plane vs Control Plane)",
            "CI/CD & Deployment Strategies (Blue-Green, Canary, Rolling)",
        ],
    ),
    (
        "Infrastructure",
        "Security, Authentication & Authorization",
        [
            "Token-Based Auth (JWT, PASETO, Session Management, Refresh Tokens)",
            "OAuth 2.0 & OpenID Connect (OIDC Authorization Flows)",
            "Access Control Models: ACL, RBAC, and ABAC",
            "Network Security: mTLS, TLS Termination, DDoS Mitigation, Vault / Secret Management",
        ],
    ),

    # --- Category: Tradeoffs ---
    (
        "Tradeoffs",
        "System Design Trade-offs & Sizing",
        [
            "Pull vs. Push Architectures",
            "Memory vs. Latency Trade-offs",
            "Throughput vs. Latency Trade-offs",
            "Consistency vs. Availability Trade-offs",
            "Latency vs. Accuracy (Approximate Counting, HyperLogLog)",
            "SQL vs. NoSQL vs. NewSQL Decision Matrix",
            "Cost-Aware Design & Resource Optimization",
        ],
    ),
]

SYSTEM_DESIGN_CASES = [
    "URL Shortener (TinyURL / Bitly)",
    "WhatsApp / Messenger Real-Time Chat System",
    "Notification System (Push, SMS, Email)",
    "Distributed File Storage (Dropbox / Google Drive / S3)",
    "Payment Processing & Order System (UPI / Stripe)",
    "Ride Booking & Driver Matching (Uber / Lyft)",
    "Distributed Log Ingestion & Analytics Pipeline",
    "Live Video Streaming Platform (Twitch / YouTube Live)",
    "Video Transcoding & Ingestion Pipeline (Netflix)",
    "Social Network News Feed & Timeline (Instagram / Twitter)",
    "Dating & Proximity Matching Platform (Tinder)",
    "Short Video Sharing & Recommendation Platform (TikTok / Reels)",
    "Online Coding Judge & Sandbox Execution (LeetCode)",
    "High-Concurrency Ticket / Train Reservation System (IRCTC / Ticketmaster)",
    "Food Delivery & Driver Dispatch Platform (DoorDash / Swiggy)",
    "E-Commerce Marketplace & Flash Sales (Amazon / Flipkart)",
    "Maps & Navigation Service (Google Maps)",
    "Scalable Email Service (Gmail)",
    "Collaborative Real-Time Document Editor (Google Docs / OT vs CRDT)",
    "Online Chess Engine & Matchmaking (Chess.com)",
    "Distributed Web Crawler & Indexer (Google Search)",
    "Typeahead / Autocomplete Search Suggestion System",
    "Distributed Key-Value Store (DynamoDB / Cassandra Style)",
    "Global Distributed Rate Limiter Service",
    "Enterprise RAG Document Chatbot & Knowledge Retrieval System",
    "Autonomous AI Agent Workflow Platform (LangGraph / MCP)",
    "Multi-Tenant SaaS Backend Architecture",
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
    existing_subs = db.query(SystemDesignSubConcept).all()
    sub_state = {}
    for s in existing_subs:
        sub_state[s.subconcept_name.lower().strip()] = {
            "status": s.status,
            "reading_done": s.reading_done,
            "practical_done": s.practical_done,
            "notes": s.notes or "",
            "resources": s.resources or "",
            "sources": s.sources or "",
        }

    # Clean and re-seed concepts & sub-concepts to apply new comprehensive curriculum
    db.query(SystemDesignSubConcept).delete()
    db.query(SystemDesignConcept).delete()
    db.commit()

    for i, (cat, concept_name, sub_list) in enumerate(SYSTEM_DESIGN_TOPICS):
        concept = SystemDesignConcept(category=cat, concept_name=concept_name, sources="", order_index=i + 1)
        db.add(concept)
        db.flush()
        for j, sub_name in enumerate(sub_list):
            prev = sub_state.get(sub_name.lower().strip(), {})
            if not prev:
                for k, v in sub_state.items():
                    if k in sub_name.lower() or sub_name.lower() in k:
                        prev = v
                        break
            db.add(SystemDesignSubConcept(
                concept_id=concept.id,
                subconcept_name=sub_name,
                order_index=j + 1,
                status=prev.get("status", "Not Started"),
                reading_done=prev.get("reading_done", False),
                practical_done=prev.get("practical_done", False),
                notes=prev.get("notes", ""),
                resources=prev.get("resources", ""),
                sources=prev.get("sources", ""),
            ))
    db.commit()

    # --- System Design Cases ---
    existing_cases = db.query(SystemDesignCase).all()
    case_state = {}
    for c in existing_cases:
        case_state[c.system_name.lower().strip()] = {
            "status": c.status,
            "key_components": c.key_components or "",
            "diagram_url": c.diagram_url or "",
            "notes": c.notes or "",
        }

    db.query(SystemDesignCase).delete()
    db.commit()

    for i, name in enumerate(SYSTEM_DESIGN_CASES):
        prev = case_state.get(name.lower().strip(), {})
        if not prev:
            for k, v in case_state.items():
                if k in name.lower() or name.lower() in k:
                    prev = v
                    break
        db.add(SystemDesignCase(
            system_name=name,
            order_index=i + 1,
            status=prev.get("status", "Not Started"),
            key_components=prev.get("key_components", ""),
            diagram_url=prev.get("diagram_url", ""),
            notes=prev.get("notes", ""),
        ))
    db.commit()

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
