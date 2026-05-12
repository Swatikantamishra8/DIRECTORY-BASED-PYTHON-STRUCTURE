# Python Mastery -- Zero to Expert

> A complete, code-ready learning ecosystem.
> Every folder is a lesson. Every file runs. Every concept builds on the last.

---

## Roadmap

### Phase 1: Foundation (Beginner)

| #  | Module               | Key Topics                                      | Run Command          |
|----|----------------------|-------------------------------------------------|----------------------|
| 01 | Setup                | Environment, first script, input/output         | `python main.py`     |
| 02 | Variables & Types    | Strings, ints, floats, type conversion          | `python main.py`     |
| 03 | Operators            | Arithmetic, comparison, logical, bitwise        | `python main.py`     |
| 04 | Strings Deep Dive    | Slicing, methods, formatting, raw strings       | `python main.py`     |
| 05 | Control Flow         | if/elif/else, ternary, match-case, truthy/falsy | `python main.py`     |
| 06 | Loops                | for, while, range, enumerate, zip, break        | `python main.py`     |

### Phase 2: Core Skills (Intermediate)

| #  | Module               | Key Topics                                      | Run Command          |
|----|----------------------|-------------------------------------------------|----------------------|
| 07 | Functions            | args, kwargs, lambda, recursion, type hints      | `python main.py`     |
| 08 | Data Structures      | Lists, tuples, dicts, sets, comprehensions       | `python main.py`     |
| 09 | File Handling        | Read, write, CSV, JSON, context managers         | `python main.py`     |
| 10 | Error Handling       | try/except, custom exceptions, logging           | `python main.py`     |
| 11 | Modules & Packages   | Imports, pip, venv, __name__, packages           | `python main.py`     |
| 12 | OOP Basics           | Classes, __init__, encapsulation, @property      | `python main.py`     |

### Phase 3: Advanced Python

| #  | Module                  | Key Topics                                    | Run Command          |
|----|-------------------------|-----------------------------------------------|----------------------|
| 13 | OOP Advanced            | Inheritance, polymorphism, ABCs, dataclasses   | `python main.py`     |
| 14 | Decorators & Generators | Closures, @decorator, yield, itertools         | `python main.py`     |
| 15 | Functional Programming  | map, filter, reduce, partial, compose          | `python main.py`     |
| 16 | Regular Expressions     | Pattern matching, groups, substitution         | `python main.py`     |
| 17 | Working with APIs       | HTTP methods, JSON APIs, error handling        | `python main.py`     |
| 18 | Database (SQLite)       | SQL, CRUD, aggregates, row factory             | `python main.py`     |

### Phase 4: Expert & Real-World

| #  | Module                  | Key Topics                                    | Run Command          |
|----|-------------------------|-----------------------------------------------|----------------------|
| 19 | Testing                 | unittest, mocking, TDD                         | `python main.py`     |
| 20 | Concurrency             | Threading, multiprocessing, asyncio            | `python main.py`     |
| 21 | Web Development (Flask) | Routes, REST API, templates                    | `python main.py`     |
| 22 | Data Analysis (Pandas)  | DataFrames, groupby, cleaning, export          | `python main.py`     |
| 23 | Automation & Scripting  | File org, log analysis, backup, scheduling     | `python main.py`     |
| 24 | Design Patterns         | Singleton, Factory, Observer, Strategy         | `python main.py`     |
| 25 | Capstone Projects       | 5 portfolio-grade projects with starter code   | `python main.py`     |

---

## How to Use

```bash
cd 03_operators
python main.py
```

Work through each folder in order. Read the comments. Run the code. Modify it. Break it. Fix it.

---

## Dependency Graph

```
Phase 1 (Foundation)
  01 -> 02 -> 03 -> 04 -> 05 -> 06

Phase 2 (Core)
  06 -> 07 -> 08 -> 09 -> 10 -> 11 -> 12

Phase 3 (Advanced)
  12 -> 13 -> 14 -> 15
  09 -> 16
  07 -> 17 -> 18

Phase 4 (Expert)
  18 -> 19
  07 -> 20
  18 -> 21
  09 -> 22
  09 -> 23
  13 -> 24
  All -> 25 (Capstone)
```

---

## Prerequisites

- Python 3.10+ installed (modules use match-case)
- A code editor (VS Code recommended)
- Terminal / Command Prompt

### Optional (for specific modules)

| Module | Install Command           |
|--------|---------------------------|
| 21     | `pip install flask`       |
| 22     | `pip install pandas`      |

---

## Project Structure

```
Python/
|-- README.md                     <-- You are here
|-- 01_setup/main.py
|-- 02_/main.py
|-- 03_operators/main.py
|-- 04_strings/main.py
|-- 05_control_flow/main.py
|-- 06_loops/main.py
|-- 07_functions/main.py
|-- 08_data_structures/main.py
|-- 09_file_handling/main.py
|-- 10_error_handling/main.py
|-- 11_modules_packages/main.py
|-- 12_oop_basics/main.py
|-- 13_oop_advanced/main.py
|-- 14_decorators_generators/main.py
|-- 15_functional_programming/main.py
|-- 16_regular_expressions/main.py
|-- 17_working_with_apis/main.py
|-- 18_database/main.py
|-- 19_testing/main.py
|-- 20_concurrency/main.py
|-- 21_web_flask/main.py
|-- 22_data_analysis_pandas/main.py
|-- 23_automation_scripting/main.py
|-- 24_design_patterns/main.py
|-- 25_capstone_projects/main.py
```

---

## By the End You Will

- Write production-quality Python code
- Build REST APIs with Flask
- Work with databases (SQLite, SQL)
- Analyze data with Pandas
- Automate tasks and scripts
- Understand OOP, design patterns, and concurrency
- Test code with unittest and mocking
- Have 5+ portfolio projects ready for interviews

---

## Career Path Mapping

| Skill Level        | Modules Completed | Roles You Can Target              |
|--------------------|-------------------|-----------------------------------|
| Beginner           | 01 - 06           | Intern, Junior Script Writer      |
| Intermediate       | 07 - 12           | Junior Python Developer           |
| Advanced           | 13 - 18           | Mid-Level Backend Developer       |
| Expert             | 19 - 25           | Senior Engineer, Tech Lead        |

---

## Capstone Projects (Module 25)

1. **CLI Task Manager** -- Python + JSON + argparse
2. **Student Grade Tracker** -- OOP + SQLite
3. **REST API + Web Dashboard** -- Flask + SQLite + HTML
4. **Data Pipeline & Analyzer** -- Pandas + Matplotlib + CSV
5. **Microservice Architecture** -- Flask + Docker + Redis

---

> "The best way to learn to code is to code."
> Start with Module 01. Run it. Then move to the next.
