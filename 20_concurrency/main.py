# =============================================================
#  MODULE 20 -- CONCURRENCY
#  Level: Expert
#  Goal:  Threading, Multiprocessing, Asyncio.
# =============================================================

import threading
import asyncio
import time
import concurrent.futures


def download_page(url, delay):
    print(f"    [wait] Downloading {url}...")
    time.sleep(delay)
    print(f"    [OK] Done: {url}")


def fetch_data(item_id):
    time.sleep(0.5)
    return f"Data-{item_id}"


def cpu_heavy(n):
    """Simulate CPU work."""
    return sum(i * i for i in range(n))


async def async_download(name, delay):
    print(f"    [wait] Starting {name}...")
    await asyncio.sleep(delay)
    print(f"    [OK] Finished {name}")
    return f"{name}-done"


async def async_main():
    start = time.perf_counter()
    results = await asyncio.gather(
        async_download("API-1", 1),
        async_download("API-2", 1.5),
        async_download("API-3", 0.8),
    )
    elapsed = time.perf_counter() - start
    print(f"  Results: {results}")
    print(f"  [time]  Asyncio took {elapsed:.2f}s")


def safe_increment(lock, shared):
    for _ in range(100_000):
        with lock:
            shared[0] += 1


# On Windows, multiprocessing requires this guard
if __name__ == "__main__":

    print("=" * 55)
    print("  MODULE 20 -- CONCURRENCY")
    print("=" * 55)

    # ----- 1. WHY CONCURRENCY? -----
    print("\n--- 1. Why Concurrency? ---")
    print("  CPU-bound -> multiprocessing (parallel cores)")
    print("  I/O-bound -> threading or asyncio (waiting for network/disk)")

    # ----- 2. THREADING -----
    print("\n--- 2. Threading (I/O-bound tasks) ---")

    start = time.perf_counter()
    threads = []
    urls = [("page1.html", 1), ("page2.html", 1.5), ("page3.html", 0.8)]
    for url, delay in urls:
        t = threading.Thread(target=download_page, args=(url, delay))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    elapsed = time.perf_counter() - start
    print(f"  [time]  Threading took {elapsed:.2f}s (vs ~3.3s sequential)")

    # ----- 3. THREAD POOL -----
    print("\n--- 3. ThreadPoolExecutor ---")

    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        futures = [pool.submit(fetch_data, i) for i in range(8)]
        results = [f.result() for f in futures]
    elapsed = time.perf_counter() - start
    print(f"  Results: {results}")
    print(f"  [time]  Pool took {elapsed:.2f}s")

    # ----- 4. MULTIPROCESSING -----
    print("\n--- 4. Multiprocessing (CPU-bound tasks) ---")

    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as pool:
        futures = [pool.submit(cpu_heavy, 500_000) for _ in range(4)]
        results = [f.result() for f in futures]
    elapsed = time.perf_counter() - start
    print(f"  4 CPU tasks completed in {elapsed:.2f}s")

    # ----- 5. ASYNCIO -----
    print("\n--- 5. Asyncio (Modern Async) ---")
    asyncio.run(async_main())

    # ----- 6. THREAD SAFETY -----
    print("\n--- 6. Thread Safety (Locks) ---")

    shared = [0]  # Use a list so threads can mutate
    lock = threading.Lock()

    t1 = threading.Thread(target=safe_increment, args=(lock, shared))
    t2 = threading.Thread(target=safe_increment, args=(lock, shared))
    t1.start(); t2.start()
    t1.join(); t2.join()
    print(f"  Counter (with lock): {shared[0]} (should be 200,000)")

    # ----- 7. WHEN TO USE WHAT -----
    print("\n--- 7. Decision Guide ---")
    guide = {
        "Network/API calls": "asyncio or threading",
        "File downloads":    "threading",
        "CPU math/analysis": "multiprocessing",
        "Web scraping":      "asyncio + aiohttp",
        "Simple scripts":    "sequential is fine!",
    }
    for task, solution in guide.items():
        print(f"    {task:<22} -> {solution}")

    print("\n" + "=" * 55)
    print("  [TROPHY] CHALLENGES")
    print("=" * 55)
    print("  1. Async web scraper (fetch 10 URLs concurrently)")
    print("  2. Parallel image processor with multiprocessing")
    print("  3. Producer-consumer pattern with threading.Queue")
    print("=" * 55)
