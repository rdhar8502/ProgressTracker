"""
Curated seed data for Database Mastery Track:
- SQL (DDL, DML, DQL, ACID, CTEs, Transactions, Normalization)
- Joins & Advanced Functions (All Join Types, Algorithms, Window Functions, Framing, Aggregations, JSONB)
- NoSQL & Modern Storage (Redis, DynamoDB, MongoDB, Cassandra, ClickHouse, Neo4j, Vector DBs, Timescale)
- Database Internals & Indexing (B-Tree, B+Tree, Hash, GIN, Composite Indexes, EXPLAIN ANALYZE, MVCC, WAL)
- Real-World Query Challenges & Schema Design
"""

DATABASE_TOPICS = [
    # ══════════════════════════════════════════════════════════════════════════
    # 🗄️ SQL TRACK — Fundamentals, Queries & Relational Architecture
    # ══════════════════════════════════════════════════════════════════════════
    (
        "SQL",
        "Relational Foundations & DDL/DML",
        "Schema Definition, Constraints & Normalization",
        "Medium",
        "Master relational database structure, primary/foreign keys, constraints, and data normalization rules.",
        [
            (
                "Primary Keys, Composite Keys & Surrogate Keys",
                "CREATE TABLE users (\n  id BIGSERIAL PRIMARY KEY,\n  email VARCHAR(255) UNIQUE NOT NULL,\n  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()\n);\n\n-- Composite Primary Key Example\nCREATE TABLE order_items (\n  order_id BIGINT NOT NULL,\n  product_id BIGINT NOT NULL,\n  quantity INT DEFAULT 1,\n  PRIMARY KEY (order_id, product_id)\n);",
                "Natural keys vs Auto-increment surrogate keys vs UUIDv4/UUIDv7. Composite keys identify unique tuples across many-to-many junction tables."
            ),
            (
                "Foreign Keys, Referential Integrity & Cascades",
                "ALTER TABLE orders\nADD CONSTRAINT fk_orders_user\nFOREIGN KEY (user_id)\nREFERENCES users(id)\nON DELETE CASCADE\nON UPDATE RESTRICT;",
                "Referential integrity constraints prevent orphaned rows. ON DELETE actions: CASCADE, SET NULL, RESTRICT, NO ACTION."
            ),
            (
                "Database Normalization (1NF, 2NF, 3NF, BCNF) & Controlled Denormalization",
                "-- 1NF: Atomic values, unique column names\n-- 2NF: 1NF + No partial dependencies on composite PK\n-- 3NF: 2NF + No transitive functional dependencies (A -> B, B -> C)\n-- BCNF: Every determinant is a candidate key\n-- Denormalization: Pre-joining or caching aggregates for high-read throughput",
                "Understanding normal forms to eliminate data redundancy and anomalies (Insert, Update, Delete anomalies)."
            ),
            (
                "Check Constraints, Enums & Default Values",
                "CREATE TABLE accounts (\n  id SERIAL PRIMARY KEY,\n  balance NUMERIC(12, 2) NOT NULL DEFAULT 0.00,\n  status VARCHAR(20) DEFAULT 'ACTIVE',\n  CONSTRAINT chk_positive_balance CHECK (balance >= 0.00),\n  CONSTRAINT chk_valid_status CHECK (status IN ('ACTIVE', 'SUSPENDED', 'CLOSED'))\n);",
                "Enforce business rules directly in database engine level to guarantee data integrity."
            ),
        ]
    ),
    (
        "SQL",
        "Relational Foundations & DDL/DML",
        "Core DQL, Filtering & Conditional Logic",
        "Easy",
        "Fundamental data querying, filtering predicates, NULL behavior, and conditional expressions.",
        [
            (
                "SELECT, WHERE, LIKE, ILIKE & Pattern Matching",
                "SELECT id, first_name, last_name, email\nFROM users\nWHERE is_active = TRUE\n  AND (email ILIKE '%@google.com' OR email ILIKE '%@amazon.com')\nORDER BY created_at DESC\nLIMIT 25 OFFSET 50;",
                "Use parameterized predicates, case-insensitive ILIKE in PostgreSQL, and avoid leading wildcard `%term` when possible to utilize B-tree indexes."
            ),
            (
                "CASE WHEN Conditional Expressions & Pivoting",
                "SELECT \n  order_id,\n  amount,\n  CASE \n    WHEN amount >= 1000 THEN 'VIP / High'\n    WHEN amount >= 250  THEN 'Medium'\n    ELSE 'Standard / Low'\n  END AS customer_tier,\n  -- Conditional Count Pivot\n  COUNT(CASE WHEN status = 'COMPLETED' THEN 1 END) AS completed_cnt\nFROM orders\nGROUP BY order_id, amount;",
                "CASE WHEN works as inline switch/ternary expression. Critical for pivoting rows to columns and conditional aggregations."
            ),
            (
                "NULL Semantics (Three-Valued Logic, COALESCE, NULLIF)",
                "-- Three-valued logic: TRUE, FALSE, UNKNOWN (NULL = NULL evaluates to UNKNOWN)\nSELECT \n  user_id,\n  COALESCE(phone_number, fallback_number, 'N/A') AS contact_phone,\n  NULLIF(score, 0) AS safe_divisor -- Returns NULL if score == 0 to prevent division by zero\nFROM user_profiles\nWHERE deleted_at IS NULL;",
                "NULL means missing or unknown data. Always use IS NULL / IS NOT NULL. COALESCE returns first non-null argument."
            ),
        ]
    ),
    (
        "SQL",
        "Grouping & Advanced Aggregations",
        "Aggregations, GROUP BY & Multi-Dimensional Analysis",
        "Medium",
        "Aggregate calculation, grouping criteria, filtering groups with HAVING, and OLAP grouping sets.",
        [
            (
                "GROUP BY and HAVING Filtering Clause",
                "SELECT \n  department_id,\n  COUNT(*) AS total_employees,\n  ROUND(AVG(salary), 2) AS avg_salary,\n  MAX(salary) AS top_salary\nFROM employees\nWHERE hire_date >= '2023-01-01'  -- Row-level filter BEFORE grouping\nGROUP BY department_id\nHAVING COUNT(*) >= 5 AND AVG(salary) > 80000  -- Group-level filter AFTER aggregation\nORDER BY avg_salary DESC;",
                "WHERE filters rows before aggregation; HAVING filters grouped sets after aggregation."
            ),
            (
                "Multi-Dimensional Aggregations: GROUPING SETS, ROLLUP & CUBE",
                "SELECT \n  COALESCE(region, 'ALL REGIONS') AS region,\n  COALESCE(category, 'ALL CATEGORIES') AS category,\n  SUM(sales_amount) AS total_revenue,\n  GROUPING(region) AS is_region_subtotal\nFROM product_sales\nGROUP BY ROLLUP (region, category)\nORDER BY region, category;",
                "ROLLUP generates hierarchical sub-totals and grand total. CUBE generates all 2^N combinations. GROUPING SETS calculates exact specified groupings."
            ),
            (
                "Distinct Counting & Approximate Aggregations (HyperLogLog)",
                "-- Exact Count\nSELECT date, COUNT(DISTINCT user_id) AS dau FROM user_events GROUP BY date;\n\n-- PostgreSQL / Redis HyperLogLog for Billion-Scale DAU (O(1) Memory)\n-- SELECT hll_count(hll_add_agg(hll_hash_bigint(user_id))) FROM user_events;",
                "COUNT(DISTINCT) requires storing all unique keys in hash set. For big data streams, approximate algorithms like HyperLogLog provide 99% accuracy with tiny memory footprint."
            ),
        ]
    ),
    (
        "SQL",
        "Subqueries & CTEs",
        "Subqueries, Common Table Expressions & Recursion",
        "Hard",
        "Scalar subqueries, correlated subqueries, WITH statements, and graph/tree recursive traversal.",
        [
            (
                "Scalar & Correlated Subqueries",
                "-- Find employees earning more than their department's average salary\nSELECT e.id, e.name, e.salary, e.department_id\nFROM employees e\nWHERE e.salary > (\n  SELECT AVG(sub.salary)\n  FROM employees sub\n  WHERE sub.department_id = e.department_id  -- Correlated reference to outer query\n);",
                "Correlated subquery executes for every outer candidate row. Consider rewriting to JOIN or Window function for better optimizer performance."
            ),
            (
                "EXISTS vs IN Performance & NULL edge cases",
                "-- Safe and fast semi-join using EXISTS\nSELECT u.id, u.email\nFROM users u\nWHERE EXISTS (\n  SELECT 1 FROM orders o\n  WHERE o.user_id = u.id AND o.total_amount > 500\n);\n-- Note: NOT IN fails if subquery contains ANY null value (evaluates to UNKNOWN). Always prefer NOT EXISTS.",
                "EXISTS stops scanning on first match (short-circuit). NOT IN returns empty set if subquery contains a single NULL."
            ),
            (
                "Common Table Expressions (CTEs / WITH Clause)",
                "WITH MonthlyRevenue AS (\n  SELECT \n    DATE_TRUNC('month', order_date) AS order_month,\n    SUM(amount) AS monthly_total\n  FROM orders\n  GROUP BY 1\n),\nGrowthRate AS (\n  SELECT \n    order_month,\n    monthly_total,\n    LAG(monthly_total) OVER (ORDER BY order_month) AS prev_month_total\n  FROM MonthlyRevenue\n)\nSELECT \n  order_month,\n  monthly_total,\n  ROUND(((monthly_total - prev_month_total) / prev_month_total * 100.0), 2) AS pct_growth\nFROM GrowthRate;",
                "CTEs improve modularity and readability. In Postgres 12+, CTEs are automatically inlined unless marked `WITH cte AS MATERIALIZED (...)`."
            ),
            (
                "Recursive CTEs for Hierarchical & Graph Traversal",
                "WITH RECURSIVE OrgHierarchy AS (\n  -- Base Case: Top Level Managers (where manager_id IS NULL)\n  SELECT id, name, manager_id, 1 AS depth, CAST(name AS VARCHAR(1000)) AS path\n  FROM employees\n  WHERE manager_id IS NULL\n  \n  UNION ALL\n  \n  -- Recursive Member: Join child employees with parent OrgHierarchy\n  SELECT e.id, e.name, e.manager_id, h.depth + 1, CAST(h.path || ' -> ' || e.name AS VARCHAR(1000))\n  FROM employees e\n  JOIN OrgHierarchy h ON e.manager_id = h.id\n)\nSELECT * FROM OrgHierarchy ORDER BY depth, path;",
                "Recursive CTEs consist of an Anchor member and a Recursive member. Essential for categories trees, org charts, bills of materials, and graphs."
            ),
        ]
    ),
    (
        "SQL",
        "Transactions & Concurrency",
        "ACID, Isolation Levels & Locking Mechanics",
        "Hard",
        "Transaction boundaries, serializability, lock contention, MVCC, and concurrency anomalies.",
        [
            (
                "ACID Properties & Transaction Control (BEGIN, COMMIT, ROLLBACK)",
                "BEGIN TRANSACTION;\n\n-- Deduct funds from sender\nUPDATE bank_accounts \nSET balance = balance - 250.00 \nWHERE account_id = 'ACC_101' AND balance >= 250.00;\n\n-- Credit funds to recipient\nUPDATE bank_accounts \nSET balance = balance + 250.00 \nWHERE account_id = 'ACC_202';\n\n-- Save audit log\nINSERT INTO transfer_logs(from_acc, to_acc, amount, created_at)\nVALUES ('ACC_101', 'ACC_202', 250.00, NOW());\n\nCOMMIT;",
                "Atomicity: All-or-nothing. Consistency: Schema rules strictly preserved. Isolation: Concurrent txns do not corrupt state. Durability: Written to WAL/disk before ACK."
            ),
            (
                "Transaction Isolation Levels & Concurrency Anomalies",
                "-- Set Isolation Level\nSET TRANSACTION ISOLATION LEVEL REPEATABLE READ;\n\n-- Isolation Levels:\n-- 1. Read Uncommitted: Dirty reads possible (PostgreSQL treats as Read Committed)\n-- 2. Read Committed: Default. Prevents dirty reads. Non-repeatable reads possible.\n-- 3. Repeatable Read: Snapshot isolation. Prevents non-repeatable reads & phantom reads in Postgres.\n-- 4. Serializable: Strict serial execution guarantee (SSI). Aborts conflicting transactions.",
                "Anomalies: Dirty Read (reading uncommitted txn data), Non-repeatable read (value changes between two reads), Phantom read (new rows appear in range query)."
            ),
            (
                "Pessimistic Locking vs Optimistic Concurrency Control (OCC)",
                "-- Pessimistic Locking: Explicit row-level lock (Blocks other writers/readers wanting lock)\nSELECT * FROM inventory \nWHERE item_id = 899 \nFOR UPDATE; -- Or FOR SHARE for read locks\n\n-- Optimistic Concurrency Control (OCC): Check version on update\nUPDATE products\nSET stock = stock - 1, version = version + 1\nWHERE id = 899 AND version = 4;\n-- If row count returned == 0, retry transaction due to conflict.",
                "Pessimistic locking is best when contention is high. Optimistic locking with version timestamp is ideal for high-scale, low-contention distributed systems."
            ),
            (
                "Deadlocks & Prevention Strategies",
                "-- Cause: Txn A locks Row 1 and waits for Row 2; Txn B locks Row 2 and waits for Row 1.\n-- Resolution: DB engine deadlock detector aborts one transaction.\n-- Prevention Rules:\n-- 1. Always acquire locks in uniform global order (e.g. sorted by primary key ID).\n-- 2. Keep transactions short and focused.\n-- 3. Use SELECT ... FOR UPDATE NOWAIT or SKIP LOCKED for worker queues.",
                "Deadlocks occur with cyclic dependencies between locks. Ensure all code paths lock resources in the exact same deterministic order."
            ),
        ]
    ),

    # ══════════════════════════════════════════════════════════════════════════
    # ⚡ JOINS & FUNCTIONS TRACK — Deep Dive into Joins, Algorithms & Window Ops
    # ══════════════════════════════════════════════════════════════════════════
    (
        "JOINS_FUNCTIONS",
        "SQL Joins Deep Dive",
        "Join Types, Semantics & Relational Algebra",
        "Medium",
        "In-depth analysis of every join type, anti-joins, semi-joins, self-joins, and join predicate mechanics.",
        [
            (
                "INNER, LEFT, RIGHT & FULL OUTER Joins",
                "SELECT \n  u.id AS user_id,\n  u.name,\n  o.id AS order_id,\n  o.total_amount\nFROM users u\n-- INNER: only matching records in both tables\n-- LEFT OUTER: all users, with NULL orders if no match\n-- RIGHT OUTER: all orders, with NULL user if unmatched\n-- FULL OUTER: all users and all orders, paired where matched\nFULL OUTER JOIN orders o ON u.id = o.user_id;",
                "Inner Join is intersection. Left Join retains all left rows. Full Outer Join retains all rows from both sides, matching where possible."
            ),
            (
                "CROSS JOIN & Generating Combinations (Cartesian Product)",
                "-- Generate full matrix of dates and product categories for gapless reporting\nSELECT \n  d.calendar_date,\n  c.category_name,\n  COALESCE(SUM(s.amount), 0) AS daily_revenue\nFROM generate_series('2026-01-01'::date, '2026-01-31'::date, '1 day'::interval) d(calendar_date)\nCROSS JOIN product_categories c\nLEFT JOIN sales s ON s.sale_date = d.calendar_date AND s.category_id = c.id\nGROUP BY d.calendar_date, c.category_name\nORDER BY d.calendar_date, c.category_name;",
                "Cross join produces M * N rows. Essential for generating reporting grids, date series calendars, and test permutations."
            ),
            (
                "SELF JOIN for Sequential & Hierarchical Relationships",
                "-- Compare employee and their direct manager\nSELECT \n  e.name AS employee_name,\n  e.title AS employee_title,\n  COALESCE(m.name, 'TOP EXECUTIVE') AS manager_name\nFROM employees e\nLEFT JOIN employees m ON e.manager_id = m.id;\n\n-- Compare consecutive temperature logs (Weather problem)\nSELECT w1.record_date\nFROM weather_logs w1\nJOIN weather_logs w2 ON w1.record_date = w2.record_date + INTERVAL '1 day'\nWHERE w1.temperature > w2.temperature;",
                "Self join joins a table to itself using aliases. Ideal for hierarchy lookups, consecutive sequence checks, and graph edges."
            ),
            (
                "Anti-Joins & Semi-Joins (Finding Missing or Existing Records)",
                "-- ANTI-JOIN: Find users who NEVER placed an order\n-- Method A: LEFT JOIN with IS NULL filter\nSELECT u.id, u.name\nFROM users u\nLEFT JOIN orders o ON u.id = o.user_id\nWHERE o.id IS NULL;\n\n-- Method B: NOT EXISTS (Often faster with an index on orders.user_id)\nSELECT u.id, u.name\nFROM users u\nWHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id);\n\n-- SEMI-JOIN: Find products with at least one review (without duplicate rows)\nSELECT p.* FROM products p WHERE EXISTS (SELECT 1 FROM reviews r WHERE r.product_id = p.id);",
                "Semi-join returns each left row at most once if a match exists. Anti-join returns left rows that have no match on the right."
            ),
        ]
    ),
    (
        "JOINS_FUNCTIONS",
        "SQL Joins Deep Dive",
        "Physical Join Algorithms & Optimizer Execution",
        "Hard",
        "How database query planners physically execute joins: Nested Loop, Hash Join, and Sort-Merge Join.",
        [
            (
                "Nested Loop Join (Index vs Block Nested Loop)",
                "-- Optimizer picks Nested Loop when outer relation is small and inner has an index:\n-- Cost ~ O(N_outer * log(N_inner))\n-- Pseudocode:\n-- FOR each row in OuterTable:\n--   Search matching rows in InnerTable using B-Tree index\n--   Emit joined tuple\nEXPLAIN SELECT * FROM users u JOIN orders o ON u.id = o.user_id WHERE u.id = 42;",
                "Nested Loop is optimal when one table is very small (or filtered to 1 row) and the other table is indexed on join column."
            ),
            (
                "Hash Join (Build Phase & Probe Phase)",
                "-- Optimizer picks Hash Join for large, unsorted, unindexed equijoins:\n-- Cost ~ O(N + M)\n-- 1. Build Phase: Hash the smaller table into in-memory hash table on join key\n-- 2. Probe Phase: Scan the larger table, hash join key, probe hash table for matches\n-- Note: If hash table exceeds work_mem, spills to disk (Grace Hash Join)\nEXPLAIN SELECT * FROM customers c JOIN transactions t ON c.id = t.customer_id;",
                "Hash join requires equijoin (`=`). Scales linearly in time O(N+M). Memory bound by `work_mem`."
            ),
            (
                "Sort-Merge Join (Pre-Sorted & Range Joins)",
                "-- Optimizer picks Sort-Merge when both datasets are already sorted on join keys (via B-tree or explicit sort):\n-- Cost ~ O(N log N + M log M) or O(N + M) if pre-sorted\n-- Both pointers advance like two-pointer merge step\nEXPLAIN SELECT * FROM accounts a JOIN transactions t ON a.id = t.account_id ORDER BY a.id;",
                "Sort-merge join is efficient for large tables when inputs are already ordered by index or when join conditions involve inequalities (`<=`, `>=`)."
            ),
        ]
    ),
    (
        "JOINS_FUNCTIONS",
        "Window & Analytical Functions",
        "Ranking & Positional Window Functions",
        "Hard",
        "Master ROW_NUMBER, RANK, DENSE_RANK, NTILE, LEAD, LAG, and FIRST_VALUE with PARTITION BY.",
        [
            (
                "ROW_NUMBER() vs RANK() vs DENSE_RANK()",
                "SELECT \n  employee_id,\n  department_id,\n  salary,\n  -- 1, 2, 3, 4 (Strictly unique, arbitrary order on tie)\n  ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS row_num,\n  -- 1, 2, 2, 4 (Gaps on tie: next rank skips)\n  RANK()       OVER (PARTITION BY department_id ORDER BY salary DESC) AS rnk,\n  -- 1, 2, 2, 3 (No gaps on tie: next rank is continuous)\n  DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS dense_rnk\nFROM employees;",
                "DENSE_RANK() is required for 'Find Nth highest salary' problems. ROW_NUMBER() is best for pagination and deduplication."
            ),
            (
                "LEAD() and LAG() for Period-over-Period Delta Comparisons",
                "SELECT \n  metric_date,\n  daily_revenue,\n  LAG(daily_revenue, 1) OVER (ORDER BY metric_date) AS prev_day_revenue,\n  (daily_revenue - LAG(daily_revenue, 1) OVER (ORDER BY metric_date)) AS day_change,\n  LEAD(daily_revenue, 1) OVER (ORDER BY metric_date) AS next_day_revenue\nFROM daily_metrics\nORDER BY metric_date;",
                "LAG accesses preceding row at specified offset; LEAD accesses following row. Eliminates the need for self-joins."
            ),
            (
                "NTILE(n) for Quantile, Decile & Cohort Segmentation",
                "SELECT \n  customer_id,\n  total_spent,\n  -- Splits customers into 4 quartiles (1 = Top 25%, 4 = Bottom 25%)\n  NTILE(4) OVER (ORDER BY total_spent DESC) AS spend_quartile,\n  -- 10 Deciles\n  NTILE(10) OVER (ORDER BY total_spent DESC) AS spend_decile\nFROM customer_lifetime_value;",
                "NTILE distributes rows as evenly as possible into N ranked buckets."
            ),
            (
                "FIRST_VALUE(), LAST_VALUE() & NTH_VALUE()",
                "SELECT \n  emp_id,\n  department_id,\n  salary,\n  FIRST_VALUE(emp_id) OVER (\n    PARTITION BY department_id \n    ORDER BY salary DESC \n    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING\n  ) AS highest_paid_emp_id,\n  NTH_VALUE(emp_id, 2) OVER (\n    PARTITION BY department_id \n    ORDER BY salary DESC \n    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING\n  ) AS second_highest_paid_emp_id\nFROM employees;",
                "Always check frame specification `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING` when using LAST_VALUE and NTH_VALUE."
            ),
        ]
    ),
    (
        "JOINS_FUNCTIONS",
        "Window & Analytical Functions",
        "Window Framing & Sliding Window Aggregations",
        "Hard",
        "Sliding window frames, cumulative running totals, moving averages, and frame bounds.",
        [
            (
                "ROWS vs RANGE Frame Specifications",
                "SELECT \n  transaction_date,\n  amount,\n  -- Physical row offset: exactly current + prior 6 rows\n  AVG(amount) OVER (\n    ORDER BY transaction_date \n    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW\n  ) AS rolling_7_row_avg,\n  -- Logical range offset: within 7 calendar days\n  SUM(amount) OVER (\n    ORDER BY transaction_date \n    RANGE BETWEEN INTERVAL '6 days' PRECEDING AND CURRENT ROW\n  ) AS rolling_7_day_sum\nFROM daily_transactions;",
                "ROWS counts physical rows regardless of duplicates. RANGE operates on value ranges according to ORDER BY column."
            ),
            (
                "Cumulative Running Totals & YTD Metrics",
                "SELECT \n  account_id,\n  txn_date,\n  amount,\n  -- Running balance from beginning of time\n  SUM(amount) OVER (\n    PARTITION BY account_id \n    ORDER BY txn_date, txn_id \n    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW\n  ) AS running_balance\nFROM bank_transactions;",
                "Running totals compute cumulative sums without GROUP BY, retaining all individual row details."
            ),
        ]
    ),
    (
        "JOINS_FUNCTIONS",
        "Specialized Functions & JSON",
        "String, Date/Time & PostgreSQL JSONB Operations",
        "Medium",
        "Date truncation, string aggregation, pattern extractions, and semi-structured JSON querying.",
        [
            (
                "Date/Time Manipulation (DATE_TRUNC, AGE, INTERVAL Arithmetic)",
                "SELECT \n  DATE_TRUNC('month', created_at) AS signup_month,\n  COUNT(*) AS new_users,\n  AVG(AGE(NOW(), date_of_birth)) AS avg_age\nFROM users\nWHERE created_at >= NOW() - INTERVAL '12 months'\nGROUP BY 1\nORDER BY 1 DESC;",
                "DATE_TRUNC rounds timestamps to specified granularity (minute, hour, day, week, month, quarter, year)."
            ),
            (
                "String Aggregation: STRING_AGG / GROUP_CONCAT",
                "SELECT \n  d.department_name,\n  COUNT(e.id) AS member_count,\n  STRING_AGG(e.name, ', ' ORDER BY e.salary DESC) AS team_roster\nFROM departments d\nJOIN employees e ON d.id = e.department_id\nGROUP BY d.department_name;",
                "Combines multiple string values from grouped rows into a single delimited string."
            ),
            (
                "JSON & JSONB Querying in PostgreSQL",
                "-- Filter and extract fields from JSONB column\nSELECT \n  id,\n  payload->>'event_name' AS event_type,\n  (payload->'user'->>'age')::INT AS user_age,\n  payload->'tags' AS tags_array\nFROM event_logs\n-- Fast JSON containment operator using GIN Index (@>)\nWHERE payload @> '{\"status\": \"ERROR\", \"priority\": \"HIGH\"}'\n  AND payload->'tags' ? 'production';",
                "`->` returns JSON object; `->>` returns raw text. `@>` tests JSON containment (indexable with GIN)."
            ),
        ]
    ),

    # ══════════════════════════════════════════════════════════════════════════
    # 🍃 NOSQL & MODERN STORAGE TRACK — Distributed, Document, Key-Value & Vector
    # ══════════════════════════════════════════════════════════════════════════
    (
        "NOSQL",
        "Key-Value & In-Memory Storage",
        "Redis & DynamoDB Architecture",
        "Medium",
        "In-memory caching patterns, Redis data structures, distributed locks, and DynamoDB single-table design.",
        [
            (
                "Redis Data Structures & Command Patterns",
                "# String & Cache with TTL\nSET session:usr_9981 '{\"name\":\"Alice\"}' EX 3600\n\n# Sorted Sets for Real-time Leaderboards\nZADD leaderboard 14500 'user_1'\nZADD leaderboard 18200 'user_2'\nZREVRANGE leaderboard 0 9 WITHSCORES\n\n# Hashes for object fields\nHSET user:100 name 'Bob' email 'bob@work.com' logins 42\nHINCRBY user:100 logins 1",
                "Redis is single-threaded event loop (epoll) operating entirely in RAM with optional RDB/AOF persistence. O(1) string ops, O(log N) sorted set ops."
            ),
            (
                "Amazon DynamoDB Single-Table Design",
                "-- DynamoDB Keys:\n-- Partition Key (PK) -> Determines partition hash ring placement\n-- Sort Key (SK) -> Orders items within the same partition\n\n-- Example Single-Table Entities:\n-- PK: USER#101,    SK: METADATA,   Data: { name: 'Rahul', email: 'r@d.com' }\n-- PK: USER#101,    SK: ORDER#501,  Data: { total: 199.99, date: '2026-08-16' }\n-- PK: ORDER#501,   SK: ITEM#P88,   Data: { title: 'Mechanical Keyboard', qty: 1 }",
                "Single-Table design retrieves parent entity and all related child records in a single partition query `PK = USER#101 AND SK BEGINS_WITH 'ORDER#'`."
            ),
            (
                "Distributed Locking with Redis (Redlock)",
                "// Distributed Lock Pattern:\n// 1. SET lock_key unique_token NX PX 30000 (Atomic acquire with TTL)\n// 2. Perform critical section work\n// 3. Lua script to release lock only if token matches (avoids releasing another worker's expired lock)\nif redis.call('get', KEYS[1]) == ARGV[1] then\n    return redis.call('del', KEYS[1])\nelse\n    return 0\nend",
                "Atomic lock acquisition prevents race conditions across distributed microservices."
            ),
        ]
    ),
    (
        "NOSQL",
        "Document & Columnar Databases",
        "MongoDB & ClickHouse / Cassandra",
        "Hard",
        "Document data modeling, MongoDB aggregation pipelines, wide-column Cassandra, and OLAP columnar ClickHouse.",
        [
            (
                "MongoDB Document Modeling: Embedding vs Referencing",
                "// 1:Few relationship -> Embed directly (e.g. User addresses)\n{\n  _id: ObjectId('...'),\n  name: 'Alex',\n  addresses: [\n    { street: '123 Main St', city: 'Seattle', zip: '98101' },\n    { street: '456 Oak Ave', city: 'San Jose', zip: '95112' }\n  ]\n}\n\n// 1:Many / 1:Squillions -> Reference with ObjectId\n// posts collection references user_id with index on user_id",
                "Embed when data is queried together and bounded in size (<16MB BSON limit). Reference when unbounded growth or data is updated independently."
            ),
            (
                "MongoDB Aggregation Pipeline",
                "db.orders.aggregate([\n  // Stage 1: Filter completed orders in 2026\n  { $match: { status: 'COMPLETED', order_date: { $gte: ISODate('2026-01-01') } } },\n  // Stage 2: Unwind line items array\n  { $unwind: '$items' },\n  // Stage 3: Group by category and sum revenue\n  { $group: {\n      _id: '$items.category',\n      totalRevenue: { $sum: { $multiply: ['$items.price', '$items.quantity'] } },\n      itemCount: { $sum: '$items.quantity' }\n  } },\n  // Stage 4: Filter high-grossing categories\n  { $match: { totalRevenue: { $gt: 50000 } } },\n  // Stage 5: Sort descending\n  { $sort: { totalRevenue: -1 } }\n]);",
                "Aggregation pipeline processes streams of documents sequentially through composable stages: $match, $project, $group, $lookup, $unwind."
            ),
            (
                "Apache Cassandra & ScyllaDB Wide-Column Architecture",
                "-- CQL (Cassandra Query Language)\nCREATE TABLE sensor_readings (\n  sensor_id UUID,\n  reading_date DATE,\n  recorded_at TIMESTAMP,\n  temperature DOUBLE,\n  humidity DOUBLE,\n  PRIMARY KEY ((sensor_id, reading_date), recorded_at)\n) WITH CLUSTERING ORDER BY (recorded_at DESC);\n\n-- Partition Key = (sensor_id, reading_date) -> determines node replica\n-- Clustering Key = recorded_at -> orders data on disk in SSTables",
                "Cassandra is masterless peer-to-peer ring. Highly optimized for high write throughput using CommitLog and LSM-Trees. Never query without Partition Key."
            ),
            (
                "ClickHouse & Columnar Storage for Real-Time Analytics (OLAP)",
                "-- ClickHouse Columnar Table\nCREATE TABLE event_stream (\n  event_time DateTime,\n  user_id UInt64,\n  event_type LowCardinality(String),\n  ip IPv4,\n  duration_ms UInt32\n)\nENGINE = MergeTree()\nPARTITION BY toYYYYMM(event_time)\nORDER BY (event_type, event_time, user_id);",
                "Columnar storage reads only queried columns from disk. Vectorized SIMD execution and heavy compression (LZ4/ZSTD) deliver 100x faster analytical aggregations than OLTP RDBMS."
            ),
        ]
    ),
    (
        "NOSQL",
        "Graph, Vector & Time-Series",
        "Neo4j, pgvector & TimescaleDB",
        "Hard",
        "Graph query traversal with Cypher, high-dimensional vector embeddings search, and time-series hypertables.",
        [
            (
                "Neo4j & Cypher Graph Queries",
                "// Find 2nd-degree friend recommendations (Friends of Friends)\nMATCH (u:User {username: 'rahul'})-[:FRIENDS_WITH]->(f:User)-[:FRIENDS_WITH]->(fof:User)\nWHERE NOT (u)-[:FRIENDS_WITH]->(fof) AND u <> fof\nRETURN fof.username, COUNT(f) AS mutual_friends_count\nORDER BY mutual_friends_count DESC\nLIMIT 10;",
                "Index-free adjacency allows constant O(1) edge traversal regardless of total graph database size."
            ),
            (
                "Vector Databases & Similarity Search (pgvector / HNSW)",
                "-- Enable pgvector in PostgreSQL\nCREATE EXTENSION IF NOT EXISTS vector;\n\nCREATE TABLE document_chunks (\n  id BIGSERIAL PRIMARY KEY,\n  document_id BIGINT,\n  content TEXT,\n  embedding vector(1536) -- OpenAI text-embedding-3-small dimension\n);\n\n-- Create Hierarchical Navigable Small World (HNSW) Approximate Nearest Neighbor Index\nCREATE INDEX ON document_chunks USING hnsw (embedding vector_cosine_ops);\n\n-- Cosine Distance Query (<=>)\nSELECT id, content, 1 - (embedding <=> '[0.015, -0.042, ...]') AS similarity\nFROM document_chunks\nORDER BY embedding <=> '[0.015, -0.042, ...]' \nLIMIT 5;",
                "Vector databases store high-dimensional embeddings for Semantic Search and LLM RAG pipelines using HNSW or IVFFlat indexes."
            ),
            (
                "TimescaleDB & Time-Series Hypertables",
                "-- Convert standard table to Timescale Hypertable with automatic time chunking\nSELECT create_hypertable('device_telemetry', 'timestamp');\n\n-- Time-bucket Downsampling Query\nSELECT \n  time_bucket('5 minutes', timestamp) AS five_min,\n  device_id,\n  avg(cpu_usage) AS avg_cpu,\n  max(temperature) AS max_temp\nFROM device_telemetry\nWHERE timestamp >= NOW() - INTERVAL '24 hours'\nGROUP BY five_min, device_id\nORDER BY five_min DESC;",
                "Hypertables automatically partition incoming time-series data into time chunks, maintaining fast write rates and efficient retention policies."
            ),
        ]
    ),

    # ══════════════════════════════════════════════════════════════════════════
    # ⚙️ INTERNALS & PERFORMANCE — Indexes, Optimizer, Storage Engines & Scaling
    # ══════════════════════════════════════════════════════════════════════════
    (
        "INTERNALS",
        "Index Structures & Mechanics",
        "B-Trees, Composite Indexes & Leftmost Prefix",
        "Hard",
        "Deep understanding of B+Tree node pointers, fan-out, composite index ordering, and specialized indexes.",
        [
            (
                "B-Tree vs B+Tree Internals",
                "-- B-Tree: Stores keys and data pointers in both internal and leaf nodes.\n-- B+Tree: Stores ALL data pointers strictly in leaf nodes; internal nodes only store keys for routing.\n-- Leaf nodes form a doubly-linked list enabling fast sequential range scans.\n-- Fan-out: Number of child pointers per node (typically 100-500), keeping tree height shallow (3-4 levels for billions of rows).",
                "A B+Tree with height 3 and branch factor 200 can index 8,000,000 leaf pages with only 3 disk I/O lookups."
            ),
            (
                "Composite Indexes & The Leftmost Prefix Rule",
                "-- Index Definition:\nCREATE INDEX idx_orders_customer_status_date \nON orders (customer_id, status, order_date DESC);\n\n-- USES INDEX FULLY (matches leftmost prefix: customer_id + status + date):\nSELECT * FROM orders WHERE customer_id = 10 AND status = 'PAID' AND order_date > '2026-01-01';\n\n-- USES INDEX PARTIALLY (matches customer_id only):\nSELECT * FROM orders WHERE customer_id = 10 AND order_date > '2026-01-01';\n\n-- CANNOT USE INDEX (skips leading customer_id column):\nSELECT * FROM orders WHERE status = 'PAID';",
                "Composite indexes only serve queries filtering on a continuous prefix of index columns starting from the first column."
            ),
            (
                "Covering Indexes & Index Only Scans (INCLUDE Clause)",
                "-- Covering Index includes non-key payload columns directly in leaf nodes\nCREATE INDEX idx_users_email_covering \nON users (email) \nINCLUDE (first_name, last_name, role);\n\n-- Returns result straight from index without touching table heap pages (Index Only Scan):\nEXPLAIN SELECT first_name, last_name, role FROM users WHERE email = 'user@corp.com';",
                "Index Only Scan avoids expensive Table Heap I/O lookups by satisfying the entire query from the index pages."
            ),
            (
                "Specialized Indexes: GIN, GiST, BRIN & Hash",
                "-- GIN (Generalized Inverted Index) for full text search & JSONB containment\nCREATE INDEX idx_docs_gin ON articles USING gin(to_tsvector('english', body));\n\n-- BRIN (Block Range Index) for massive append-only sequential time data (tiny index size)\nCREATE INDEX idx_logs_brin ON system_logs USING brin(created_at);\n\n-- Partial Index (Indexes only subset of rows to save memory)\nCREATE INDEX idx_pending_orders ON orders(id) WHERE status = 'PENDING';",
                "BRIN indexes store min/max values per page block range, taking 1/1000th the disk space of a B-tree for append-only logs."
            ),
        ]
    ),
    (
        "INTERNALS",
        "Query Optimization & Storage Engines",
        "EXPLAIN ANALYZE, MVCC, WAL & Connection Pooling",
        "Hard",
        "Execution plans, buffer statistics, vacuum mechanics, write-ahead logging, and scaling architectures.",
        [
            (
                "Decoding EXPLAIN (ANALYZE, BUFFERS)",
                "EXPLAIN (ANALYZE, BUFFERS, TIMING, COSTS)\nSELECT u.name, SUM(o.total_amount)\nFROM users u\nJOIN orders o ON u.id = o.user_id\nWHERE o.created_at >= '2026-01-01'\nGROUP BY u.name;\n\n-- Key Plan Metrics:\n-- 1. Seq Scan vs Index Scan vs Index Only Scan vs Bitmap Heap Scan\n-- 2. Actual Rows vs Estimated Rows (Large discrepancy means stale statistics -> run ANALYZE)\n-- 3. Buffers: Shared hit (RAM cache) vs Shared read (Disk I/O)",
                "Always run `EXPLAIN (ANALYZE, BUFFERS)` to diagnose slow queries, identify missing indexes, and inspect buffer page cache hits."
            ),
            (
                "MVCC (Multi-Version Concurrency Control) & VACUUM",
                "-- In PostgreSQL, UPDATES create new row versions (tuples) with xmin / xmax txn IDs.\n-- DELETES set xmax to deleting txn ID without immediately reclaiming disk space.\n-- Dead Tuples accumulate and cause table bloat.\n-- VACUUM reclaims dead tuple storage for reuse; AUTOVACUUM automates cleanup.\n\n-- Check dead tuple ratio\nSELECT relname, n_live_tup, n_dead_tup, ROUND(n_dead_tup * 100.0 / NULLIF(n_live_tup + n_dead_tup, 0), 2) AS dead_pct\nFROM pg_stat_user_tables;",
                "MVCC allows readers not to block writers and writers not to block readers. Autovacuum prevents transaction ID wraparound and bloat."
            ),
            (
                "Write-Ahead Logging (WAL), Checkpoints & Crash Recovery",
                "-- 1. Changes written sequentially to WAL buffer and flushed to disk (fsync)\n-- 2. Dirty data pages in shared_buffers modified in RAM\n-- 3. Transaction commits as soon as WAL is flushed (fast sequential write)\n-- 4. Checkpointer asynchronously flushes dirty RAM pages to main data files\n-- 5. Crash Recovery: Replays WAL logs starting from last checkpoint",
                "WAL guarantees Durability (D in ACID) by converting random disk page writes into sequential log appends."
            ),
            (
                "Connection Pooling (PgBouncer) & Database Sharding",
                "-- Why Connection Pooling:\n-- Each PostgreSQL backend connection is a separate OS process consuming ~5-10MB RAM.\n-- PgBouncer modes:\n--   * Session Pooling: 1 connection per client session\n--   * Transaction Pooling: Connection returned to pool after COMMIT/ROLLBACK (Highest concurrency)\n--   * Statement Pooling: Single statement per connection (No multi-statement transactions)\n\n-- Database Sharding: Partitioning data horizontally across distinct database servers via Hash Ring or Lookup Directory.",
                "Connection poolers sit between app servers and database, multiplexing thousands of incoming client requests over a tight pool of backend database connections."
            ),
        ]
    ),
]


DATABASE_CHALLENGES = [
    {
        "track": "SQL",
        "title": "Top N Highest Earning Employees Per Department",
        "category": "Window Functions & Ranking",
        "difficulty": "Medium",
        "scenario": "Given an `employees` table and a `departments` table, write a SQL query to find the employees who have the top 3 highest unique salaries in each department. If there are ties, all employees with that salary rank should be included.",
        "schema_definition": "CREATE TABLE departments (\n  id INT PRIMARY KEY,\n  name VARCHAR(100)\n);\n\nCREATE TABLE employees (\n  id INT PRIMARY KEY,\n  name VARCHAR(100),\n  salary NUMERIC(10, 2),\n  department_id INT REFERENCES departments(id)\n);",
        "solution_query": "WITH RankedSalaries AS (\n  SELECT \n    d.name AS department,\n    e.name AS employee,\n    e.salary,\n    DENSE_RANK() OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) AS salary_rank\n  FROM employees e\n  JOIN departments d ON e.department_id = d.id\n)\nSELECT department, employee, salary\nFROM RankedSalaries\nWHERE salary_rank <= 3\nORDER BY department, salary DESC, employee;",
        "explanation": "Using `DENSE_RANK()` ensures that tied salaries share the same ranking without skipping numbers (e.g. 1, 2, 2, 3), satisfying the requirement to get the top 3 distinct salary tiers per department.",
    },
    {
        "track": "SQL",
        "title": "Consecutive Active Days & Login Streaks (Gaps and Islands)",
        "category": "Gaps & Islands Problem",
        "difficulty": "Hard",
        "scenario": "Given a `user_logins` table recording user logins by date, write a query to find all users who logged in for at least 3 consecutive days, returning the user ID, streak start date, streak end date, and total streak length.",
        "schema_definition": "CREATE TABLE user_logins (\n  user_id INT,\n  login_date DATE,\n  PRIMARY KEY (user_id, login_date)\n);",
        "solution_query": "WITH NumberedLogins AS (\n  SELECT \n    user_id,\n    login_date,\n    -- Subtracting row_number from login_date yields a constant grouping date for consecutive days\n    login_date - (ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY login_date) * INTERVAL '1 day') AS streak_island\n  FROM user_logins\n),\nStreakGroups AS (\n  SELECT \n    user_id,\n    MIN(login_date) AS streak_start,\n    MAX(login_date) AS streak_end,\n    COUNT(*) AS streak_length\n  FROM NumberedLogins\n  GROUP BY user_id, streak_island\n)\nSELECT user_id, streak_start, streak_end, streak_length\nFROM StreakGroups\nWHERE streak_length >= 3\nORDER BY user_id, streak_start;",
        "explanation": "The classic Gaps & Islands pattern: `date - row_number` creates a constant grouping identifier (`streak_island`) for all contiguous dates. When grouped by this island, `COUNT(*)` yields streak length.",
    },
    {
        "track": "SQL",
        "title": "Monthly Retention & Cohort Churn Rate",
        "category": "Cohort Analysis & Date Math",
        "difficulty": "Hard",
        "scenario": "Calculate monthly cohort retention rates. Group users by their signup month and compute the percentage of those users who remained active in Month 1, Month 2, and Month 3 after signup.",
        "schema_definition": "CREATE TABLE users (\n  user_id INT PRIMARY KEY,\n  signup_date DATE\n);\n\nCREATE TABLE user_activity (\n  user_id INT,\n  activity_date DATE\n);",
        "solution_query": "WITH UserCohorts AS (\n  SELECT \n    user_id,\n    DATE_TRUNC('month', signup_date)::DATE AS cohort_month\n  FROM users\n),\nCohortSizes AS (\n  SELECT cohort_month, COUNT(user_id) AS total_users\n  FROM UserCohorts\n  GROUP BY cohort_month\n),\nActivityMonths AS (\n  SELECT DISTINCT\n    c.cohort_month,\n    c.user_id,\n    (EXTRACT(YEAR FROM a.activity_date) - EXTRACT(YEAR FROM c.cohort_month)) * 12 + \n    (EXTRACT(MONTH FROM a.activity_date) - EXTRACT(MONTH FROM c.cohort_month)) AS month_offset\n  FROM UserCohorts c\n  JOIN user_activity a ON c.user_id = a.user_id\n  WHERE a.activity_date >= c.cohort_month\n)\nSELECT \n  s.cohort_month,\n  s.total_users,\n  COUNT(CASE WHEN a.month_offset = 0 THEN a.user_id END) AS month_0_active,\n  ROUND(COUNT(CASE WHEN a.month_offset = 1 THEN a.user_id END) * 100.0 / s.total_users, 1) AS m1_retention_pct,\n  ROUND(COUNT(CASE WHEN a.month_offset = 2 THEN a.user_id END) * 100.0 / s.total_users, 1) AS m2_retention_pct,\n  ROUND(COUNT(CASE WHEN a.month_offset = 3 THEN a.user_id END) * 100.0 / s.total_users, 1) AS m3_retention_pct\nFROM CohortSizes s\nLEFT JOIN ActivityMonths a ON s.cohort_month = a.cohort_month\nGROUP BY s.cohort_month, s.total_users\nORDER BY s.cohort_month;",
        "explanation": "Calculates month delta offset between user signup cohort date and activity date, then aggregates using conditional counts to calculate retention percentages across M0, M1, M2, and M3.",
    },
    {
        "track": "SQL",
        "title": "Hierarchical Category Breadcrumb Path Generator",
        "category": "Recursive CTEs",
        "difficulty": "Medium",
        "scenario": "Given a category table with self-referencing `parent_id`, generate the complete breadcrumb hierarchy path string (e.g. `Electronics > Computers > Laptops`) for all categories.",
        "schema_definition": "CREATE TABLE categories (\n  id INT PRIMARY KEY,\n  name VARCHAR(100),\n  parent_id INT REFERENCES categories(id)\n);",
        "solution_query": "WITH RECURSIVE CategoryPath AS (\n  -- Anchor member: Root categories (no parent)\n  SELECT \n    id,\n    name,\n    parent_id,\n    1 AS depth,\n    CAST(name AS TEXT) AS breadcrumb\n  FROM categories\n  WHERE parent_id IS NULL\n\n  UNION ALL\n\n  -- Recursive member: Join child with parent path\n  SELECT \n    c.id,\n    c.name,\n    c.parent_id,\n    cp.depth + 1,\n    cp.breadcrumb || ' > ' || c.name\n  FROM categories c\n  JOIN CategoryPath cp ON c.parent_id = cp.id\n)\nSELECT id, name, depth, breadcrumb\nFROM CategoryPath\nORDER BY breadcrumb;",
        "explanation": "Anchor selects root nodes where parent_id is NULL. Recursive union builds path strings by concatenating the parent breadcrumb with child name.",
    },
    {
        "track": "NOSQL",
        "title": "MongoDB E-Commerce Aggregation Pipeline: Top Selling Categories",
        "category": "Document DB Aggregation",
        "difficulty": "Medium",
        "scenario": "In a MongoDB database with an `orders` collection, write an aggregation pipeline to find the top 5 highest grossing product categories for completed orders in Q1 2026.",
        "schema_definition": "// Orders document structure:\n// {\n//   _id: ObjectId(...),\n//   status: 'COMPLETED',\n//   order_date: ISODate('2026-02-14T...'),\n//   items: [\n//     { product_id: 'P10', category: 'Electronics', price: 299.99, quantity: 2 },\n//     { product_id: 'P22', category: 'Accessories', price: 25.00, quantity: 1 }\n//   ]\n// }",
        "solution_query": "db.orders.aggregate([\n  {\n    $match: {\n      status: 'COMPLETED',\n      order_date: {\n        $gte: ISODate('2026-01-01T00:00:00Z'),\n        $lt: ISODate('2026-04-01T00:00:00Z')\n      }\n    }\n  },\n  { $unwind: '$items' },\n  {\n    $group: {\n      _id: '$items.category',\n      totalRevenue: { $sum: { $multiply: ['$items.price', '$items.quantity'] } },\n      totalUnitsSold: { $sum: '$items.quantity' }\n    }\n  },\n  { $sort: { totalRevenue: -1 } },\n  { $limit: 5 },\n  {\n    $project: {\n      _id: 0,\n      category: '$_id',\n      totalRevenue: { $round: ['$totalRevenue', 2] },\n      totalUnitsSold: 1\n    }\n  }\n]);",
        "explanation": "Stages: $match filters by status and date range; $unwind splits embedded items array; $group calculates multiplied revenue sum; $sort and $limit extract top 5.",
    },
    {
        "track": "SYSTEM",
        "title": "High-Concurrency Inventory Reservation (Flash Sale Race Condition)",
        "category": "Concurrency & Locking",
        "difficulty": "Hard",
        "scenario": "Design a resilient schema and write the atomic transaction logic for reserving flash-sale inventory (e.g. 100 iPhone units with 50,000 concurrent purchase attempts) guaranteeing zero overselling.",
        "schema_definition": "CREATE TABLE inventory (\n  product_id BIGINT PRIMARY KEY,\n  total_stock INT NOT NULL,\n  reserved_stock INT NOT NULL DEFAULT 0,\n  version INT NOT NULL DEFAULT 1,\n  CONSTRAINT chk_stock CHECK (reserved_stock <= total_stock)\n);\n\nCREATE TABLE reservations (\n  id UUID PRIMARY KEY,\n  user_id BIGINT NOT NULL,\n  product_id BIGINT NOT NULL,\n  quantity INT NOT NULL,\n  status VARCHAR(20) DEFAULT 'HELD',\n  expires_at TIMESTAMP WITH TIME ZONE NOT NULL,\n  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()\n);",
        "solution_query": "-- Option 1: Atomic In-Place SQL Update (Fastest & Lock-free at row level)\nBEGIN;\nUPDATE inventory\nSET reserved_stock = reserved_stock + 1\nWHERE product_id = 99\n  AND (total_stock - reserved_stock) >= 1;\n-- Check affected rows: if rows_affected == 1 -> success, else -> SOLD OUT.\n\nINSERT INTO reservations (id, user_id, product_id, quantity, expires_at)\nVALUES (gen_random_uuid(), 1042, 99, 1, NOW() + INTERVAL '10 minutes');\nCOMMIT;",
        "explanation": "Atomic in-place `UPDATE inventory SET reserved_stock = reserved_stock + 1 WHERE (total_stock - reserved_stock) >= 1` relies on the database row lock during update evaluation. Eliminates race conditions without long SELECT FOR UPDATE locks.",
    },
]
