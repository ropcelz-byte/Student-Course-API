import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

COURSES = [
    {
        "id": 1,
        "code": "CS101",
        "name": "Introduction to Programming",
        "description": "Learn programming fundamentals, problem-solving, and basic Python."
    },
    {
        "id": 2,
        "code": "WEB201",
        "name": "Web Development Fundamentals",
        "description": "Explore HTML, CSS, JavaScript, and the foundations of modern web apps."
    },
    {
        "id": 3,
        "code": "DB202",
        "name": "Database Systems",
        "description": "Understand relational databases, SQL queries, and data modeling."
    },
    {
        "id": 4,
        "code": "NET210",
        "name": "Computer Networks",
        "description": "Study network protocols, addressing, routing, and network security basics."
    },
    {
        "id": 5,
        "code": "SE301",
        "name": "Software Engineering",
        "description": "Learn software development life cycles, requirements, testing, and teamwork."
    },
    {
        "id": 6,
        "code": "AI310",
        "name": "Foundations of Artificial Intelligence",
        "description": "Discover search, reasoning, machine learning concepts, and responsible AI."
    }
]


@app.get("/")
def homepage():
    """Simple human-friendly API landing page."""
    endpoint_data = [
        ("GET", "/api/health", "Check whether the API is running."),
        ("GET", "/api/courses", "Retrieve all available courses."),
        ("GET", "/api/courses/1", "Retrieve the course with ID 1."),
        ("GET", "/api/courses/9999", "Example of a course-not-found response.")
    ]
    return """
    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Student Course API</title>
      <style>
        :root { color-scheme: light; }
        body {
          font: 16px/1.6 system-ui, sans-serif;
          margin: 0;
          color: #eaf0ff;
          background:
            radial-gradient(ellipse at top left, rgba(45, 91, 160, .35), transparent 48%),
            linear-gradient(135deg, #101827 0%, #172b45 52%, #0b1423 100%);
          min-height: 100vh;
        }
        main { max-width: 900px; margin: 40px auto; padding: 0 20px; }
        .panel {
          background: rgba(255, 255, 255, .97);
          color: #172033;
          padding: 24px;
          margin: 18px 0;
          border: 1px solid rgba(255, 255, 255, .18);
          border-radius: 14px;
          box-shadow: 0 12px 34px rgba(0, 0, 0, .22);
        }
        h1 { margin-bottom: 4px; } h2 { margin-top: 0; }
        .status { display: inline-flex; gap: 8px; align-items: center; color: #137547; font-weight: 700; }
        .dot { width: 10px; height: 10px; border-radius: 50%; background: #20a464; }
        code { background: #eef2f8; padding: 3px 7px; border-radius: 5px; }
        li { margin: 9px 0; } pre { overflow-x: auto; padding: 14px; border-radius: 8px; background: #101827; color: #e8eef9; }
      </style>
    </head>
    <body><main>
      <section class="panel">
        <h1>Student Course API</h1>
        <p>A lightweight REST API built with Python and Flask. It provides fictional course data in JSON format.</p>
        <p class="status"><span class="dot"></span> API status: Operational</p>
      </section>
      <section class="panel">
        <h2>Available endpoints</h2>
        <ul>
          <li><code>GET /api/health</code> — Check API service status.</li>
          <li><code>GET /api/courses</code> — List all courses.</li>
          <li><code>GET /api/courses/1</code> — Get course ID 1.</li>
          <li><code>GET /api/courses/9999</code> — Example not-found response (HTTP 404).</li>
        </ul>
      </section>
      <section class="panel">
        <h2>Example JSON responses</h2>
        <h3>Health</h3>
        <pre>{
  "status": "ok",
  "service": "Student Course API"
}</pre>
        <h3>Course</h3>
        <pre>{
  "id": 1,
  "code": "CS101",
  "name": "Introduction to Programming",
  "description": "Learn programming fundamentals, problem-solving, and basic Python."
}</pre>
        <h3>Not found</h3>
        <pre>{
  "error": "Course with ID 9999 was not found."
}</pre>
      </section>
    </main></body></html>
    """


@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "service": "Student Course API"}), 200


@app.get("/api/courses")
def get_courses():
    return jsonify({"courses": COURSES, "count": len(COURSES)}), 200


@app.get("/api/courses/<int:course_id>")
def get_course(course_id):
    course = next((item for item in COURSES if item["id"] == course_id), None)
    if course is None:
        return jsonify({"error": f"Course with ID {course_id} was not found."}), 404
    return jsonify(course), 200


@app.errorhandler(404)
def not_found(_error):
    return jsonify({"error": "The requested endpoint was not found."}), 404


@app.errorhandler(405)
def method_not_allowed(_error):
    return jsonify({"error": "Method not allowed. Use GET for this API."}), 405


@app.errorhandler(500)
def internal_server_error(_error):
    return jsonify({"error": "An unexpected server error occurred."}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
