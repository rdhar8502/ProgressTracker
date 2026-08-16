# 🎯 Progress Tracker

A full-stack Python web application to track interview preparation progress for **Senior AI / Python Backend Engineer** abroad roles.

Built with **FastAPI + PostgreSQL + Docker** — one command to run.

---

## 🚀 Quick Start

```bash
# 1. Clone / navigate to this directory
cd ProgressTracker

# 2. Start everything with Docker Compose
docker-compose up --build

# 3. Open your browser
open http://localhost:15000
```

> **Ports used**: App → `15000`, PostgreSQL → `15432` (high ports to avoid conflicts)

---

## 🗂️ Features

| Module | Description |
|---|---|
| 📊 Dashboard | Total hours, streak, progress rings, daily/weekly charts |
| 📝 Daily Log | Multi-session per day — log any topic mix, track problems solved |
| 📅 Weekly View | 33 weeks (Aug 2026 → Mar 2027), Sun–Sat, auto-aggregated |
| 💻 DSA Tracker | 20 topics, problem log with pattern/mistake/complexity notes |
| 🏗️ System Design | 20 core concepts (96 sub-concepts) + 27 full case studies |
| 🤖 AI/LLM | 20 concepts with depth rating + interview talking points |
| 🐙 GitHub | 3 portfolio projects with task checklists |
| 📤 Applications | Job pipeline tracker with stage/visa/salary tracking |
| ⚙️ Settings | Edit profile, targets, dates — fully database-driven |

---

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python 3.12)
- **Database**: PostgreSQL 15 + SQLAlchemy ORM
- **Frontend**: Jinja2 templates + Vanilla CSS + Chart.js
- **Container**: Docker + docker-compose
- **Theme**: Light — warm cream, dark sidebar, violet accent

---

## ⚙️ Environment Variables

Copy `.env.example` to `.env` to customize:

```
DATABASE_URL=postgresql://tracker:tracker123@db:5432/progress_tracker
POSTGRES_USER=tracker
POSTGRES_PASSWORD=tracker123
POSTGRES_DB=progress_tracker
```

---

## 📅 Prep Plan

- **Start**: August 12, 2026  
- **Target**: March 2027  
- **Week 1 starts**: Sunday, August 16, 2026  
- **Daily target**: 1.5h weekdays · 4h Saturday · 3.5h Sunday (~15h/week)
