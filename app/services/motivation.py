from datetime import date
from typing import Dict

TECH_SPARKS = [
    # Level 1: System Design Basics
    "System Design: Caching is highly effective but introduces cache invalidation challenges. Remember the 3 main strategies: Write-through, Write-around, and Write-back.",
    "System Design: SQL databases are ACID compliant and optimal for relational data. NoSQL (like DynamoDB, Cassandra) excels at scaling horizontally with flexible schemas.",
    "System Design: Database indexes speed up reads but slow down writes. For composite indexes, order of columns is critical: place the most selective fields first.",
    "System Design: Load balancers (L4 vs L7) operate at different layers. L4 routes based on IP & Port (fast, TCP/UDP), while L7 routes based on HTTP headers, cookies, or content (flexible, SSL termination).",
    "System Design: CAP Theorem states a distributed system can only guarantee two out of Consistency, Availability, and Partition Tolerance. In practice, networks will partition (P), so we choose AP or CP.",
    "System Design: Message Queues (RabbitMQ) focus on message delivery guarantees and transient storage. Event Streams (Kafka) keep an immutable log of events, allowing consumers to replay history.",
    "System Design: Rate limiting protects APIs from abuse. Common algorithms include Token Bucket (allows bursts), Leaky Bucket (smooths output), and Sliding Window Log (precise but memory intensive).",
    "System Design: To design a URL Shortener, calculate storage requirements. 100M URLs/month * 500 bytes per record = 50GB storage/month. Keep estimations in mind during interviews!",
    "System Design: Consistent Hashing minimizes key redistribution when scaling cache nodes. A hash ring ensures that adding or removing a node only impacts a fraction of keys.",
    "System Design: Observability is built on three pillars: Logs (what happened), Metrics (aggregatable performance indicators), and Traces (end-to-end request journeys).",
    
    # Level 2: AI / LLM & RAG
    "AI/LLM: Hybrid search combines dense vector retrieval (semantic meaning) with sparse keyword matching (BM25 for exact terms). Rerankers (like Cohere) then re-order the combined top results.",
    "AI/LLM: Chunking strategies are vital for RAG. Use sliding windows or semantic chunking (splitting on sentence transitions) rather than rigid character counts to preserve context.",
    "AI/LLM: RAG Evaluation metrics (like RAGAS) focus on: Faithfulness (is the answer grounded in context?), Answer Relevance (does it address the query?), and Context Recall.",
    "AI/LLM: LLM Agent Memory relies on two layers: short-term memory (in-context window via chat history) and long-term memory (persisted in vector DBs or graph databases).",
    "AI/LLM: Streaming responses from LLMs improves user perceived latency (Time to First Token - TTFT) dramatically. Implement server-sent events (SSE) in FastAPI for this.",
    "AI/LLM: Guardrails (like LlamaGuard or Guardrails AI) validate LLM inputs and outputs to prevent prompt injection, toxic content, and hallucinated security leaks.",
    "AI/LLM: LangGraph allows building stateful multi-agent systems with cycles, unlike traditional DAG frameworks. Persistence checkpoints enable human-in-the-loop approvals.",
    "AI/LLM: Fine-tuning updates model weights for style/domain adjustment. RAG injects dynamic external facts. For factual accuracy and fresh data, RAG is almost always preferred.",
    "AI/LLM: Vector DB Indexing: HNSW (Hierarchical Navigable Small World) provides fast, approximate nearest neighbor search but has higher memory usage than IVF (Inverted File).",
    "AI/LLM: Prompt Injection can bypass system instructions. Secure your prompts by separating user input with distinct delimiters and using LLM classifiers to detect input intent.",

    # Level 3: Python & Backend Engineering
    "Python: The GIL (Global Interpreter Lock) limits CPU-bound multi-threading. Use multiprocessing for CPU-heavy jobs, and asyncio or threading for I/O-bound tasks.",
    "Python: FastAPI uses any ASGI server (like Uvicorn). Defining a route as `async def` runs it on the main event loop (should not do blocking I/O!). `def` runs it in a background threadpool.",
    "Python: Memory management in Python combines Reference Counting (immediate deletion when count is 0) with a Generational Garbage Collector to clean up reference cycles.",
    "Python: Database connection pooling (e.g. in SQLAlchemy) keeps database connections open to reuse them. Avoid opening/closing connections per request; it adds massive TCP handshake latency.",
    "Python: Generator functions (`yield`) produce values on demand, saving memory. Use generators when processing large datasets or streaming logs.",
    "Python: Celery tasks should be idempotent (safe to run multiple times with the same output). If a worker crashes and retries, duplicate task execution won't break data state.",
    "Python: Pydantic v2 is written in Rust, making validation and serialization up to 20x faster. Utilize `.model_dump()` and `.model_validate()` for data translation.",
    "Python: In PostgreSQL, the 'Serializable' isolation level prevents write skew and phantom reads but has high performance overhead due to serialization failures. Use Read Committed for general web apps.",
    "Python: Gunicorn with Uvicorn workers (`gunicorn -k uvicorn.workers.UvicornWorker`) is the standard production deployment setup for FastAPI to handle multiple CPU cores.",
    "Python: Keep Docker images small by using multi-stage builds. Compile dependencies in a builder stage and copy only the runtime artifacts to a slim base image.",
]

MOTIVATIONAL_QUOTES = [
    "Resilience: 'The only way to learn a new programming language is by writing programs in it.' — Dennis Ritchie",
    "Consistency: 'First, solve the problem. Then, write the code.' — John Johnson",
    "Focus: 'Simplicity is the soul of efficiency.' — Austin Freeman",
    "Consistency: 'Make it work, make it right, make it fast.' — Kent Beck",
    "Confidence: 'Talk is cheap. Show me the code.' — Linus Torvalds",
    "Consistency: 'Small daily improvements over time lead to stunning results.' — Robin Sharma",
    "Resilience: 'Strive for continuous improvement, not perfection.' — Kim Collins",
    "Focus: 'The secret of getting ahead is getting started.' — Mark Twain",
    "Growth: 'An investment in knowledge pays the best interest.' — Benjamin Franklin",
    "Consistency: 'We are what we repeatedly do. Excellence, then, is not an act, but a habit.' — Aristotle",
    "Resilience: 'It is not that I'm so smart, it's just that I stay with problems longer.' — Albert Einstein",
    "Focus: 'One step at a time is enough for me.' — Mahatma Gandhi",
    "Consistency: 'Consistency is the belt that fastens efficiency in place.' — Unknown",
    "Growth: 'The expert in anything was once a beginner.' — Helen Hayes",
    "Confidence: 'Believe you can and you're halfway there.' — Theodore Roosevelt",
    "Growth: 'Continuous learning is the minimum requirement for success in any field.' — Brian Tracy",
    "Resilience: 'Do not fear failure. Fear instead the lack of progress.' — Unknown",
    "Focus: 'Energy and persistence conquer all things.' — Benjamin Franklin",
    "Consistency: 'Success isn't always about greatness. It's about consistency.' — Dwayne Johnson",
    "Resilience: 'It always seems impossible until it's done.' — Nelson Mandela",
    "Growth: 'Be not afraid of going slowly, be afraid only of standing still.' — Chinese Proverb",
    "Consistency: 'Eighty percent of success is showing up.' — Woody Allen",
    "Focus: 'Concentrate all your thoughts upon the work at hand. The sun's rays do not burn until brought to a focus.' — Alexander Graham Bell",
    "Growth: 'If you are the smartest person in the room, you are in the wrong room.' — Unknown",
    "Resilience: 'Fall seven times, stand up eight.' — Japanese Proverb",
    "Focus: 'Focus on being productive instead of busy.' — Tim Ferriss",
    "Confidence: 'Action is the foundational key to all success.' — Pablo Picasso",
    "Growth: 'He who questions nothing learns nothing.' — English Proverb",
    "Consistency: 'Motivation gets you going, but discipline keeps you growing.' — John C. Maxwell",
    "Resilience: 'Difficulties master'd are opportunities won.' — Winston Churchill",
]


def get_daily_spark() -> Dict[str, str]:
    """Returns a daily tech tip and motivational quote based on the current date."""
    day_of_year = date.today().timetuple().tm_yday
    
    tech_index = day_of_year % len(TECH_SPARKS)
    quote_index = day_of_year % len(MOTIVATIONAL_QUOTES)
    
    return {
        "tech_tip": TECH_SPARKS[tech_index],
        "motivation": MOTIVATIONAL_QUOTES[quote_index]
    }
