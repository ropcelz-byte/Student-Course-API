# Student-Course-API

A simple REST API built with Python and Flask. It serves fictional course information as JSON, includes a small HTML homepage, enables CORS, and is configured for deployment on Render.

## Features

- Four requested GET endpoints
- Six fictional courses (no database or real student data)
- JSON responses and appropriate HTTP status codes
- JSON error responses for missing routes, unsupported methods, and server errors
- CORS enabled
- Automated tests with pytest
- Render deployment configuration using Gunicorn and the `PORT` environment variable
- Professional responsive dark-blue gradient homepage background (CSS; no external image required)

## Project structure

```text
Student-Course-API/
├── app.py
├── requirements.txt
├── README.md
├── Procfile
├── render.yaml
├── .gitignore
└── test_app.py
```

## Run locally

1. Install Python 3.10 or newer.
2. Open a terminal in this project directory.
3. Create and activate a virtual environment:

   **Windows (PowerShell):**
   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   **macOS/Linux:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
5. Start the API:
   ```bash
   python app.py
   ```
6. Open `http://127.0.0.1:5000/` for the homepage.

## API endpoints

| Method | Endpoint | Success / expected result |
|---|---|---|
| GET | `/api/health` | HTTP 200; service status |
| GET | `/api/courses` | HTTP 200; six courses |
| GET | `/api/courses/1` | HTTP 200; course ID 1 |
| GET | `/api/courses/9999` | HTTP 404; course-not-found JSON |

Example health response:

```json
{
  "status": "ok",
  "service": "Student Course API"
}
```

Example missing-course response:

```json
{
  "error": "Course with ID 9999 was not found."
}
```

The course-list response contains a `courses` array and a `count` field. Each course has `id`, `code`, `name`, and `description`.

## Run tests

Install dependencies first, then run:

```bash
python -m unittest -v
```

The test suite verifies all four required endpoints, JSON content types, course fields, and CORS headers.

## Deploy to Render

1. Create a GitHub repository named `Student-Course-API`.
2. Push the contents of this project folder to the repository root (do not nest another project folder inside it).
3. Sign in to [Render](https://render.com/) and choose **New + → Blueprint**.
4. Connect the GitHub repository and deploy the service described by `render.yaml`.
5. Render installs packages from `requirements.txt` and starts the app with `gunicorn app:app`. The app binds to `0.0.0.0` and reads the `PORT` environment variable.
6. After deployment, open the Render-provided URL. The homepage is at `/`; API routes are under `/api`.

You can also create a Render **Web Service** manually with:
- **Runtime:** Python
- **Build command:** `pip install -r requirements.txt`
- **Start command:** `gunicorn app:app`

## Notes

- Course data is stored in memory and resets whenever the service restarts or a new deployment is made.
- This project intentionally uses no database and contains no real student information.
