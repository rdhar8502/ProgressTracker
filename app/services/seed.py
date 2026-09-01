"""
Seed script — populates the database with initial prep plan data.
Safe to run multiple times (checks for existing data first).
"""
import re
from datetime import date
from sqlalchemy.orm import Session

from app.models.user import UserProfile, SalaryTarget, WeeklySchedule
from app.models.destination import RelocationDestination
from app.models.dsa import DSATopic, DSAProblem, DSACompany
from app.models.system_design import SystemDesignConcept, SystemDesignSubConcept, SystemDesignCase
from app.models.ai_llm import AILLMTopic
from app.models.github import GithubProject, GithubTask
from app.models.database_track import DatabaseConcept, DatabaseItem, DatabaseChallenge
from app.services.week_utils import generate_weeks, week_target_hours
from app.services.dsa_seed_data import DSA_PROBLEMS_DATA, DSA_ALGORITHM_TOPICS, DSA_COMPANIES
from app.services.database_seed_data import DATABASE_TOPICS, DATABASE_CHALLENGES
from app.services.destination_seed_data import DESTINATIONS_DATA


START_DATE = date(2026, 8, 12)
END_DATE = date(2027, 3, 31)

DSA_TOPICS = [
    "Arrays and Strings",
    "HashMap / HashSet",
    "Two Pointers",
    "Sliding Window",
    "Sorting Algorithms",
    "Binary Search",
    "Stack / Monotonic Stack",
    "Queue / Deque",
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
    # ══════════════════════════════════════════════════════════════════════════
    # 🏛️ HIGH LEVEL DESIGN (HLD) — Distributed Systems & Architecture
    # ══════════════════════════════════════════════════════════════════════════
    (
        "HLD",
        "Fundamentals & Scale Estimation",
        "Basics & Scaling Fundamentals",
        [
            "What is System Design & 45-Min Interview Framework",
            "Horizontal vs. Vertical Scaling & Bottlenecks",
            "Capacity Estimation & Back-of-the-Envelope Calculations (QPS, Storage, Bandwidth)",
            "Latency Numbers Every Engineer Should Know (L1, RAM, SSD, Network, Cross-DC)",
            "High Availability (HA), Fault Tolerance & Single Point of Failure (SPOF)",
            "Concurrency, Thread Pools & OS Resource Management",
            "Thrashing & OS Memory Management",
        ],
    ),
    (
        "HLD",
        "Networking & Web Protocols",
        "Protocols & Network Stack",
        [
            "HTTP/1.1, HTTP/2, and HTTP/3 (QUIC Protocol)",
            "Internet TCP/IP Stack vs UDP (Handshake, Flow & Congestion Control)",
            "What Happens When You Enter google.com (DNS, Handshake, TLS)",
            "WebSockets & Server-Sent Events (SSE)",
            "Polling vs Long Polling vs WebSockets vs WebRTC",
            "RPC Architectures & Protocol Buffers (gRPC vs REST vs GraphQL)",
        ],
    ),
    (
        "HLD",
        "Traffic Management & Caching",
        "Load Balancing & Edge Routing",
        [
            "Load Balancing Algorithms (Round Robin, Least Connections, IP Hash)",
            "Layer 4 vs Layer 7 Load Balancing & SSL Termination",
            "Consistent Hashing & Virtual Nodes / Hash Ring",
            "Reverse Proxy vs Forward Proxy (Nginx / HAProxy / Envoy)",
            "API Gateway Architecture (Routing, Aggregation, Rate Limiting, Auth)",
            "DNS Load Balancing & Anycast Routing",
        ],
    ),
    (
        "HLD",
        "Traffic Management & Caching",
        "Caching Strategies & CDNs",
        [
            "Distributed In-Memory Caching (Redis vs Memcached Cluster)",
            "Content Delivery Networks (CDN) & Edge Caching (Push vs Pull)",
            "Cache Write Policies (Write-Through, Write-Around, Write-Back / Write-Behind)",
            "Cache Eviction & Replacement Policies (LRU, LFU, Segmented LRU, ARC, TTL)",
            "Cache Invalidation & Pitfalls (Cache Avalanche, Stampede, Penetration)",
        ],
    ),
    (
        "HLD",
        "Databases & Storage Engines",
        "Relational Databases (SQL & PostgreSQL)",
        [
            "RDBMS Fundamentals, ACID Properties & Normalization",
            "Database Index Mechanics (B-Tree, B+Tree, Composite, Hash)",
            "Transaction Isolation Levels (Read Uncommitted, Read Committed, Repeatable Read, Serializable)",
            "Query Optimization & EXPLAIN ANALYZE",
            "Database Connection Pooling (PgBouncer, SQLAlchemy Pool) & Read Replicas",
            "Database Migrations & Zero-Downtime Schema Evolution",
        ],
    ),
    (
        "HLD",
        "Databases & Storage Engines",
        "NoSQL & Specialized Storage",
        [
            "Key-Value & Document Stores (DynamoDB, MongoDB)",
            "Wide-Column & Columnar Stores (Cassandra, ClickHouse)",
            "Storage Engine Internals (LSM-Trees, SSTables, WAL vs B-Trees)",
            "Bloom Filters & Counting Bloom Filters",
            "Location-Based Databases & Spatial Indexing (Geohash, QuadTree, Google S2)",
            "Time-Series Databases (Gorilla Compression, InfluxDB, TimescaleDB)",
            "Vector Search & Vector Databases (pgvector, Milvus, HNSW)",
            "Distributed Object Storage (S3 Architecture, Multipart Uploads, Blob Store)",
        ],
    ),
    (
        "HLD",
        "Asynchronous & Event Streaming",
        "Message Queues & Event Streaming",
        [
            "Message Queues (RabbitMQ, AWS SQS)",
            "Event Streaming & Distributed Log (Apache Kafka Architecture, Partitions, Offsets)",
            "Publisher-Subscriber (Pub/Sub) Model & Consumer Groups",
            "Event-Driven Architecture & Event Sourcing",
            "Database as a Message Queue Anti-Pattern & Transactional Outbox Pattern",
            "Task Queues & Asynchronous Workers (Celery, BullMQ, Temporal Orchestration)",
            "Batch Processing vs Stream Processing (Apache Spark, Apache Flink)",
        ],
    ),
    (
        "HLD",
        "Distributed Systems & Consensus",
        "Distributed Consistency & Theorems",
        [
            "CAP Theorem & PACELC Theorem in Practice",
            "Data Consistency Models (Strong / Linearizability, Causal, Eventual Consistency)",
            "Optimistic Concurrency Control (OCC) vs Pessimistic Locking",
            "Vector Clocks, Lamport Timestamps & Conflict Resolution",
        ],
    ),
    (
        "HLD",
        "Distributed Systems & Consensus",
        "Distributed Transactions & Consensus",
        [
            "Two-Phase Commit (2PC) & Three-Phase Commit (3PC)",
            "Saga Pattern (Choreography vs Orchestration)",
            "Distributed Consensus Protocols (Raft, Paxos, Multi-Paxos)",
            "Distributed Locking (Redis Redlock, ZooKeeper, etcd)",
            "Quorum Reads & Writes (Leaderless Dynamo-style Replication)",
        ],
    ),
    (
        "HLD",
        "Distributed Systems & Consensus",
        "Scalability & Data Partitioning",
        [
            "Master-Slave (Leader-Follower) Replication & Read Replicas",
            "Multi-Leader Replication & Conflict Handling",
            "Database Sharding Strategies (Range, Hash, Directory-Based)",
            "Cross-Shard Transactions, Joins & Resharding",
        ],
    ),
    (
        "HLD",
        "Reliability & Microservices",
        "Reliability, Fault Tolerance & Resiliency",
        [
            "Circuit Breaker Pattern & Fallback Mechanisms",
            "Retry Strategies with Exponential Backoff & Jitter",
            "Bulkhead Pattern & Cascading Failure Prevention",
            "Dead Letter Queues (DLQ) & Poison Message Handling",
            "Graceful Degradation & Load Shedding",
            "Distributed Rate Limiting (Token Bucket, Leaky Bucket, Redis Lua)",
        ],
    ),
    (
        "HLD",
        "Reliability & Microservices",
        "Observability, SRE & Microservices",
        [
            "Three Pillars of Observability: Logs, Metrics, Traces",
            "Distributed Tracing (OpenTelemetry, Jaeger)",
            "Metrics Collection & Dashboards (Prometheus, Grafana)",
            "Centralized Structured Logging (ELK / EFK / Vector)",
            "Anomaly Detection, Alerting & SLO / SLA / SLI Tracking",
            "Microservices vs Monoliths & Strangler Fig Pattern",
            "Service Mesh & Sidecar Pattern (Envoy, Istio)",
        ],
    ),
    (
        "HLD",
        "Security & Tradeoffs",
        "Security, Auth & Architectural Trade-offs",
        [
            "Token-Based Auth (JWT, PASETO, Session Management, Refresh Tokens)",
            "OAuth 2.0 & OpenID Connect (OIDC Authorization Flows)",
            "Access Control Models: ACL, RBAC, and ABAC",
            "Network Security: mTLS, TLS Termination, DDoS Mitigation, Vault Secret Management",
            "Pull vs. Push Architectures & Sizing Trade-offs",
            "Consistency vs. Availability Trade-offs & SQL vs. NoSQL Decision Matrix",
        ],
    ),
    (
        "HLD",
        "Compliance & Regulatory Standards",
        "Healthcare Compliance — HIPAA, PHI & HL7/FHIR",
        [
            "HIPAA Overview — Protected Health Information (PHI) & Covered Entities",
            "PHI vs. PII: What counts as sensitive health data (18 HIPAA identifiers)",
            "HIPAA Technical Safeguards: Encryption at Rest & In Transit, Audit Logs, MFA",
            "HIPAA Administrative Safeguards: BAA Agreements, Role-Based Access, Training",
            "HL7 & FHIR — Healthcare Data Interchange Standards & API Design",
            "De-identification & Anonymization Strategies for Healthcare Data",
            "Who Uses HIPAA: Hospitals, Health Insurers, EHR Vendors, Telehealth Platforms",
        ],
    ),
    (
        "HLD",
        "Compliance & Regulatory Standards",
        "Financial & Payment Compliance — PCI-DSS, SOX & SOC 2",
        [
            "PCI-DSS Overview — Payment Card Industry Data Security Standard (Levels 1–4)",
            "Cardholder Data Environment (CDE): Segmentation, Tokenization & Vaulting",
            "SOC 2 Type I vs Type II — Trust Service Criteria (Security, Availability, Confidentiality)",
            "SOX Compliance (Sarbanes-Oxley) — Audit Trails & Financial Data Integrity",
            "Who Uses PCI-DSS: Payment Gateways (Stripe, PayPal), Banks, E-Commerce Platforms",
            "Who Uses SOC 2: SaaS Companies, Cloud Providers, B2B Software (AWS, Salesforce)",
        ],
    ),
    (
        "HLD",
        "Compliance & Regulatory Standards",
        "Privacy Regulations — GDPR, CCPA & Data Sovereignty",
        [
            "GDPR Core Principles: Lawful Basis, Data Minimization, Right to Be Forgotten",
            "GDPR Technical Requirements: Consent Management, Data Portability APIs, DPO",
            "CCPA vs. GDPR: Key Differences & Overlapping Requirements",
            "Data Residency & Data Sovereignty: Multi-region Architecture Constraints",
            "Privacy by Design & Privacy by Default Principles in System Architecture",
            "Who Must Comply with GDPR: Any company serving EU users regardless of location",
            "Cookie Consent Management, Audit Logs & Breach Notification Timelines (72h GDPR)",
        ],
    ),
    (
        "HLD",
        "Compliance & Regulatory Standards",
        "Cloud & Infrastructure Compliance — FedRAMP, ISO 27001 & NIST",
        [
            "FedRAMP Authorization Levels (Low, Moderate, High) — US Government Cloud Contracts",
            "ISO 27001 — Information Security Management System (ISMS) Certification",
            "NIST Cybersecurity Framework (CSF) — Identify, Protect, Detect, Respond, Recover",
            "NIST SP 800-53 Security Controls — Used by Government & Defense Contractors",
            "Who Uses FedRAMP: AWS GovCloud, Azure Government, Google Public Sector",
            "CIS Benchmarks — Security Configuration Baselines for Cloud & OS Hardening",
        ],
    ),
    (
        "HLD",
        "Organization Types & Design Focus",
        "Healthcare Tech — System Design Priorities",
        [
            "Primary HLD Focus: High Availability (99.999% uptime for critical systems), HIPAA compliance",
            "EHR Systems: Event Sourcing, Immutable Audit Logs, FHIR REST APIs",
            "Medical Imaging: Object Storage (DICOM files), CDN for radiology image delivery",
            "Telehealth Platforms: WebRTC for video, HIPAA-compliant messaging, low-latency signaling",
            "Hospital Operations: Real-time IoT (vitals monitors), HL7 message queues, alerting",
            "LLD Focus: Strategy Pattern for billing rules, Observer for patient alerts, State for patient admission lifecycle",
            "Companies: Epic Systems, Cerner, Veeva, Philips Healthcare, Apple Health, Amazon HealthLake",
        ],
    ),
    (
        "HLD",
        "Organization Types & Design Focus",
        "Fintech & Banking — System Design Priorities",
        [
            "Primary HLD Focus: Strong Consistency (ACID transactions), PCI-DSS, SOC 2, SOX compliance",
            "Payment Processing: Idempotent APIs, Distributed Sagas, Two-Phase Commit (2PC), Outbox Pattern",
            "Core Banking: Event Sourcing for ledger (immutable transaction log), CQRS read models",
            "Fraud Detection: Real-time stream processing (Kafka + Flink), ML scoring, anomaly detection",
            "High-Frequency Trading (HFT): Ultra-low latency (sub-millisecond), co-location, lock-free data structures",
            "LLD Focus: Strategy for fee calculation, State for loan lifecycle, Observer for account alerts",
            "Companies: Stripe, Plaid, Goldman Sachs, JPMorgan, Revolut, Robinhood, Square",
        ],
    ),
    (
        "HLD",
        "Organization Types & Design Focus",
        "E-Commerce & Retail — System Design Priorities",
        [
            "Primary HLD Focus: High read throughput, flash sale scalability, eventual consistency acceptable",
            "Product Catalog: Read-heavy, aggressive caching (Redis, CDN), Elasticsearch for search",
            "Inventory Management: Distributed locking for stock deductions, optimistic vs pessimistic locking",
            "Order Management: Saga pattern for distributed transactions (Payment → Inventory → Shipping)",
            "Recommendation Engine: Collaborative filtering, real-time clickstream processing (Kafka)",
            "Flash Sales / Black Friday: Queue-based load leveling, token bucket rate limiting, pre-warming",
            "LLD Focus: Strategy for discount rules, Decorator for pricing tiers, Observer for order status events",
            "Companies: Amazon, Shopify, Flipkart, Walmart, Instacart, DoorDash",
        ],
    ),
    (
        "HLD",
        "Organization Types & Design Focus",
        "Social Media & Content Platforms — System Design Priorities",
        [
            "Primary HLD Focus: Massive write & read scale, feed generation, media ingestion pipelines",
            "News Feed / Timeline: Fan-out on write (celebrity problem) vs Fan-out on read, hybrid approach",
            "Media Storage & Delivery: Object storage (S3), transcoding pipelines (FFmpeg workers), multi-CDN",
            "Notifications: Push notifications at scale (APNs, FCM), WebSocket long-polling, SSE",
            "Content Moderation: Async ML pipelines, human review queues, appeal workflows",
            "LLD Focus: Observer for feed updates, Strategy for ranking algorithms, Composite for post types",
            "Companies: Meta (Facebook/Instagram), Twitter/X, TikTok, Snapchat, YouTube, Reddit, LinkedIn",
        ],
    ),
    (
        "HLD",
        "Organization Types & Design Focus",
        "Ride-sharing, Delivery & Location-Tech — System Design Priorities",
        [
            "Primary HLD Focus: Real-time geospatial matching, GPS tracking at scale, dynamic pricing",
            "Driver/Rider Matching: Geohashing, QuadTree / H3 spatial indexing, proximity search",
            "Real-time Location Tracking: WebSockets / MQTT for live updates, Redis Geo for driver positions",
            "Dynamic Pricing (Surge): Real-time supply/demand computation, Kafka for event streaming",
            "Route Optimization: Graph algorithms (Dijkstra, A*), pre-computed turn-by-turn caching",
            "LLD Focus: Strategy for surge pricing, State for trip lifecycle (Requested→Matched→InProgress→Completed), Observer for driver location",
            "Companies: Uber, Lyft, DoorDash, Instacart, Grab, Zomato, Ola",
        ],
    ),
    (
        "HLD",
        "Organization Types & Design Focus",
        "Cloud Providers, SaaS & Enterprise Infra — System Design Priorities",
        [
            "Primary HLD Focus: Multi-tenancy, SLA guarantees (99.99%), auto-scaling, global distribution",
            "Multi-tenant Architecture: Silo vs Pool vs Bridge models, tenant isolation, noisy neighbor prevention",
            "Managed Services Design: Control Plane vs Data Plane separation, rate limiting per tenant",
            "Global Distribution: Multi-region active-active, data residency compliance, latency-based routing",
            "Observability Platform: Distributed tracing (OpenTelemetry), centralized logging, SLO/SLI alerting",
            "LLD Focus: Factory for resource provisioning, Strategy for billing tiers, Decorator for feature flags",
            "Companies: AWS, Google Cloud, Azure, Salesforce, Snowflake, Datadog, PagerDuty",
        ],
    ),

    # ══════════════════════════════════════════════════════════════════════════
    # ⚙️ LOW LEVEL DESIGN (LLD / OOD) — Object Oriented Design & Machine Coding
    # ══════════════════════════════════════════════════════════════════════════
    (
        "LLD",
        "OOP & SOLID Principles",
        "Object-Oriented Programming Fundamentals",
        [
            "4 Pillars of OOP (Encapsulation, Abstraction, Inheritance, Polymorphism)",
            "Composition vs. Inheritance (Has-A vs. Is-A Trade-offs)",
            "Static vs. Dynamic Polymorphism (Method Overloading vs. Overriding)",
            "Abstract Classes vs. Interfaces & Pure Virtual Contracts",
            "Coupling vs. Cohesion in Software Architecture",
        ],
    ),
    (
        "LLD",
        "OOP & SOLID Principles",
        "SOLID Principles in Practice",
        [
            "Single Responsibility Principle (SRP) — Violations & Refactoring",
            "Open-Closed Principle (OCP) — Extension via Interfaces & Polymorphism",
            "Liskov Substitution Principle (LSP) — Contract & Invariant Preservation",
            "Interface Segregation Principle (ISP) — Role Interfaces vs Fat Interfaces",
            "Dependency Inversion Principle (DIP) & Inversion of Control (IoC Containers)",
        ],
    ),
    (
        "LLD",
        "OOP & SOLID Principles",
        "Clean Code & Object Modeling",
        [
            "DRY (Don't Repeat Yourself), KISS & YAGNI Principles",
            "Law of Demeter (Principle of Least Knowledge)",
            "Tell, Don't Ask Principle & Defensive Programming",
            "Code Smells Identification & Refactoring Strategies",
        ],
    ),
    (
        "LLD",
        "Design Patterns (GoF)",
        "Creational Design Patterns",
        [
            "Singleton Pattern (Thread-Safe, Double-Checked Locking, Enum / Eager)",
            "Factory Method Pattern (Decoupling Object Creation from Usage)",
            "Abstract Factory Pattern (Families of Related Objects)",
            "Builder Pattern (Step-by-Step Construction & Method Chaining)",
            "Prototype Pattern (Object Cloning & Deep vs Shallow Copy)",
            "Object Pool Pattern (Connection & Thread Resource Reuse)",
        ],
    ),
    (
        "LLD",
        "Design Patterns (GoF)",
        "Structural Design Patterns",
        [
            "Adapter Pattern (Interface Compatibility & Wrapper Layer)",
            "Decorator Pattern (Dynamic Behavior Extension without Subclassing)",
            "Facade Pattern (Simplified Unified Interface for Complex Subsystems)",
            "Composite Pattern (Tree Structures & Uniform Object Hierarchy)",
            "Proxy Pattern (Virtual, Protection, Caching & Remote Proxies)",
            "Bridge Pattern (Decoupling Abstraction from Implementation)",
            "Flyweight Pattern (Fine-Grained Memory Optimization)",
        ],
    ),
    (
        "LLD",
        "Design Patterns (GoF)",
        "Behavioral Design Patterns",
        [
            "Strategy Pattern (Interchangeable Algorithms & Policy Injection)",
            "Observer Pattern (Event Listeners, Pub/Sub & Notification Engine)",
            "Command Pattern (Encapsulating Requests, Undo/Redo, Macro Execution)",
            "State Pattern (Finite State Machines & State Context Transitions)",
            "Chain of Responsibility Pattern (Request Handlers, Middlewares, Filters)",
            "Template Method Pattern (Algorithm Skeletons with Invariant Steps)",
            "Iterator Pattern (Collection Traversal Decoupling)",
            "Mediator Pattern (Centralized Inter-Object Communication)",
            "Memento Pattern (State Snapshots & Rollback Mechanisms)",
            "Visitor Pattern (Separating Operations from Object Data Structures)",
        ],
    ),
    (
        "LLD",
        "Concurrency & Low-Level Systems",
        "Multi-Threading & Concurrency Primitives",
        [
            "Thread Lifecycle, Mutexes & Reentrant Locks",
            "Semaphores, CountdownLatches & CyclicBarriers",
            "Read-Write Locks (Shared vs Exclusive Access)",
            "Atomic Variables, Memory Barriers & Compare-And-Swap (CAS)",
            "Thread Pools, ExecutorService & Async Worker Queues",
        ],
    ),
    (
        "LLD",
        "Concurrency & Low-Level Systems",
        "Concurrent Design Patterns & Safety",
        [
            "Producer-Consumer Pattern with Thread-Safe Blocking Queue",
            "ThreadLocal Storage & Context Propagation",
            "Deadlock Detection, Prevention & Lock Ordering Strategies",
            "Double-Checked Locking & Safe Lazy Initialization",
        ],
    ),
    (
        "LLD",
        "UML & Schema Modeling",
        "UML & Class Diagram Modeling",
        [
            "Class Diagrams (Associations, Aggregations, Compositions, Dependencies)",
            "Sequence Diagrams (Lifelines, Sync vs Async Message Flow)",
            "State Transition Diagrams (State Machine Modeling)",
            "Entity-Relationship (ER) Modeling & Table Schemas for LLD",
        ],
    ),

    # ══════════════════════════════════════════════════════════════════════════
    # 🤖 AI SYSTEM DESIGN (AI SD) — Modern AI/LLM Architectures & Production
    # ══════════════════════════════════════════════════════════════════════════
    (
        "AI",
        "RAG & Vector Architecture",
        "Enterprise RAG & Hybrid Retrieval Pipelines",
        [
            "Chunking Strategies (Fixed-size, Recursive Character, Semantic Chunking, Sliding Window)",
            "Dense vs. Sparse Embeddings & Hybrid Search (BM25 + Vector via Reciprocal Rank Fusion / RRF)",
            "Vector Database Internals & Indexing (HNSW, IVFFlat, Product Quantization, pgvector vs Milvus)",
            "Two-Stage Retrieval & Cross-Encoder Reranking (Cohere Rerank, BGE-Reranker, ColBERT)",
            "Metadata Filtering & Multi-Tenant Role-Based Access Control (RBAC) in Vector Search",
            "Context Window Compression, Lost-in-the-Middle Mitigation & Dynamic Context Pruning",
            "Corrective RAG (CRAG) & Self-RAG (Retrieval Quality Gating, Active Retrieval Verification)",
            "Document Ingestion Pipelines: Asynchronous Parsing, OCR (Docling / Unstructured) & Deduplication",
        ],
    ),
    (
        "AI",
        "Agentic Systems & Orchestration",
        "Autonomous Agent Workflows & State Machines",
        [
            "Agent Frameworks & Topologies (ReAct Loop, Plan-and-Solve, Supervisor-Worker, Multi-Agent Swarms)",
            "State Machines & Cyclic Workflows (LangGraph StateGraph vs Temporal vs LlamaIndex Workflows)",
            "Function Calling & Tool Orchestration (Dynamic Schema Injection, JSON Mode, Tool Error Recovery)",
            "Model Context Protocol (MCP) Architecture (Client-Host-Server Topology, Tool & Resource Discovery)",
            "Agent Memory Architectures (Short-Term Buffer, Summary Memory, Episodic & Long-Term Vector Memory)",
            "State Persistence, Checkpointing & Time-Travel Debugging (SQLite / PostgreSQL Checkpointers)",
            "Human-in-the-Loop (HITL) Approval Gateways for Critical, Financial or Destructive Tool Execution",
            "Multi-Agent Coordination: Message Bus, Distributed Consensus & Hand-off Protocols",
        ],
    ),
    (
        "AI",
        "AI Model Serving & Inference",
        "LLM Inference Optimization, Streaming & Gateway Routing",
        [
            "Streaming Response Architecture (Server-Sent Events / SSE vs WebSockets for Token Streaming)",
            "Time to First Token (TTFT) vs Inter-Token Latency (ITL) Optimization & Profiling",
            "Prompt Caching Architectures (KV-Cache Reuse, Semantic Prompt Caching via Redis / GPTCache)",
            "Model Routing & Cascade Architecture (Fast SLMs for Triage -> Heavy Frontier LLMs for Complex Reasoning)",
            "Batching Strategies (Continuous / Dynamic Batching, vLLM / TGI Engines, PagedAttention)",
            "Asynchronous Background Job Queues & Rate Limiting for High-Volume LLM Pipelines",
            "Structured Output Enforcement (Outlines, Jsonformer, Instructor, Regex & Pydantic Constrained Decoding)",
            "Speculative Decoding & Model Quantization (AWQ, GPTQ, INT8/INT4 Serving Trade-offs)",
        ],
    ),
    (
        "AI",
        "AI Observability & Evaluation",
        "Continuous Evaluation, LLM-as-Judge & Tracing",
        [
            "The RAG Triad Evaluation (Faithfulness, Answer Relevance, Context Precision using Ragas / TruLens)",
            "LLM-as-a-Judge Design Patterns (G-Eval, Reference-Free vs Reference-Based Scoring, Position Bias Mitigation)",
            "Distributed Tracing for LLM Calls (OpenTelemetry Spans, Phoenix, LangSmith, Arize)",
            "Telemetry & Cost Tracking (Token Usage per Tenant / Model, Prompt vs Completion Cost Dashboards)",
            "Continuous CI/CD Evaluation Gating & Regression Detection for AI Pipelines",
            "Deterministic Fallback Cascades & Circuit Breakers on LLM Outages or Provider Rate Limits",
            "Synthetic Dataset Generation for Domain-Specific Evaluation Suites",
        ],
    ),
    (
        "AI",
        "AI Security, Safety & Guardrails",
        "Jailbreak Defense, PII Masking & Sandboxed Tool Execution",
        [
            "Prompt Injection & Jailbreak Defenses (Direct vs Indirect Injection, Canary Tokens, Input Sanitizers)",
            "Guardrail Architectures (NeMo Guardrails, Llama Guard, Content Safety Classifiers)",
            "Data Leakage & PII Masking / Anonymization before LLM Transmission (Presidio, Tokenization)",
            "Insecure Tool Calling & Sandboxed Execution (Docker, gVisor, WebAssembly, Ephemeral Python Containers)",
            "Hallucination Detection, Fact-Checking Pipelines & Grounding Verifiers",
            "EU AI Act & Compliance Constraints (Risk-Based Classification, Model Transparency, Audit Logs)",
        ],
    ),
    (
        "AI",
        "Multimodal & Real-Time AI",
        "Live Audio/Video Streaming Pipelines & Latency Budgets",
        [
            "Real-Time Multimodal Architecture (WebSockets / WebRTC Audio Streaming with Silence Detection)",
            "Voice Activity Detection (VAD) & Low-Latency Streaming Speech-to-Text (Whisper Live)",
            "Streaming Text-to-Speech (TTS) Chunking & Audio Buffer Management",
            "End-to-End Voice Roundtrip Latency Budget Breakdown (<500ms Human Conversation Target)",
            "Visual Document Processing & Visual Question Answering (VQA) Ingestion Pipelines",
        ],
    ),
]

SYSTEM_DESIGN_CASES = [
    # ── High Level Design (HLD) Distributed Systems ──
    {
        "track": "HLD",
        "category": "Distributed Systems",
        "system_name": "URL Shortener (TinyURL / Bitly)",
        "key_components": "Base62 Encoding, KGS (Key Generation Service), Redis Cache, SQL Sharding, 301 vs 302 Redirects",
    },
    {
        "track": "HLD",
        "category": "Communication & Messaging",
        "system_name": "WhatsApp / Messenger Real-Time Chat System",
        "key_components": "WebSockets, Gateway Servers, Message Service, Cassandra Message Store, Redis Pub/Sub, Push Notifications",
    },
    {
        "track": "HLD",
        "category": "Infrastructure & Microservices",
        "system_name": "Notification System (Push, SMS, Email)",
        "key_components": "Notification API, Priority Kafka Queues, Worker Fleet, 3rd Party Gateways (APNS, FCM, Twilio), Rate Limiter",
    },
    {
        "track": "HLD",
        "category": "Storage & File Systems",
        "system_name": "Distributed File Storage (Dropbox / Google Drive / S3)",
        "key_components": "Block Server, Chunking Engine (4MB chunks), Deduplication (SHA-256), Metadata DB, S3 Storage, Sync Service",
    },
    {
        "track": "HLD",
        "category": "Fintech & Payments",
        "system_name": "Payment Processing & Order System (UPI / Stripe)",
        "key_components": "Double-Entry Ledger, Idempotency Keys, Payment Gateway Integrations, 2PC/Saga Orchestration, Reconciliation",
    },
    {
        "track": "HLD",
        "category": "Geospatial & Mobility",
        "system_name": "Ride Booking & Driver Matching (Uber / Lyft)",
        "key_components": "Geohashing / Google S2, Driver Location Ingestion (WebSockets), Matching Engine, Surge Pricing, Trip Lifecycle State Machine",
    },
    {
        "track": "HLD",
        "category": "Big Data & Streaming",
        "system_name": "Distributed Log Ingestion & Analytics Pipeline",
        "key_components": "Log Agents, Kafka Distributed Buffer, Flink Stream Processing, ClickHouse / Elasticsearch, Grafana Dashboards",
    },
    {
        "track": "HLD",
        "category": "Streaming & Media",
        "system_name": "Live Video Streaming Platform (Twitch / YouTube Live)",
        "key_components": "RTMP/WebRTC Ingestion, Transcoder Cluster, Low-Latency HLS (LL-HLS), Edge CDN Mesh, Live Chat Sharding",
    },
    {
        "track": "HLD",
        "category": "Streaming & Media",
        "system_name": "Video Transcoding & Ingestion Pipeline (Netflix)",
        "key_components": "Chunk Splitter, Async Task Queue, GPU Transcoding Cluster, Adaptive Bitrate Manifest (DASH/HLS), CDN Pre-warming",
    },
    {
        "track": "HLD",
        "category": "Social & Feed Architecture",
        "system_name": "Social Network News Feed & Timeline (Instagram / Twitter)",
        "key_components": "Fanout-on-Write vs Fanout-on-Read, Celebrity Invalidation, Redis Sorted Sets, Feed Aggregator, Ranking Service",
    },
    {
        "track": "HLD",
        "category": "Geospatial & Social",
        "system_name": "Dating & Proximity Matching Platform (Tinder)",
        "key_components": "Geohash Location Clusters, Recommendation Engine, Swipe Processing Queue, Mutual Match Notification Service",
    },
    {
        "track": "HLD",
        "category": "Streaming & AI",
        "system_name": "Short Video Sharing & Recommendation Platform (TikTok / Reels)",
        "key_components": "Video Upload Pipeline, Recommendation Model Scoring, CDN Edge Delivery, User Engagement Event Stream",
    },
    {
        "track": "HLD",
        "category": "Compute & Sandboxing",
        "system_name": "Online Coding Judge & Sandbox Execution (LeetCode)",
        "key_components": "Docker/cgroups Sandbox, Task Dispatcher, Worker Daemon, Resource Throttler, Result Aggregator",
    },
    {
        "track": "HLD",
        "category": "High Concurrency & Ticketing",
        "system_name": "High-Concurrency Ticket / Train Reservation System (IRCTC / Ticketmaster)",
        "key_components": "Seat Inventory Cache, Redis Temporary Hold (10-min TTL), Fair Queueing with Kafka, Transactional DB Lock",
    },
    {
        "track": "HLD",
        "category": "E-Commerce & Logistics",
        "system_name": "Food Delivery & Driver Dispatch Platform (DoorDash / Swiggy)",
        "key_components": "Restaurant Catalog, Order State Machine, Geospatial Driver Dispatcher, Live GPS WebSocket Tracker",
    },
    {
        "track": "HLD",
        "category": "E-Commerce & Logistics",
        "system_name": "E-Commerce Marketplace & Flash Sales (Amazon / Flipkart)",
        "key_components": "Catalog Service, Redis Inventory Pre-allocation, Optimistic Concurrency Control, Asynchronous Order Checkout Queue",
    },
    {
        "track": "HLD",
        "category": "Geospatial & Mobility",
        "system_name": "Maps & Navigation Service (Google Maps)",
        "key_components": "Graph Road Network, Dijkstra / A* Routing Engine, Real-time Traffic Ingestion, Tile Vector Rendering",
    },
    {
        "track": "HLD",
        "category": "Communication & Messaging",
        "system_name": "Scalable Email Service (Gmail)",
        "key_components": "SMTP Receiving Gateway, Distributed Mailbox Store, Inverted Search Index (Elasticsearch), Spam Filter Pipeline",
    },
    {
        "track": "HLD",
        "category": "Collaboration & Real-Time",
        "system_name": "Collaborative Real-Time Document Editor (Google Docs / OT vs CRDT)",
        "key_components": "Operational Transformation (OT) / CRDTs, WebSocket Event Stream, Snapshot Service, Document Version History",
    },
    {
        "track": "HLD",
        "category": "Search & Web Systems",
        "system_name": "Distributed Web Crawler & Indexer (Google Search)",
        "key_components": "URL Frontier (Kafka/Redis), Politeness Manager, HTML Parser, Content Deduplication, Inverted Index Builder",
    },
    {
        "track": "HLD",
        "category": "Search & Web Systems",
        "system_name": "Typeahead / Autocomplete Search Suggestion System",
        "key_components": "Trie Data Structure, Top-K Aggregations, Redis Distributed Cache, Frequency Aggregator Pipeline",
    },
    {
        "track": "HLD",
        "category": "Storage & Databases",
        "system_name": "Distributed Key-Value Store (DynamoDB / Cassandra Style)",
        "key_components": "Consistent Hashing, Quorum Consensus (R+W>N), Vector Clocks, Gossip Protocol, LSM-Tree Storage Engine",
    },
    {
        "track": "HLD",
        "category": "Infrastructure & Security",
        "system_name": "Global Distributed Rate Limiter Service",
        "key_components": "Token Bucket & Sliding Window Log, Redis Lua Scripts, Local Memory Cache, Fallback Bypass Circuit",
    },
    {
        "track": "HLD",
        "category": "AI & Knowledge Systems",
        "system_name": "Enterprise RAG Document Chatbot & Knowledge Retrieval System",
        "key_components": "Document Chunking Pipeline, pgvector / Milvus Vector Store, Hybrid Keyword + Semantic Search, Cohere Reranker",
    },
    {
        "track": "HLD",
        "category": "AI & Knowledge Systems",
        "system_name": "Autonomous AI Agent Workflow Platform (LangGraph / MCP)",
        "key_components": "State Machine Engine, Persistent SQLite Checkpointer, MCP Tool Registry, Human-in-the-Loop Gateway",
    },
    {
        "track": "HLD",
        "category": "Infrastructure & Microservices",
        "system_name": "Multi-Tenant SaaS Backend Architecture",
        "key_components": "Tenant Subdomain Routing, Row-Level Security vs Dynamic Schema Isolation, Redis Per-Tenant Rate Limiting",
    },

    # ── Low Level Design (LLD / Machine Coding) Problems ──
    {
        "track": "LLD",
        "category": "Machine Coding & Object Design",
        "system_name": "Design Parking Lot System",
        "key_components": "Strategy Pattern for Pricing, Vehicle Polymorphism (Bike/Car/Truck), Multi-Floor Spot Allocation, Entry/Exit Gate Controllers",
    },
    {
        "track": "LLD",
        "category": "Machine Coding & Object Design",
        "system_name": "Design In-Memory Cache with Eviction Policies (LRU / LFU / TTL)",
        "key_components": "Doubly Linked List + HashMap, Min-Heap for LFU, ReadWriteLock Thread-Safety, Generic Key-Value Storage",
    },
    {
        "track": "LLD",
        "category": "Machine Coding & Object Design",
        "system_name": "Design Splitwise (Expense Sharing App)",
        "key_components": "Strategy Pattern (Equal, Exact, Percentage Splits), User Graph, Minimum Cash Flow Simplification Algorithm",
    },
    {
        "track": "LLD",
        "category": "Machine Coding & Object Design",
        "system_name": "Design Elevator Management System",
        "key_components": "State Pattern (Idle, MovingUp, MovingDown), SCAN/LOOK Scheduling Algorithm, Dispatcher Strategy, Multi-Car Controller",
    },
    {
        "track": "LLD",
        "category": "Machine Coding & Object Design",
        "system_name": "Design Rate Limiter Library",
        "key_components": "Strategy Pattern (Token Bucket, Leaky Bucket, Sliding Window Log), Atomic Variables & Mutex Concurrency Safety",
    },
    {
        "track": "LLD",
        "category": "Machine Coding & Object Design",
        "system_name": "Design Logging Framework (Log4j Style)",
        "key_components": "Singleton Logger, Chain of Responsibility for Log Levels (DEBUG/INFO/ERROR), Strategy for Appenders (Console/File), Async Buffer",
    },
    {
        "track": "LLD",
        "category": "Machine Coding & Object Design",
        "system_name": "Design Movie Ticket Booking System (BookMyShow)",
        "key_components": "Cinema/Hall/Screen Hierarchy, Seat Locking with TTL, Payment Gateway Adapter, Concurrency-Safe Booking Transactions",
    },
    {
        "track": "LLD",
        "category": "Machine Coding & Object Design",
        "system_name": "Design Snake and Ladder Board Game",
        "key_components": "Board & Cell Entities, Dice Roll Strategy, Jumper Interface (Snake/Ladder), Turn-based Game Loop Controller",
    },
    {
        "track": "LLD",
        "category": "Machine Coding & Object Design",
        "system_name": "Design Pub-Sub Message Broker / Event Bus",
        "key_components": "Topic, Subscription, Observer Pattern, Broadcast vs Consumer Group Routing, ThreadPool Worker Queue",
    },
    {
        "track": "LLD",
        "category": "Machine Coding & Object Design",
        "system_name": "Design Chess Game / Tic-Tac-Toe",
        "key_components": "Board Model, Piece Movement Rules (Polymorphism), Move Validator, Game Loop, Check/Checkmate Engine",
    },
    {
        "track": "LLD",
        "category": "Machine Coding & Object Design",
        "system_name": "Design Food Delivery / Order Management System",
        "key_components": "State Pattern for Order Status, Cart Price Calculation Decorator, Restaurant/Menu Model, Rider Assignment Strategy",
    },
    {
        "track": "LLD",
        "category": "Machine Coding & Object Design",
        "system_name": "Design ATM / Vending Machine",
        "key_components": "State Pattern (Idle, CardInserted, PinVerified, Dispensing), Chain of Responsibility for Cash Dispense ($100, $50, $20)",
    },
    {
        "track": "LLD",
        "category": "Machine Coding & Object Design",
        "system_name": "Design Notification Dispatcher Library",
        "key_components": "Adapter Pattern for Channels (Email, SMS, Push), Observer Pattern, Bulk Dispatcher, Retry & Rate Limit Decorators",
    },
    {
        "track": "LLD",
        "category": "Machine Coding & Object Design",
        "system_name": "Design File System & Directory Tree",
        "key_components": "Composite Pattern (File vs Directory), Command Pattern for Operations, Visitor Pattern for Size Calculation & Search",
    },
    {
        "track": "LLD",
        "category": "Machine Coding & Object Design",
        "system_name": "Design Online Shopping Cart & Coupon Engine",
        "key_components": "Decorator / Strategy Pattern for Discount Rules, Tax Calculator, Item Model, Inventory Reservation Lock",
    },
    {
        "track": "LLD",
        "category": "Machine Coding & Object Design",
        "system_name": "Design Meeting Scheduler / Calendar",
        "key_components": "Room Booking Model, Interval Tree / Overlap Checker, Recurring Event Builder, Invitation Dispatcher",
    },
    {
        "track": "LLD",
        "category": "Machine Coding & Object Design",
        "system_name": "Design Live Cricket Scoreboard (Cricinfo)",
        "key_components": "Observer Pattern for Live Ball Updates, Innings/Match State Machine, Player Statistics Aggregator, Commentary Stream",
    },
    {
        "track": "LLD",
        "category": "Machine Coding & Object Design",
        "system_name": "Design Ride Booking Application (Uber LLD)",
        "key_components": "Driver Matching Strategy, Fare Estimation Strategy, Trip State Machine, Rating System, Payment Adapter",
    },

    # ── AI System Design (AI SD) Case Studies & Real-World Questions ──
    {
        "track": "AI",
        "category": "Enterprise AI & RAG",
        "system_name": "Design Enterprise Multi-Tenant RAG Platform with RBAC",
        "key_components": "Document Ingestion Pipeline, Chunking Engine, pgvector / Milvus, Hybrid Search (BM25 + Dense Vectors via RRF), Cohere Reranker, Tenant-Isolated RBAC Filtering, Verifiable Citations",
    },
    {
        "track": "AI",
        "category": "Agentic Systems",
        "system_name": "Design Autonomous Customer Support & Remediation Agent",
        "key_components": "LangGraph Cyclic State Machine, MCP Tool Integrations, PostgreSQL Checkpointer, Sentiment Analyzer, Human-in-the-Loop Escalation Gateway, Distributed Rate Limiter",
    },
    {
        "track": "AI",
        "category": "Real-Time AI Streaming",
        "system_name": "Design Real-Time Multimodal Voice & Audio Assistant",
        "key_components": "WebSocket / WebRTC Audio Streaming, Silero VAD, Streaming STT (Whisper), Fast LLM Inference (vLLM / Groq), Streaming TTS, Latency Budget (<500ms End-to-End)",
    },
    {
        "track": "AI",
        "category": "AI Code & Developer Tools",
        "system_name": "Design Code Generation & Sandboxed Autonomous Execution Engine",
        "key_components": "AST Parser, Repository Graph Indexer, Pydantic Structured Output, Docker / gVisor Isolated Container Sandbox, Self-Correction Execution Loop, AST Lint Validator",
    },
    {
        "track": "AI",
        "category": "Enterprise AI & Data",
        "system_name": "Design Text-to-SQL Enterprise Clarification & Execution Pipeline",
        "key_components": "DB Schema Graph Extractor, Few-Shot RAG Selector, Ambiguity Detector & User Clarification Prompter, Read-Only SQL Sandbox, Self-Healing Query Corrector",
    },
    {
        "track": "AI",
        "category": "Search & AI Retrieval",
        "system_name": "Design AI-Powered Semantic Search & Recommendation Engine",
        "key_components": "HNSW Indexing, Approximate Nearest Neighbor (ANN), Reciprocal Rank Fusion (RRF), ColBERT Token-Level Reranking, Dynamic Redis Prompt Cache, Personalization Embeddings",
    },
    {
        "track": "AI",
        "category": "AI Infrastructure & Serving",
        "system_name": "Design High-Throughput Distributed LLM Gateway & Smart Router",
        "key_components": "Semantic Cache (Redis / GPTCache), Model Router (Fast SLM Triage -> Frontier LLM), Token Bucket Rate Limiting per Tenant, Fallback Circuit Breaker, Prometheus Metrics Exporter",
    },
    {
        "track": "AI",
        "category": "AI Safety & Observability",
        "system_name": "Design Continuous AI Evaluation & Guardrail Safety Gateway",
        "key_components": "Llama Guard Classifier, PII Anonymizer (Presidio), OpenTelemetry LLM Tracing, Ragas Faithfulness Evaluator, Automated Rollback Trigger, Canary Testing Pipeline",
    },
    {
        "track": "AI",
        "category": "Agentic Systems",
        "system_name": "Design AI Agent Swarm for Automated Root Cause Analysis (SRE / Incident Remediation)",
        "key_components": "Multi-Agent Supervisor-Worker Topology, Prometheus / OpenSearch Tool Ingestor, Runbook Execution Sandbox, Human Approval Step for Prod Actions, Incident Post-Mortem Generator",
    },
    {
        "track": "AI",
        "category": "Document & Visual AI",
        "system_name": "Design High-Volume Document Processing & Visual Question Answering (VQA) Pipeline",
        "key_components": "Docling / Unstructured OCR Parser, Table Structure Extractor, Multimodal Embedding Model (CLIP / ColPali), Vector Search Index, S3 Storage, Celery Async Worker Fleet",
    },
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
    ("United States (Direct Product / Tech)", "USD", 150000, 210000, "year"),
    ("United States (AI Startup Direct)", "USD", 140000, 190000, "year"),
    ("United States (Contractor Placement Take-Home)", "USD", 90000, 120000, "year"),
    ("United States (Contractor Gross Client Billing)", "USD", 180000, 260000, "year"),
    ("Canada", "CAD", 120000, 160000, "year"),
    ("United Kingdom", "GBP", 75000, 110000, "year"),
    ("Germany / Netherlands", "EUR", 80000, 115000, "year"),
    ("UAE (Tax-Free)", "AED", 360000, 540000, "year"),
]


def seed_database(db: Session):
    """Seed all initial data. Safe to call multiple times."""

    # --- User Profile ---
    user = db.query(UserProfile).first()
    if not user:
        user = UserProfile(
            name="Rahul Dhar",
            target_role="Lead AI Engineer / Senior Python Backend Engineer",
            start_date=START_DATE,
            end_date=END_DATE,
            current_company="Denali Software Solutions (US: AllianceTek Inc, PA)",
            years_experience=8,
            linkedin_url="https://www.linkedin.com/in/rdhar8502/",
            github_url="https://github.com/rdhar8502",
            weekday_target_hours=1.5,
            saturday_target_hours=4.0,
            sunday_target_hours=3.5,
        )
        db.add(user)
    else:
        # Keep profile updated if default exists
        if not user.linkedin_url:
            user.linkedin_url = "https://www.linkedin.com/in/rdhar8502/"
        if not user.github_url:
            user.github_url = "https://github.com/rdhar8502"
        if user.years_experience < 8:
            user.years_experience = 8
        if "Denali" not in (user.current_company or ""):
            user.current_company = "Denali Software Solutions (US: AllianceTek Inc, PA)"
        if user.target_role != "Lead AI Engineer / Senior Python Backend Engineer":
            user.target_role = "Lead AI Engineer / Senior Python Backend Engineer"

    # --- Salary Targets ---
    db.query(SalaryTarget).delete()
    for region, currency, s_min, s_max, unit in SALARY_TARGETS:
        db.add(SalaryTarget(
            region=region, currency=currency,
            salary_min=s_min, salary_max=s_max, salary_unit=unit
        ))

    # --- Relocation Destinations ---
    existing_destinations = {d.country_name.lower(): d for d in db.query(RelocationDestination).all()}
    for d_data in DESTINATIONS_DATA:
        c_name = d_data["country_name"].lower()
        if c_name not in existing_destinations:
            dest = RelocationDestination(**d_data)
            db.add(dest)
        else:
            dest = existing_destinations[c_name]
            for key, val in d_data.items():
                setattr(dest, key, val)
    db.commit()

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

    # --- DSA Topics & Algorithm Topics ---
    existing_topic_names = {t.name.lower(): t for t in db.query(DSATopic).all()}
    max_order = max([t.order_index for t in existing_topic_names.values()], default=0)
    
    # 1. Base roadmap topics
    for i, name in enumerate(DSA_TOPICS):
        if name.lower() not in existing_topic_names:
            t = DSATopic(name=name, order_index=i + 1)
            db.add(t)
            existing_topic_names[name.lower()] = t
    
    # 2. Named algorithm topics
    for i, name in enumerate(DSA_ALGORITHM_TOPICS):
        if name.lower() not in existing_topic_names:
            max_order += 1
            t = DSATopic(name=name, order_index=max_order)
            db.add(t)
            existing_topic_names[name.lower()] = t
    
    db.commit()

    # --- DSA Companies ---
    existing_company_names = {c.name.lower(): c for c in db.query(DSACompany).all()}
    max_c_order = max([c.order_index for c in existing_company_names.values()], default=0)
    for i, name in enumerate(DSA_COMPANIES):
        if name.lower() not in existing_company_names:
            max_c_order += 1
            c = DSACompany(name=name, order_index=max_c_order)
            db.add(c)
            existing_company_names[name.lower()] = c
    db.commit()

    # Re-fetch all topics and companies mapping for accurate foreign key associations
    topic_map = {t.name.lower(): t for t in db.query(DSATopic).all()}
    company_map = {c.name.lower(): c for c in db.query(DSACompany).all()}

    # --- DSA Problems (280+ Curated Curriculum from Striver, Love Babbar, NeetCode) ---
    existing_problems = db.query(DSAProblem).all()

    def normalize_title(t: str) -> str:
        if not t:
            return ""
        # Strip leading numbering like "98. ", "41. "
        cleaned = re.sub(r"^\d+[\.\-\)]\s*", "", t.strip())
        if cleaned.startswith("http://") or cleaned.startswith("https://"):
            from app.models.dsa import clean_title_from_url
            cleaned = clean_title_from_url(cleaned)
        cleaned = re.sub(r"[^a-zA-Z0-9\s]", "", cleaned.lower())
        return " ".join(cleaned.split())

    # Build lookup index for existing problems
    existing_by_norm_title = {}
    existing_by_url = {}
    existing_by_alt_url = {}

    for p in existing_problems:
        norm = normalize_title(p.title)
        if norm:
            existing_by_norm_title[norm] = p
        norm_clean = normalize_title(p.clean_title)
        if norm_clean:
            existing_by_norm_title[norm_clean] = p
        if p.problem_url:
            existing_by_url[p.problem_url.strip().lower().rstrip("/")] = p
        if p.alternate_url:
            existing_by_alt_url[p.alternate_url.strip().lower().rstrip("/")] = p

    for p_data in DSA_PROBLEMS_DATA:
        title = p_data["title"]
        category = p_data["category"]
        difficulty = p_data["difficulty"]
        p_url = p_data.get("problem_url", "").strip()
        alt_title = p_data.get("alternate_title", "").strip()
        alt_url = p_data.get("alternate_url", "").strip()
        pattern = p_data.get("pattern", "")
        time_comp = p_data.get("time_complexity", "")
        space_comp = p_data.get("space_complexity", "")
        sec_topics = p_data.get("secondary_topics", [])
        comps = p_data.get("companies", [])

        # Match against existing problems to preserve user status and notes
        matched_prob = None
        norm_t = normalize_title(title)
        if norm_t in existing_by_norm_title:
            matched_prob = existing_by_norm_title[norm_t]
        elif p_url and p_url.lower().rstrip("/") in existing_by_url:
            candidate = existing_by_url[p_url.lower().rstrip("/")]
            # Only match if candidates have matching or empty titles
            if not candidate.title or normalize_title(candidate.title) == norm_t:
                matched_prob = candidate
        elif alt_url and alt_url.lower().rstrip("/") in existing_by_alt_url:
            candidate = existing_by_alt_url[alt_url.lower().rstrip("/")]
            if not candidate.title or normalize_title(candidate.title) == norm_t:
                matched_prob = candidate

        # Determine topic objects to associate
        topics_to_associate = []
        if category.lower() in topic_map:
            topics_to_associate.append(topic_map[category.lower()])
        for sec in sec_topics:
            if sec.lower() in topic_map and topic_map[sec.lower()] not in topics_to_associate:
                topics_to_associate.append(topic_map[sec.lower()])

        # Determine company objects to associate
        companies_to_associate = []
        for c_name in comps:
            c_key = c_name.strip().lower()
            if c_key in company_map:
                companies_to_associate.append(company_map[c_key])
            elif c_name.strip():
                new_c = DSACompany(name=c_name.strip(), order_index=len(company_map) + 1)
                db.add(new_c)
                db.flush()
                company_map[c_key] = new_c
                companies_to_associate.append(new_c)

        if matched_prob:
            # Update/enrich metadata while strictly preserving user progress and notes
            matched_prob.category = category
            matched_prob.difficulty = difficulty
            if not matched_prob.problem_url:
                matched_prob.problem_url = p_url
            if not matched_prob.alternate_url:
                matched_prob.alternate_url = alt_url
            if not matched_prob.alternate_title:
                matched_prob.alternate_title = alt_title
            if not matched_prob.pattern:
                matched_prob.pattern = pattern
            if not matched_prob.time_complexity:
                matched_prob.time_complexity = time_comp
            if not matched_prob.space_complexity:
                matched_prob.space_complexity = space_comp
            
            # Ensure topic association is up to date
            for t_obj in topics_to_associate:
                if t_obj not in matched_prob.topics:
                    matched_prob.topics.append(t_obj)

            # Ensure company association is up to date
            for c_obj in companies_to_associate:
                if c_obj not in matched_prob.companies:
                    matched_prob.companies.append(c_obj)
        else:
            # Create new problem
            new_p = DSAProblem(
                category=category,
                title=title,
                difficulty=difficulty,
                status="Not Started",
                pattern=pattern,
                mistake="",
                time_complexity=time_comp,
                space_complexity=space_comp,
                solution_snippet="",
                confidence=3,
                problem_url=p_url,
                alternate_title=alt_title,
                alternate_url=alt_url,
                topics=topics_to_associate,
                companies=companies_to_associate,
            )
            db.add(new_p)
            # Register in index
            if norm_t:
                existing_by_norm_title[norm_t] = new_p
            if p_url:
                existing_by_url[p_url.lower().rstrip("/")] = new_p
            if alt_url:
                existing_by_alt_url[alt_url.lower().rstrip("/")] = new_p

    db.commit()

    # --- System Design Concepts & Sub-concepts ---
    existing_concepts = db.query(SystemDesignConcept).all()
    concept_map = {(c.track.upper().strip(), c.concept_name.lower().strip()): c for c in existing_concepts}
    
    existing_subs = db.query(SystemDesignSubConcept).all()
    sub_map = {(s.concept_id, s.subconcept_name.lower().strip()): s for s in existing_subs}

    for i, (track, cat, concept_name, sub_list) in enumerate(SYSTEM_DESIGN_TOPICS):
        c_key = (track.upper().strip(), concept_name.lower().strip())
        concept = concept_map.get(c_key)
        if not concept:
            concept = SystemDesignConcept(
                track=track,
                category=cat,
                concept_name=concept_name,
                sources="",
                order_index=i + 1
            )
            db.add(concept)
            db.flush()
            concept_map[c_key] = concept
        else:
            concept.category = cat
            concept.order_index = i + 1

        for j, sub_name in enumerate(sub_list):
            s_key = (concept.id, sub_name.lower().strip())
            sub = sub_map.get(s_key)
            if not sub:
                sub = SystemDesignSubConcept(
                    concept_id=concept.id,
                    subconcept_name=sub_name,
                    order_index=j + 1,
                    status="Not Started",
                    reading_done=False,
                    practical_done=False,
                    notes="",
                    resources="",
                    sources="",
                )
                db.add(sub)
                db.flush()
                sub_map[s_key] = sub
            else:
                sub.order_index = j + 1
    db.commit()

    # --- System Design Cases ---
    existing_cases = {c.system_name.lower().strip(): c for c in db.query(SystemDesignCase).all()}
    for i, c_data in enumerate(SYSTEM_DESIGN_CASES):
        name = c_data["system_name"]
        track = c_data.get("track", "HLD")
        category = c_data.get("category", "Distributed Systems")
        default_components = c_data.get("key_components", "")

        case = existing_cases.get(name.lower().strip())
        if not case:
            case = SystemDesignCase(
                track=track,
                category=category,
                system_name=name,
                order_index=i + 1,
                status="Not Started",
                key_components=default_components,
                diagram_url="",
                notes="",
            )
            db.add(case)
        else:
            case.track = track
            case.category = category
            case.order_index = i + 1
            if not case.key_components:
                case.key_components = default_components
    db.commit()

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

    # --- Database Mastery Track Topics & Challenges ---
    if not db.query(DatabaseConcept).first():
        print("🌱 Seeding Database Mastery track concepts and items...")
        for c_idx, (track, cat, title, diff, desc, items_list) in enumerate(DATABASE_TOPICS):
            concept = DatabaseConcept(
                track=track,
                category=cat,
                title=title,
                difficulty=diff,
                description=desc,
                order_index=c_idx + 1,
            )
            db.add(concept)
            db.flush()

            for item_idx, (it_title, it_syntax, it_notes) in enumerate(items_list):
                db.add(DatabaseItem(
                    concept_id=concept.id,
                    title=it_title,
                    syntax_example=it_syntax,
                    notes=it_notes,
                    status="Not Started",
                    reading_done=False,
                    practical_done=False,
                    depth=2 if diff == "Medium" else (3 if diff == "Hard" else 1),
                    order_index=item_idx + 1,
                ))

        for ch_idx, ch in enumerate(DATABASE_CHALLENGES):
            db.add(DatabaseChallenge(
                track=ch.get("track", "SQL"),
                title=ch["title"],
                category=ch["category"],
                difficulty=ch["difficulty"],
                scenario=ch["scenario"],
                schema_definition=ch.get("schema_definition", ""),
                solution_query=ch.get("solution_query", ""),
                explanation=ch.get("explanation", ""),
                status="Not Started",
                order_index=ch_idx + 1,
            ))
        db.commit()

    print("✅ Database seeded successfully.")
