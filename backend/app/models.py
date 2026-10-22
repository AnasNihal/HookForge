from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class EventStatus(str, Enum):
    delivered = "Delivered"
    failed = "Failed"
    retrying = "Retrying"
    pending = "Pending"


class EndpointStatus(str, Enum):
    active = "Active"
    paused = "Paused"


class ProjectEnvironment(str, Enum):
    production = "Production"
    staging = "Staging"


class Project(BaseModel):
    id: str
    name: str
    environment: ProjectEnvironment
    endpoint_count: int = 0
    event_count: int = 0
    delivery_rate: str = "—"
    avg_latency: str = "—"
    updated_at: datetime


class ProjectCreate(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    environment: ProjectEnvironment = ProjectEnvironment.staging


class Endpoint(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    project_id: str
    name: str
    url: HttpUrl
    path: str
    method: str = "POST"
    status: EndpointStatus = EndpointStatus.active
    category: str = "Internal"
    events: int = 0
    latency_ms: int | None = None
    success_rate: float | None = None
    created_at: datetime
    updated_at: datetime


class EndpointCreate(BaseModel):
    project_id: str = "proj_payments"
    name: str = Field(min_length=2, max_length=80)
    url: HttpUrl
    method: str = Field(default="POST", pattern="^(GET|POST|PATCH)$")
    category: str = Field(default="Internal", min_length=2, max_length=40)


class EndpointUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=80)
    url: HttpUrl | None = None
    status: EndpointStatus | None = None
    category: str | None = Field(default=None, min_length=2, max_length=40)


class HookEvent(BaseModel):
    id: str
    project_id: str
    type: str
    endpoint_id: str
    endpoint_name: str
    status: EventStatus
    method: str
    response_status: int | None = None
    response_label: str
    received_at: datetime
    payload: dict[str, Any]
    headers: dict[str, str] = Field(default_factory=dict)


class EventPage(BaseModel):
    items: list[HookEvent]
    page: int
    page_size: int
    total: int
    total_pages: int


class DeliveryAttempt(BaseModel):
    id: str
    event_id: str
    attempt_number: int
    status_code: int | None = None
    status: EventStatus
    latency_ms: int | None = None
    detail: str
    attempted_at: datetime


class ReplayRequest(BaseModel):
    reason: str | None = Field(default=None, max_length=240)


class ReplayResponse(BaseModel):
    event_id: str
    attempt: DeliveryAttempt
    message: str


class InvestigationRequest(BaseModel):
    question: str = Field(min_length=3, max_length=500)
    event_id: str | None = None


class InvestigationResponse(BaseModel):
    answer: str
    recommended_action: str
    related_event_ids: list[str]


class LoginRequest(BaseModel):
    email: str = Field(min_length=3, max_length=160)
    password: str = Field(min_length=8, max_length=128)


class RegisterRequest(LoginRequest):
    name: str = Field(min_length=2, max_length=80)
    workspace_name: str = Field(min_length=2, max_length=80)


class AuthResponse(BaseModel):
    token: str
    user: dict[str, str]
    workspace_id: str


class WorkspaceSettings(BaseModel):
    id: str
    name: str
    slug: str
    description: str
    plan: str
    member_count: int
    notifications: dict[str, bool | str]


class WorkspaceSettingsUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=80)
    description: str | None = Field(default=None, max_length=240)
    email_notifications: bool | None = None
    failure_notifications: bool | None = None
    digest_frequency: str | None = Field(default=None, pattern="^(Daily summary|Weekly summary|Never)$")
