# =============================================================
#  MODULE 21 — WEB DEVELOPMENT WITH FLASK
#  Level: [ERR] Expert
#  Goal:  Build a REST API and web app with Flask.
#  Run:   pip install flask  ->  python main.py
# =============================================================

print("=" * 55)
print("  MODULE 21 — WEB DEVELOPMENT WITH FLASK")
print("=" * 55)
print("  This module creates a runnable Flask app.")
print("  Run: pip install flask")
print("  Then: python main.py")
print("  Visit: http://127.0.0.1:5000")
print("=" * 55)

try:
    from flask import Flask, jsonify, request, render_template_string
except ImportError:
    print("\n  [!]  Flask not installed. Run: pip install flask")
    print("  Showing code structure instead...\n")

    print("""
    # --- Flask App Structure ---

    from flask import Flask, jsonify, request
    app = Flask(__name__)

    # In-memory "database"
    tasks = []

    @app.route('/')
    def home():
        return '<h1>Welcome to PyMastery API</h1>'

    @app.route('/api/tasks', methods=['GET'])
    def get_tasks():
        return jsonify(tasks)

    @app.route('/api/tasks', methods=['POST'])
    def create_task():
        data = request.get_json()
        task = {
            'id': len(tasks) + 1,
            'title': data['title'],
            'done': False,
        }
        tasks.append(task)
        return jsonify(task), 201

    @app.route('/api/tasks/<int:task_id>', methods=['PUT'])
    def update_task(task_id):
        task = next((t for t in tasks if t['id'] == task_id), None)
        if not task:
            return jsonify({'error': 'Not found'}), 404
        data = request.get_json()
        task['title'] = data.get('title', task['title'])
        task['done'] = data.get('done', task['done'])
        return jsonify(task)

    @app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
    def delete_task(task_id):
        tasks[:] = [t for t in tasks if t['id'] != task_id]
        return '', 204

    if __name__ == '__main__':
        app.run(debug=True)
    """)
    exit()

# ---- ACTUAL FLASK APP ----

app = Flask(__name__)

# In-memory database
tasks = [
    {"id": 1, "title": "Learn Python basics", "done": True},
    {"id": 2, "title": "Build a REST API", "done": False},
    {"id": 3, "title": "Deploy to production", "done": False},
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>PyMastery Task API</title>
<style>
  body { font-family: 'Segoe UI', sans-serif; max-width: 700px;
         margin: 40px auto; background: #1a1a2e; color: #eee; padding: 20px; }
  h1 { color: #e94560; }
  .task { background: #16213e; padding: 12px; margin: 8px 0;
          border-radius: 8px; border-left: 4px solid #e94560; }
  .done { border-left-color: #0f3460; opacity: 0.6; }
  code { background: #0f3460; padding: 2px 6px; border-radius: 4px; }
  .endpoints { background: #16213e; padding: 15px; border-radius: 8px; }
</style></head>
<body>
  <h1>[py] PyMastery Task API</h1>
  <h2>Tasks</h2>
  {% for task in tasks %}
    <div class="task {{ 'done' if task.done }}">
      <strong>{{ task.title }}</strong>
      <span>{{ '[OK]' if task.done else '[wait]' }}</span>
    </div>
  {% endfor %}
  <h2>API Endpoints</h2>
  <div class="endpoints">
    <p><code>GET</code> /api/tasks — List all tasks</p>
    <p><code>POST</code> /api/tasks — Create a task</p>
    <p><code>PUT</code> /api/tasks/&lt;id&gt; — Update a task</p>
    <p><code>DELETE</code> /api/tasks/&lt;id&gt; — Delete a task</p>
  </div>
</body></html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE, tasks=tasks)

@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    task = {
        "id": max(t["id"] for t in tasks) + 1 if tasks else 1,
        "title": data["title"],
        "done": False,
    }
    tasks.append(task)
    return jsonify(task), 201

@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Not found"}), 404
    data = request.get_json()
    task["title"] = data.get("title", task["title"])
    task["done"] = data.get("done", task["done"])
    return jsonify(task)

@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks[:] = [t for t in tasks if t["id"] != task_id]
    return "", 204

if __name__ == "__main__":
    print("\n  >> Starting Flask server...")
    print("  [net] Visit: http://127.0.0.1:5000")
    print("  [net] API:   http://127.0.0.1:5000/api/tasks")
    print("  Press Ctrl+C to stop.\n")
    app.run(debug=True, port=5000)
