from fastapi import APIRouter, HTTPException, status

from ..models import EventStatus, InvestigationRequest, InvestigationResponse
from ..store import MemoryStore


def router_for(store: MemoryStore) -> APIRouter:
    router = APIRouter(prefix="/api/ai", tags=["investigation"])

    @router.post("/investigate", response_model=InvestigationResponse)
    def investigate(payload: InvestigationRequest) -> InvestigationResponse:
        event = store.events.get(payload.event_id) if payload.event_id else next((item for item in store.events.values() if item.status == EventStatus.failed), None)
        if payload.event_id and event is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
        if event is None:
            return InvestigationResponse(answer="No failed delivery is currently available in this workspace.", recommended_action="Wait for an event to arrive, then ask again.", related_event_ids=[])
        if event.status == EventStatus.failed:
            answer = f"{event.type} failed at {event.endpoint_name} with {event.response_label}. The delivery history points to an upstream timeout, so the endpoint should be checked before replaying."
            action = "Inspect the receiving service, then replay the event once it is healthy."
        elif event.status == EventStatus.retrying:
            answer = f"{event.type} is retrying against {event.endpoint_name}. The last response was {event.response_label}, which suggests a temporary upstream failure."
            action = "Monitor the next attempt and replay only if the retry window is exhausted."
        else:
            answer = f"{event.type} was delivered successfully to {event.endpoint_name}. Its most recent response was {event.response_label}."
            action = "No action is required; keep the endpoint under normal observation."
        related = [item.id for item in store.events.values() if item.status in {EventStatus.failed, EventStatus.retrying}][:4]
        return InvestigationResponse(answer=answer, recommended_action=action, related_event_ids=related)

    return router
