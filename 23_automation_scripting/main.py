# =============================================================
#  MODULE 23 — AUTOMATION & SCRIPTING
#  Level: [ERR] Expert
#  Goal:  OS automation, web scraping, scheduling.
# =============================================================

import os
import shutil
import glob
import subprocess
import datetime

print("=" * 55)
print("  MODULE 23 — AUTOMATION & SCRIPTING")
print("=" * 55)

# ----- 1. FILE SYSTEM OPERATIONS -----
print("\n--- 1. File System Automation ---")

# Create directory structure
base = "temp_files/auto_demo"
for folder in ["documents", "images", "logs"]:
    os.makedirs(f"{base}/{folder}", exist_ok=True)
print(f"  [OK] Created directory tree at {base}/")

# Create sample files
for i in range(3):
    with open(f"{base}/documents/note_{i}.txt", "w") as f:
        f.write(f"Note #{i} created at {datetime.datetime.now()}\n")
print(f"  [OK] Created 3 sample text files.")

# List files
print("\n  Files in documents/:")
for filepath in glob.glob(f"{base}/documents/*.txt"):
    size = os.path.getsize(filepath)
    print(f"    [doc] {os.path.basename(filepath)} ({size} bytes)")

# ----- 2. FILE ORGANIZER -----
print("\n--- 2. File Organizer (by extension) ---")

def organize_files(source_dir, dest_dir):
    """Move files into sub-folders based on their extension."""
    ext_map = {
        ".txt": "text_files",
        ".py":  "python_files",
        ".csv": "data_files",
        ".json": "data_files",
        ".jpg": "images",
        ".png": "images",
    }

    organized = 0
    for filepath in glob.glob(f"{source_dir}/*.*"):
        ext = os.path.splitext(filepath)[1].lower()
        folder = ext_map.get(ext, "other")
        target = os.path.join(dest_dir, folder)
        os.makedirs(target, exist_ok=True)
        # In a real script you'd use shutil.move()
        organized += 1
        print(f"    Would move: {os.path.basename(filepath)} -> {folder}/")

    return organized

count = organize_files(f"{base}/documents", f"{base}/organized")
print(f"  Would organize {count} files.")

# ----- 3. LOG ANALYZER -----
print("\n--- 3. Log Analyzer ---")

# Create sample log
log_path = f"{base}/logs/app.log"
sample_logs = [
    "2026-05-13 10:00:01 INFO  Server started on port 8080",
    "2026-05-13 10:00:15 WARN  Slow query detected (2.3s)",
    "2026-05-13 10:01:02 ERROR Database connection timeout",
    "2026-05-13 10:01:03 ERROR Retry failed after 3 attempts",
    "2026-05-13 10:02:00 INFO  Connection re-established",
    "2026-05-13 10:05:00 WARN  Memory usage at 85%",
]

with open(log_path, "w") as f:
    f.write("\n".join(sample_logs))

# Analyze
with open(log_path) as f:
    lines = f.readlines()

stats = {"INFO": 0, "WARN": 0, "ERROR": 0}
errors = []
for line in lines:
    for level in stats:
        if level in line:
            stats[level] += 1
            if level == "ERROR":
                errors.append(line.strip())

print(f"  Log Analysis:")
for level, count in stats.items():
    icon = {"INFO": "[OK]", "WARN": "[WARN]", "ERROR": "[ERR]"}[level]
    print(f"    {icon} {level}: {count}")
print(f"\n  Error Details:")
for err in errors:
    print(f"    [X] {err}")

# ----- 4. SYSTEM INFO COLLECTOR -----
print("\n--- 4. System Info ---")

import platform

info = {
    "OS":         platform.system(),
    "OS Version": platform.version(),
    "Machine":    platform.machine(),
    "Processor":  platform.processor()[:40] if platform.processor() else "N/A",
    "Python":     platform.python_version(),
    "CWD":        os.getcwd(),
}
for key, val in info.items():
    print(f"    {key:<12}: {val}")

# ----- 5. SCHEDULED TASK SIMULATOR -----
print("\n--- 5. Task Scheduler (Concept) ---")

import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)

def scheduled_task(name):
    print(f"    [clock] [{datetime.datetime.now().strftime('%H:%M:%S')}] Running: {name}")

# Schedule 3 tasks at 0.5s intervals
for i in range(3):
    scheduler.enter(i * 0.3, 1, scheduled_task, (f"Task-{i+1}",))

scheduler.run()

# ----- 6. BACKUP SCRIPT -----
print("\n--- 6. Backup Script ---")

def create_backup(source, backup_dir):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}"
    backup_path = os.path.join(backup_dir, backup_name)

    if os.path.exists(source):
        shutil.copytree(source, backup_path)
        print(f"  [OK] Backup created: {backup_path}")
        return backup_path
    else:
        print(f"  [X] Source not found: {source}")
        return None

create_backup(f"{base}/documents", f"{base}/backups")

# Cleanup
print("\n  [TIP] Temp files in temp_files/auto_demo/")

print("\n" + "=" * 55)
print("  [TROPHY] CHALLENGES")
print("=" * 55)
print("  1. Build a duplicate file finder")
print("  2. Create an auto file renamer (batch rename)")
print("  3. Build a folder watcher that reacts to new files")
print("=" * 55)
