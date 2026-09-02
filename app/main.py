from datetime import date
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import FileResponse
import fastapi.templating

# Monkeypatch Jinja2Templates to inject global helper functions for all routers
_original_init = fastapi.templating.Jinja2Templates.__init__

def _patched_init(self, *args, **kwargs):
    _original_init(self, *args, **kwargs)
    self.env.globals["today"] = date.today()
    
    def get_user_gamification():
        from app.database import SessionLocal
        from app.services.gamification import get_gamification_state
        db = SessionLocal()
        try:
            return get_gamification_state(db)
        except Exception:
            return None
        finally:
            db.close()
            
    self.env.globals["user_gamification"] = get_user_gamification

fastapi.templating.Jinja2Templates.__init__ = _patched_init


from app.routers import dashboard, daily, weekly, dsa, system_design, database_track, ai_llm, github, applications, settings, personal_hub, search, achievements, destinations, eu_readiness, german_language, dutch_language, na_readiness

app = FastAPI(
    title="Progress Tracker",
    description="Interview Preparation Progress Tracker",
    version="1.0.0",
)

app.add_middleware(GZipMiddleware, minimum_size=1000)

# Static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="app/templates")



@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("app/static/favicon.svg", media_type="image/svg+xml")

# Include all routers
app.include_router(dashboard.router)
app.include_router(daily.router)
app.include_router(weekly.router)
app.include_router(dsa.router)
app.include_router(system_design.router)
app.include_router(database_track.router)
app.include_router(ai_llm.router)
app.include_router(github.router)
app.include_router(destinations.router)
app.include_router(applications.router)
app.include_router(settings.router)
app.include_router(personal_hub.router)
app.include_router(search.router)
app.include_router(achievements.router)
app.include_router(eu_readiness.router)
app.include_router(na_readiness.router)
app.include_router(na_readiness.alias_router)
app.include_router(german_language.router)
app.include_router(dutch_language.router)



