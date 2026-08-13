"""
One-time database initialization script.
Run this before starting the app (handled by Dockerfile CMD).
"""
import sys
import time
import logging
from sqlalchemy import text
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


def init():
    wait_for_db()
    logger.info("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    logger.info("✅ Tables created.")
    
    # Run schema migration for many-to-many DSA topics
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
