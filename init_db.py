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
    
    db = SessionLocal()
    try:
        logger.info("Seeding initial data...")
        seed_database(db)
    finally:
        db.close()


if __name__ == "__main__":
    init()
