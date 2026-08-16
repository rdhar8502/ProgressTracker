# 🎯 Progress Tracker

**Progress Tracker** is a full‑stack Python web application designed to help interview candidates **track their preparation progress** for senior AI / Python backend engineering roles. It provides a comprehensive dashboard for daily logs, DSA tracking, system design studies, AI/LLM concepts, and job application management—all powered by **FastAPI**, **PostgreSQL**, and **Docker**.

---

## ✨ SEO Keywords

* interview preparation tracker
* AI engineer progress dashboard
* Python backend interview tracker
* DSA practice log
* system design study manager
* job application pipeline
* Dockerized FastAPI app
* open‑source interview tracker

---

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/rdhar8502/ProgressTracker.git
cd ProgressTracker

# 2. Copy example environment variables and customise if needed
cp .env.example .env

# 3. Build and launch the app with Docker Compose (one‑command setup)
 docker-compose up --build -d
```

Open your browser and navigate to:

```
http://localhost:15000
```

> **Ports used**: Application → `15000`, PostgreSQL → `15432` (high ports avoid conflicts)

---

## 🛠️ Installation Options

### Docker (recommended)
The Docker setup bundles the FastAPI backend, PostgreSQL database, and the web UI. It ensures a consistent environment across macOS, Linux, and Windows.

### Local Python Environment
If you prefer a native Python setup:

```bash
# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialise the database
python init_db.py

# Run the FastAPI server
uvicorn app.main:app --reload --port 15000
```

---

## 📦 Features

| Module | Description |
|---|---|
| 📊 Dashboard | Total hours, streak, progress rings, daily/weekly charts |
| 📝 Daily Log | Multi‑session per day – log any topic mix, track problems solved |
| 📅 Weekly View | 33 weeks (Aug 2026 → Mar 2027), Sun‑Sat, auto‑aggregated |
| 💻 DSA Tracker | 20 topics, problem log with pattern/mistake/complexity notes |
| 🏗️ System Design | 20 core concepts (96 sub‑concepts) + 27 full case studies |
| 🤖 AI/LLM | 20 concepts with depth rating + interview talking points |
| 🐙 GitHub | 3 portfolio projects with task checklists |
| 📤 Applications | Job pipeline tracker with stage/visa/salary tracking |
| ⚙️ Settings | Edit profile, targets, dates — fully database‑driven |

---

## 💻 Tech Stack

- **Backend**: FastAPI (Python 3.12) – high‑performance async API
- **Database**: PostgreSQL 15 + SQLAlchemy ORM – robust relational storage
- **Frontend**: Jinja2 templates, vanilla CSS, Chart.js – lightweight, no heavy JS frameworks
- **Containerisation**: Docker + Docker‑Compose – one‑click environment
- **Theme**: Light warm‑cream background, dark sidebar, violet accent for a modern look

---

## 🌱 Environment Variables

Copy the example file and adjust values as required:

```dotenv
DATABASE_URL=postgresql://tracker:tracker123@db:5432/progress_tracker
POSTGRES_USER=tracker
POSTGRES_PASSWORD=tracker123
POSTGRES_DB=progress_tracker
```

---

## 📅 Prep Plan (example)

- **Start**: August 12 2026
- **Target**: March 2027
- **Week 1 starts**: Sunday, August 16 2026
- **Daily target**: 1.5 h weekdays · 4 h Saturday · 3.5 h Sunday (~15 h/week)

---

## 🤝 Contributing

Contributions are welcome! Fork the repo, create a feature branch, and submit a pull request. Please ensure your code follows the existing style and includes tests where appropriate.

---

## 📜 License

This project is licensed under the **MIT License** – see the `LICENSE` file for details.

---

## 📸 Screenshots

![Progress Tracker Dashboard](file:///Users/rahuldhar/.gemini/antigravity-ide/brain/6ac071d7-59c9-46e1-a422-44e2a5fbb1e7/progress_tracker_dashboard_1786858741781.jpg)

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
