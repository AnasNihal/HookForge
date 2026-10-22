from fastapi import APIRouter, status

from ..models import AuthResponse, LoginRequest, RegisterRequest
from ..store import MemoryStore


def router_for(store: MemoryStore) -> APIRouter:
    router = APIRouter(prefix="/api/auth", tags=["auth"])

    @router.post("/login", response_model=AuthResponse)
    def login(payload: LoginRequest) -> AuthResponse:
        return AuthResponse(token=f"demo_token_{payload.email.replace('@', '_')}", user={"name": "Amna Anas", "email": payload.email}, workspace_id=store.workspace.id)

    @router.post("/register", response_model=AuthResponse, status_code=status.HTTP_201_CREATED)
    def register(payload: RegisterRequest) -> AuthResponse:
        store.update_workspace(name=payload.workspace_name, slug=payload.workspace_name.lower().replace(" ", "-"))
        return AuthResponse(token=f"demo_token_{payload.email.replace('@', '_')}", user={"name": payload.name, "email": payload.email}, workspace_id=store.workspace.id)

    return router
