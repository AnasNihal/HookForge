from fastapi import APIRouter, HTTPException, status

from ..models import WorkspaceSettings, WorkspaceSettingsUpdate
from ..store import MemoryStore


def router_for(store: MemoryStore) -> APIRouter:
    router = APIRouter(prefix="/api/workspace", tags=["workspace"])

    @router.get("/settings", response_model=WorkspaceSettings)
    def get_settings() -> WorkspaceSettings:
        return store.workspace

    @router.patch("/settings", response_model=WorkspaceSettings)
    def update_settings(payload: WorkspaceSettingsUpdate) -> WorkspaceSettings:
        values = payload.model_dump(exclude_unset=True)
        notification_values = {key: values.pop(key) for key in list(values) if key in {"email_notifications", "failure_notifications", "digest_frequency"}}
        if values:
            workspace = store.update_workspace(**values)
        else:
            workspace = store.workspace
        if notification_values:
            notifications = {**workspace.notifications, **notification_values}
            workspace = store.update_workspace(notifications=notifications)
        return workspace

    @router.get("/settings/{setting_name}")
    def get_setting(setting_name: str) -> dict[str, object]:
        if setting_name not in store.workspace.notifications:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Setting not found")
        return {"name": setting_name, "value": store.workspace.notifications[setting_name]}

    return router
