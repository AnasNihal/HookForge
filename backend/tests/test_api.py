import sys
import unittest
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).parents[1]))
from main import app  # noqa: E402


class HookForgeApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = TestClient(app)

    def test_health_and_metrics(self) -> None:
        self.assertEqual(self.client.get("/api/health").status_code, 200)
        metrics = self.client.get("/api/metrics/overview")
        self.assertEqual(metrics.status_code, 200)
        self.assertIn("delivery_rate", metrics.json())

    def test_projects_can_be_listed_and_created(self) -> None:
        projects = self.client.get("/api/projects")
        self.assertGreaterEqual(len(projects.json()), 3)
        created = self.client.post("/api/projects", json={"name": "Test integrations", "environment": "Staging"})
        self.assertEqual(created.status_code, 201)
        self.assertEqual(created.json()["name"], "Test integrations")

    def test_endpoint_filters_and_creation(self) -> None:
        filtered = self.client.get("/api/endpoints", params={"category": "Payments"})
        self.assertEqual(filtered.status_code, 200)
        self.assertTrue(all(item["category"] == "Payments" for item in filtered.json()))
        created = self.client.post("/api/endpoints", json={"name": "Test receiver", "url": "https://example.com/hooks", "category": "Internal"})
        self.assertEqual(created.status_code, 201)
        endpoint_id = created.json()["id"]
        updated = self.client.patch(f"/api/endpoints/{endpoint_id}", json={"status": "Paused"})
        self.assertEqual(updated.json()["status"], "Paused")

    def test_events_pagination_detail_and_replay(self) -> None:
        page = self.client.get("/api/events", params={"page": 1, "page_size": 2})
        self.assertEqual(page.status_code, 200)
        self.assertEqual(len(page.json()["items"]), 2)
        event_id = page.json()["items"][0]["id"]
        detail = self.client.get(f"/api/events/{event_id}")
        self.assertEqual(detail.status_code, 200)
        attempts = self.client.get(f"/api/events/{event_id}/attempts")
        self.assertEqual(attempts.status_code, 200)
        replay = self.client.post(f"/api/events/{event_id}/replay", json={"reason": "API test replay"})
        self.assertEqual(replay.status_code, 201)
        self.assertEqual(replay.json()["attempt"]["status"], "Delivered")

    def test_ai_auth_and_settings(self) -> None:
        investigation = self.client.post("/api/ai/investigate", json={"question": "Why did the last delivery fail?"})
        self.assertEqual(investigation.status_code, 200)
        self.assertTrue(investigation.json()["answer"])
        login = self.client.post("/api/auth/login", json={"email": "test@example.com", "password": "password123"})
        self.assertEqual(login.status_code, 200)
        settings = self.client.patch("/api/workspace/settings", json={"digest_frequency": "Weekly summary", "failure_notifications": False})
        self.assertEqual(settings.status_code, 200)
        self.assertEqual(settings.json()["notifications"]["digest_frequency"], "Weekly summary")


if __name__ == "__main__":
    unittest.main()
