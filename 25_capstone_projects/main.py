# =============================================================
#  MODULE 25 — CAPSTONE PROJECTS
#  Level: [ERR] Expert
#  Goal:  5 portfolio-grade projects combining all skills.
# =============================================================

print("=" * 55)
print("  MODULE 25 — CAPSTONE PROJECTS")
print("=" * 55)

print("""
  This module contains 5 capstone project descriptions.
  Each project is designed to combine multiple skills
  from the roadmap into a portfolio-worthy application.

  ======================================================

  [pkg] PROJECT 1: CLI Task Manager (Beginner+)
  ---------------------------------------------
  Skills:  Modules 01-10 (basics through file handling)
  Stack:   Python, JSON, argparse
  Features:
    • Add / list / complete / delete tasks
    • Persistent storage with JSON files
    • Priority levels and due dates
    • Color-coded terminal output
    • Search and filter tasks
  Concepts: File I/O, data structures, CLI design

  ======================================================

  [pkg] PROJECT 2: Student Grade Tracker (Intermediate)
  -----------------------------------------------------
  Skills:  Modules 12-13, 18 (OOP + Database)
  Stack:   Python, SQLite, OOP
  Features:
    • Student CRUD operations
    • Grade calculation (GPA, percentages)
    • Class statistics and reports
    • Export to CSV
    • Data validation with custom exceptions
  Concepts: OOP, SQL, error handling, data export

  ======================================================

  [pkg] PROJECT 3: REST API + Web Dashboard (Advanced)
  --------------------------------------------------
  Skills:  Modules 18, 21 (Database + Flask)
  Stack:   Flask, SQLite, HTML/CSS, REST
  Features:
    • Full CRUD REST API
    • Web dashboard with charts
    • Authentication (JWT)
    • Rate limiting
    • API documentation (Swagger)
    • Unit tests with pytest
  Concepts: API design, web development, auth, testing

  ======================================================

  [pkg] PROJECT 4: Data Pipeline & Analyzer (Advanced)
  --------------------------------------------------
  Skills:  Modules 09, 16, 22, 23 (Files + Regex + Pandas)
  Stack:   Pandas, Matplotlib, CSV, scheduling
  Features:
    • Ingest data from multiple CSV sources
    • Clean and transform with Pandas
    • Generate statistical reports
    • Visualize trends with charts
    • Schedule automated runs
    • Email summary reports
  Concepts: ETL, data analysis, automation, visualization

  ======================================================

  [pkg] PROJECT 5: Microservice Architecture (Expert)
  -------------------------------------------------
  Skills:  Modules 17, 20, 21, 24 (APIs + Concurrency + Patterns)
  Stack:   Flask, Redis, Docker, pytest
  Features:
    • 3 independent microservices
    • API Gateway pattern
    • Message queue communication
    • Health checks and monitoring
    • Docker containerization
    • CI/CD with GitHub Actions
  Concepts: Microservices, containers, CI/CD, patterns

  ======================================================

  [grad] GRADUATION CHECKLIST
  ------------------------
  After completing these projects, you will have:

  [OK] Strong Python fundamentals
  [OK] Database design skills
  [OK] REST API development experience
  [OK] Testing and CI/CD knowledge
  [OK] Data analysis capabilities
  [OK] Architecture understanding
  [OK] 5 portfolio projects for interviews
  [OK] Production-grade coding habits

  Start with Project 1 and work your way up!
""")

# ----- Quick Start: Project 1 Skeleton -----
print("=" * 55)
print("  >> QUICK START: Project 1 Skeleton")
print("=" * 55)

import json
import os
from datetime import datetime

class TaskManager:
    """A simple CLI task manager with JSON persistence."""

    def __init__(self, filepath="tasks.json"):
        self.filepath = filepath
        self.tasks = self._load()

    def _load(self):
        if os.path.exists(self.filepath):
            with open(self.filepath) as f:
                return json.load(f)
        return []

    def _save(self):
        with open(self.filepath, "w") as f:
            json.dump(self.tasks, f, indent=2)

    def add(self, title, priority="medium"):
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "priority": priority,
            "done": False,
            "created": datetime.now().isoformat(),
        }
        self.tasks.append(task)
        self._save()
        return task

    def list_all(self):
        for t in self.tasks:
            status = "[OK]" if t["done"] else "[wait]"
            print(f"  {status} [{t['id']}] {t['title']} ({t['priority']})")

    def complete(self, task_id):
        for t in self.tasks:
            if t["id"] == task_id:
                t["done"] = True
                self._save()
                return True
        return False

# Demo
tm = TaskManager("temp_files/tasks.json")
os.makedirs("temp_files", exist_ok=True)

tm.add("Learn Python basics", "high")
tm.add("Build a REST API", "medium")
tm.add("Deploy to cloud", "low")
tm.complete(1)

print("\n  [list] Your Tasks:")
tm.list_all()

# Cleanup
if os.path.exists("temp_files/tasks.json"):
    os.remove("temp_files/tasks.json")

print("\n  [TIP] Expand this skeleton into a full CLI app!")
print("=" * 55)
