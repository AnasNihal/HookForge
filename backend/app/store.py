from collections import defaultdict
from datetime import UTC, datetime, timedelta
from threading import Lock
from typing import Any
from uuid import uuid4

from .models import DeliveryAttempt, Endpoint, EventStatus, HookEvent, Project, ProjectEnvironment, WorkspaceSettings


def now() -> datetime:
    return datetime.now(UTC)


class MemoryStore:
    """Small in-memory repository used until the persistence layer is introduced."""

    def __init__(self) -> None:
        self.lock = Lock()
        current = now()
        self.workspace = WorkspaceSettings(
            id="ws_acme",
            name="Acme workspace",
            slug="acme",
            description="Reliable delivery monitoring for the Acme team.",
            plan="Pro",
            member_count=12,
            notifications={
                "email_notifications": True,
                "failure_notifications": True,
                "digest_frequency": "Daily summary",
            },
        )
        self.projects: dict[str, Project] = {
            "proj_payments": Project(id="proj_payments", name="Payments platform", environment=ProjectEnvironment.production, endpoint_count=2, event_count=18784, delivery_rate="99.6%", avg_latency="142ms", updated_at=current - timedelta(hours=2)),
            "proj_commerce": Project(id="proj_commerce", name="Commerce sync", environment=ProjectEnvironment.production, endpoint_count=2, event_count=6302, delivery_rate="98.9%", avg_latency="212ms", updated_at=current - timedelta(hours=5)),
            "proj_internal": Project(id="proj_internal", name="Internal automation", environment=ProjectEnvironment.staging, endpoint_count=2, event_count=2411, delivery_rate="94.3%", avg_latency="408ms", updated_at=current - timedelta(hours=1)),
        }
        self.endpoints: dict[str, Endpoint] = {}
        self.events: dict[str, HookEvent] = {}
        self.attempts: dict[str, list[DeliveryAttempt]] = defaultdict(list)

    def next_id(self, prefix: str) -> str:
        return f"{prefix}_{uuid4().hex[:12]}"

    def add_endpoint(self, endpoint: Endpoint) -> Endpoint:
        with self.lock:
            self.endpoints[endpoint.id] = endpoint
            project = self.projects.get(endpoint.project_id)
            if project:
                project.endpoint_count += 1
            return endpoint

    def add_event(self, event: HookEvent, attempts: list[DeliveryAttempt] | None = None) -> HookEvent:
        with self.lock:
            self.events[event.id] = event
            if attempts:
                self.attempts[event.id].extend(attempts)
            return event

    def update_workspace(self, **values: Any) -> WorkspaceSettings:
        with self.lock:
            self.workspace = self.workspace.model_copy(update=values)
            return self.workspace
