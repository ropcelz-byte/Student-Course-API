import unittest
from app import app


class StudentCourseAPITestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_health_endpoint(self):
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "ok")
        self.assertEqual(response.get_json()["service"], "Student Course API")

    def test_courses_endpoint_returns_six_courses(self):
        response = self.client.get("/api/courses")
        self.assertEqual(response.status_code, 200)
        payload = response.get_json()
        self.assertEqual(payload["count"], 6)
        self.assertEqual(len(payload["courses"]), 6)
        for course in payload["courses"]:
            self.assertTrue({"id", "code", "name", "description"}.issubset(course))

    def test_course_one_endpoint(self):
        response = self.client.get("/api/courses/1")
        self.assertEqual(response.status_code, 200)
        course = response.get_json()
        self.assertEqual(course["id"], 1)
        self.assertEqual(course["code"], "CS101")

    def test_missing_course_returns_404_json(self):
        response = self.client.get("/api/courses/9999")
        self.assertEqual(response.status_code, 404)
        self.assertIn("not found", response.get_json()["error"].lower())

    def test_cors_header_is_present(self):
        response = self.client.get(
            "/api/health",
            headers={"Origin": "https://example.com"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers.get("Access-Control-Allow-Origin"), "*")

    def test_unknown_route_returns_json_404(self):
        response = self.client.get("/api/does-not-exist")
        self.assertEqual(response.status_code, 404)
        self.assertIn("error", response.get_json())


if __name__ == "__main__":
    unittest.main()
