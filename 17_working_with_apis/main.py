# =============================================================
#  MODULE 17 — WORKING WITH APIs
#  Level: 🟠 Advanced
#  Goal:  HTTP requests, JSON APIs, error handling, pagination.
#  Note:  Run 'pip install requests' before running this.
# =============================================================

import json
import urllib.request
import urllib.error

print("=" * 55)
print("  MODULE 17 — WORKING WITH APIs")
print("=" * 55)

# ----- 1. WHAT IS AN API? -----
print("\n--- 1. What is an API? ---")
print("  API = Application Programming Interface")
print("  It lets your code talk to other services over HTTP.")
print("  You send a REQUEST and get back a RESPONSE (usually JSON).")

# ----- 2. HTTP METHODS -----
print("\n--- 2. HTTP Methods ---")
methods = {
    "GET":    "Retrieve data (read-only)",
    "POST":   "Create new data",
    "PUT":    "Update existing data (full replace)",
    "PATCH":  "Update existing data (partial)",
    "DELETE": "Remove data",
}
for method, desc in methods.items():
    print(f"    {method:<8} -> {desc}")

# ----- 3. STATUS CODES -----
print("\n--- 3. Common Status Codes ---")
codes = {
    200: "OK — Success",
    201: "Created — Resource created",
    400: "Bad Request — Client error",
    401: "Unauthorized — Need authentication",
    403: "Forbidden — Not allowed",
    404: "Not Found — Resource doesn't exist",
    500: "Server Error — Something broke on server",
}
for code, desc in codes.items():
    print(f"    {code} -> {desc}")

# ----- 4. MAKING A GET REQUEST (stdlib) -----
print("\n--- 4. GET Request (using stdlib) ---")

try:
    url = "https://jsonplaceholder.typicode.com/users/1"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=5) as response:
        data = json.loads(response.read().decode())
        print(f"  [OK] Status: {response.status}")
        print(f"  Name:    {data['name']}")
        print(f"  Email:   {data['email']}")
        print(f"  Company: {data['company']['name']}")
except urllib.error.URLError as e:
    print(f"  [!] Could not connect: {e}")
    print("  (This is normal if you're offline)")

# ----- 5. FETCHING A LIST -----
print("\n--- 5. Fetching a List ---")

try:
    url = "https://jsonplaceholder.typicode.com/posts?_limit=5"
    with urllib.request.urlopen(url, timeout=5) as response:
        posts = json.loads(response.read().decode())
        for post in posts:
            title = post['title'][:40]
            print(f"  [log] [{post['id']}] {title}...")
except urllib.error.URLError:
    print("  [!] Offline — skipping this example.")

# ----- 6. POST REQUEST -----
print("\n--- 6. POST Request (Create Data) ---")

try:
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = json.dumps({
        "title": "My Python Journey",
        "body": "Learning APIs is awesome!",
        "userId": 1,
    }).encode()

    req = urllib.request.Request(url, data=payload, method="POST")
    req.add_header("Content-Type", "application/json")

    with urllib.request.urlopen(req, timeout=5) as response:
        result = json.loads(response.read().decode())
        print(f"  [OK] Created post with id: {result['id']}")
        print(f"  Title: {result['title']}")
except urllib.error.URLError:
    print("  [!] Offline — skipping.")

# ----- 7. ERROR HANDLING FOR APIs -----
print("\n--- 7. Robust API Error Handling ---")

def safe_get(url):
    """Fetch URL with proper error handling."""
    try:
        with urllib.request.urlopen(url, timeout=5) as resp:
            return json.loads(resp.read().decode()), resp.status
    except urllib.error.HTTPError as e:
        return None, e.code
    except urllib.error.URLError as e:
        return None, f"Connection error: {e.reason}"
    except Exception as e:
        return None, f"Unexpected: {e}"

data, status = safe_get("https://jsonplaceholder.typicode.com/users/1")
print(f"  Valid URL:   status={status}, name={data['name'] if data else 'N/A'}")

data, status = safe_get("https://jsonplaceholder.typicode.com/users/9999")
print(f"  Bad URL:     status={status}")

# ----- 8. BUILDING YOUR OWN API WRAPPER -----
print("\n--- 8. API Wrapper Pattern ---")

class JSONPlaceholderAPI:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    @staticmethod
    def _get(endpoint):
        url = f"{JSONPlaceholderAPI.BASE_URL}{endpoint}"
        try:
            with urllib.request.urlopen(url, timeout=5) as resp:
                return json.loads(resp.read().decode())
        except Exception:
            return None

    @classmethod
    def get_user(cls, user_id):
        return cls._get(f"/users/{user_id}")

    @classmethod
    def get_posts(cls, limit=5):
        return cls._get(f"/posts?_limit={limit}")

api = JSONPlaceholderAPI()
user = api.get_user(2)
if user:
    print(f"  User 2: {user['name']} ({user['email']})")

print("\n" + "=" * 55)
print("  [TROPHY] CHALLENGES")
print("=" * 55)
print("  1. Build a weather checker using a free weather API")
print("  2. Create a GitHub user info fetcher")
print("  3. Build a dictionary lookup tool (free dictionary API)")
print("=" * 55)
