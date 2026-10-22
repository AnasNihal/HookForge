from fastapi import APIRouter, HTTPException, status

from ..models import DeliveryAttempt, EventStatus, HookEvent, ReplayRequest, ReplayResponse
from ..store import MemoryStore, now


def router_for(store: MemoryStore) -> APIRouter:
    router = APIRouter(prefix="/api/events", tags=["delivery"])

    def require_event(event_id: str) -> HookEvent:
        event = store.events.get(event_id)
        if event is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
        return event

    @router.get("/{event_id}/attempts", response_model=list[DeliveryAttempt])
    def list_attempts(event_id: str) -> list[DeliveryAttempt]:
        require_event(event_id)
        return sorted(store.attempts.get(event_id, []), key=lambda attempt: attempt.attempt_number, reverse=True)

    @router.post("/{event_id}/replay", response_model=ReplayResponse, status_code=status.HTTP_201_CREATED)
    def replay_event(event_id: str, payload: ReplayRequest) -> ReplayResponse:
        event = require_event(event_id)
        existing = store.attempts.get(event_id, [])
        attempt_number = len(existing) + 1
        detail = payload.reason or "Replay delivered successfully"
        attempt = DeliveryAttempt(id=store.next_id("att"), event_id=event_id, attempt_number=attempt_number, status_code=200, status=EventStatus.delivered, latency_ms=184, detail=detail, attempted_at=now())
        store.attempts[event_id].append(attempt)
        store.events[event_id] = event.model_copy(update={"status": EventStatus.delivered, "response_status": 200, "response_label": "200 OK"})
        return ReplayResponse(event_id=event_id, attempt=attempt, message="Replay queued and delivered in the mock workspace")

    return router
