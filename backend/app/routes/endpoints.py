from fastapi import APIRouter, HTTPException, Query, status

from ..models import Endpoint, EndpointCreate, EndpointStatus, EndpointUpdate
from ..store import MemoryStore, now


def router_for(store: MemoryStore) -> APIRouter:
    router = APIRouter(prefix="/api/endpoints", tags=["endpoints"])

    @router.get("", response_model=list[Endpoint])
    def list_endpoints(project_id: str | None = None, endpoint_status: EndpointStatus | None = Query(default=None, alias="status"), search: str | None = None) -> list[Endpoint]:
        endpoints = list(store.endpoints.values())
        if project_id:
            endpoints = [endpoint for endpoint in endpoints if endpoint.project_id == project_id]
        if endpoint_status:
            endpoints = [endpoint for endpoint in endpoints if endpoint.status == endpoint_status]
        if search:
            needle = search.lower()
            endpoints = [endpoint for endpoint in endpoints if needle in f"{endpoint.name} {endpoint.path} {endpoint.category}".lower()]
        return sorted(endpoints, key=lambda endpoint: endpoint.updated_at, reverse=True)

    @router.get("/{endpoint_id}", response_model=Endpoint)
    def get_endpoint(endpoint_id: str) -> Endpoint:
        endpoint = store.endpoints.get(endpoint_id)
        if endpoint is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Endpoint not found")
        return endpoint

    @router.post("", response_model=Endpoint, status_code=status.HTTP_201_CREATED)
    def create_endpoint(payload: EndpointCreate) -> Endpoint:
        if payload.project_id not in store.projects:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
        current = now()
        endpoint = Endpoint(id=store.next_id("ep"), project_id=payload.project_id, name=payload.name, url=payload.url, path=payload.url.path or "/", method=payload.method, category=payload.category, created_at=current, updated_at=current)
        return store.add_endpoint(endpoint)

    @router.patch("/{endpoint_id}", response_model=Endpoint)
    def update_endpoint(endpoint_id: str, payload: EndpointUpdate) -> Endpoint:
        endpoint = store.endpoints.get(endpoint_id)
        if endpoint is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Endpoint not found")
        changes = payload.model_dump(exclude_unset=True)
        if "url" in changes and changes["url"] is not None:
            changes["path"] = changes["url"].path or "/"
        changes["updated_at"] = now()
        updated = endpoint.model_copy(update=changes)
        store.endpoints[endpoint_id] = updated
        return updated

    return router
