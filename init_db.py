"""
One-time database initialization script.
Run this before starting the app (handled by Dockerfile CMD).
"""
import sys
import time
import logging
from sqlalchemy import text
from alembic.config import Config
from alembic import command
from app.database import engine, Base, SessionLocal
from app.models import *  # noqa: F401, F403 - registers all models with Base
from app.services.seed import seed_database

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def wait_for_db(retries: int = 15, delay: int = 3):
    for attempt in range(retries):
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            logger.info("✅ Database connection established.")
            return
        except Exception as e:
            logger.warning(f"DB not ready (attempt {attempt + 1}/{retries}): {e}")
            time.sleep(delay)
    logger.error("❌ Could not connect to database after multiple retries.")
    sys.exit(1)


def run_migrations():
    logger.info("Checking database state and running migrations...")
    alembic_cfg = Config("alembic.ini")
    
    try:
        with engine.connect() as conn:
            # Check if alembic_version table exists
            has_alembic = conn.execute(text(
                "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'alembic_version')"
            )).scalar()
            
            # Check if other tables exist (e.g. user_profile)
            has_tables = conn.execute(text(
                "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'user_profile')"
            )).scalar()
            
        if not has_alembic and has_tables:
            logger.info("Database has existing tables but no Alembic history. Stamping to head revision...")
            command.stamp(alembic_cfg, "head")
            logger.info("✅ Database stamped to head revision.")
            
        logger.info("Running database upgrades to head...")
        command.upgrade(alembic_cfg, "head")
        logger.info("✅ Database migrations completed successfully.")
    except Exception as e:
        logger.error(f"❌ Error running migrations: {e}")
        logger.info("Falling back to Base.metadata.create_all...")
    
    # Always ensure any newly defined models/tables in Base are created
    Base.metadata.create_all(bind=engine)
    logger.info("✅ Base metadata tables verified/created.")


def init():
    wait_for_db()
    
    import os
    if os.getenv("DROP_TABLES") == "true":
        logger.info("DROP_TABLES is set to true. Dropping legacy/old tables for clean migration...")
        try:
            with engine.begin() as conn:
                conn.execute(text("DROP TABLE IF EXISTS daily_logs CASCADE"))
                conn.execute(text("DROP TABLE IF EXISTS ai_llm_topics CASCADE"))
                conn.execute(text("DROP TABLE IF EXISTS system_design_sub_concepts CASCADE"))
                conn.execute(text("DROP TABLE IF EXISTS system_design_concepts CASCADE"))
                conn.execute(text("DROP TABLE IF EXISTS system_design_topics CASCADE"))
                logger.info("✅ Dropped old tables.")
        except Exception as e:
            logger.warning(f"Could not drop old tables: {e}")
    else:
        logger.info("Skipping table drop (normal startup).")

    run_migrations()
    
    # Run schema migration for many-to-many DSA topics and category column
    try:
        with engine.begin() as conn:
            # Check if topic_id column exists in dsa_problems
            res = conn.execute(text(
                "SELECT column_name FROM information_schema.columns "
                "WHERE table_name='dsa_problems' AND column_name='topic_id'"
            )).fetchone()
            if res:
                logger.info("Migrating topic_id from dsa_problems to dsa_problem_topics...")
                # Copy existing data
                conn.execute(text(
                    "INSERT INTO dsa_problem_topics (problem_id, topic_id) "
                    "SELECT id, topic_id FROM dsa_problems "
                    "WHERE topic_id IS NOT NULL "
                    "ON CONFLICT DO NOTHING"
                ))
                # Drop constraint and column topic_id with CASCADE
                conn.execute(text(
                    "ALTER TABLE dsa_problems DROP COLUMN IF EXISTS topic_id CASCADE"
                ))
                logger.info("✅ Migration of topic_id complete.")

            # Check if category column exists in dsa_problems
            res_cat = conn.execute(text(
                "SELECT column_name FROM information_schema.columns "
                "WHERE table_name='dsa_problems' AND column_name='category'"
            )).fetchone()
            if not res_cat:
                logger.info("Adding category column to dsa_problems...")
                conn.execute(text(
                    "ALTER TABLE dsa_problems ADD COLUMN category VARCHAR(100) DEFAULT 'Arrays and Strings'"
                ))
                conn.execute(text(
                    """
                    UPDATE dsa_problems
                    SET category = (
                        SELECT t.name
                        FROM dsa_problem_topics pt
                        JOIN dsa_topics t ON pt.topic_id = t.id
                        WHERE pt.problem_id = dsa_problems.id
                        LIMIT 1
                    )
                    WHERE category IS NULL OR category = '';
                    """
                ))
                conn.execute(text(
                    "UPDATE dsa_problems SET category = 'Arrays and Strings' WHERE category IS NULL OR category = '';"
                ))
                logger.info("✅ Added category column to dsa_problems.")

            # Create dsa_companies and dsa_problem_companies if they don't exist
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS dsa_companies (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL UNIQUE,
                    order_index INTEGER DEFAULT 0
                );
                CREATE TABLE IF NOT EXISTS dsa_problem_companies (
                    problem_id INTEGER NOT NULL REFERENCES dsa_problems(id) ON DELETE CASCADE,
                    company_id INTEGER NOT NULL REFERENCES dsa_companies(id) ON DELETE CASCADE,
                    PRIMARY KEY (problem_id, company_id)
                );
            """))
            logger.info("✅ Verified dsa_companies and dsa_problem_companies tables.")

            # Check track column in system_design_concepts
            res_sd_track = conn.execute(text(
                "SELECT column_name FROM information_schema.columns "
                "WHERE table_name='system_design_concepts' AND column_name='track'"
            )).fetchone()
            if not res_sd_track:
                logger.info("Adding track column to system_design_concepts...")
                conn.execute(text(
                    "ALTER TABLE system_design_concepts ADD COLUMN track VARCHAR(20) DEFAULT 'HLD'"
                ))
                logger.info("✅ Added track column to system_design_concepts.")

            # Check track and category columns in system_design_cases
            res_case_track = conn.execute(text(
                "SELECT column_name FROM information_schema.columns "
                "WHERE table_name='system_design_cases' AND column_name='track'"
            )).fetchone()
            if not res_case_track:
                logger.info("Adding track column to system_design_cases...")
                conn.execute(text(
                    "ALTER TABLE system_design_cases ADD COLUMN track VARCHAR(20) DEFAULT 'HLD'"
                ))
                logger.info("✅ Added track column to system_design_cases.")

            res_case_cat = conn.execute(text(
                "SELECT column_name FROM information_schema.columns "
                "WHERE table_name='system_design_cases' AND column_name='category'"
            )).fetchone()
            if not res_case_cat:
                logger.info("Adding category column to system_design_cases...")
                conn.execute(text(
                    "ALTER TABLE system_design_cases ADD COLUMN category VARCHAR(100) DEFAULT 'Distributed Systems'"
                ))
                logger.info("✅ Added category column to system_design_cases.")

            # Verify columns on relocation_destinations
            dest_cols = [
                ("quality_of_life_rank", "VARCHAR(50) DEFAULT ''"),
                ("happiness_rank", "VARCHAR(50) DEFAULT ''"),
                ("safety_score", "VARCHAR(100) DEFAULT ''"),
                ("retirement_suitability", "TEXT DEFAULT ''"),
                ("scenic_pollution_rating", "TEXT DEFAULT ''"),
                ("peaceful_scenic_motivation", "TEXT DEFAULT ''"),
                ("best_cities_states", "TEXT DEFAULT ''"),
                ("keep_in_mind_notes", "TEXT DEFAULT ''"),
            ]
            for col_name, col_type in dest_cols:
                res_col = conn.execute(text(
                    f"SELECT column_name FROM information_schema.columns "
                    f"WHERE table_name='relocation_destinations' AND column_name='{col_name}'"
                )).fetchone()
                if not res_col:
                    conn.execute(text(
                        f"ALTER TABLE relocation_destinations ADD COLUMN IF NOT EXISTS {col_name} {col_type}"
                    ))
            logger.info("✅ Verified relocation_destinations columns.")
    except Exception as e:
        logger.error(f"Error migrating database schema: {e}")

    db = SessionLocal()
    try:
        logger.info("Seeding initial data...")
        seed_database(db)
    finally:
        db.close()


if __name__ == "__main__":
    init()
