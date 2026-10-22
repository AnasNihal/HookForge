from fastapi import APIRouter, HTTPException, Query, status

from ..models import EventPage, EventStatus, HookEvent
from ..store import MemoryStore


def router_for(store: MemoryStore) -> APIRouter:
    router = APIRouter(prefix="/api/events", tags=["events"])

    @router.get("", response_model=EventPage)
    def list_events(
        project_id: str | None = None,
        endpoint_id: str | None = None,
        event_status: EventStatus | None = Query(default=None, alias="status"),
        search: str | None = None,
        page: int = Query(default=1, ge=1),
        page_size: int = Query(default=25, ge=1, le=100),
    ) -> EventPage:
        events = list(store.events.values())
        if project_id:
            events = [event for event in events if event.project_id == project_id]
        if endpoint_id:
            events = [event for event in events if event.endpoint_id == endpoint_id]
        if event_status:
            events = [event for event in events if event.status == event_status]
        if search:
            needle = search.lower()
            events = [event for event in events if needle in f"{event.id} {event.type} {event.endpoint_name}".lower()]
        events.sort(key=lambda event: event.received_at, reverse=True)
        total = len(events)
        start = (page - 1) * page_size
        end = start + page_size
        total_pages = max(1, (total + page_size - 1) // page_size)
        return EventPage(items=events[start:end], page=page, page_size=page_size, total=total, total_pages=total_pages)

    @router.get("/{event_id}", response_model=HookEvent)
    def get_event(event_id: str) -> HookEvent:
        event = store.events.get(event_id)
        if event is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
        return event

    return router
