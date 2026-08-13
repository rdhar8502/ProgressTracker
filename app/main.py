from datetime import date
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.gzip import GZipMiddleware

from app.routers import dashboard, daily, weekly, dsa, system_design, ai_llm, github, applications, settings

app = FastAPI(
    title="Progress Tracker",
    description="Interview Preparation Progress Tracker",
    version="1.0.0",
)

app.add_middleware(GZipMiddleware, minimum_size=1000)

# Static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Set up Jinja2 global — inject today() as a callable into every template
templates = Jinja2Templates(directory="app/templates")
templates.env.globals["today"] = date.today()   # static for this session; resets on container restart

# Include all routers
app.include_router(dashboard.router)
app.include_router(daily.router)
app.include_router(weekly.router)
app.include_router(dsa.router)
app.include_router(system_design.router)
app.include_router(ai_llm.router)
app.include_router(github.router)
app.include_router(applications.router)
app.include_router(settings.router)
