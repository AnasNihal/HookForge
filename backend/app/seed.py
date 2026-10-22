from datetime import timedelta

from .models import DeliveryAttempt, Endpoint, EndpointStatus, EventStatus, HookEvent
from .store import MemoryStore, now


def seed_store(store: MemoryStore) -> None:
    if store.endpoints:
        return

    current = now()
    endpoints = [
        Endpoint(id="ep_stripe", project_id="proj_payments", name="Stripe Payments", url="https://api.acme.dev/hooks/stripe", path="/hooks/stripe", category="Payments", events=12482, latency_ms=184, success_rate=99.8, created_at=current - timedelta(days=16), updated_at=current - timedelta(hours=2)),
        Endpoint(id="ep_billing", project_id="proj_payments", name="Billing Service", url="https://billing.acme.dev/hooks", path="/hooks/billing", category="Payments", events=1821, latency_ms=257, success_rate=97.8, created_at=current - timedelta(days=14), updated_at=current - timedelta(hours=4)),
        Endpoint(id="ep_shopify", project_id="proj_commerce", name="Shopify Orders", url="https://commerce.acme.dev/hooks/shopify/orders", path="/hooks/shopify/orders", category="Commerce", events=6302, latency_ms=212, success_rate=98.9, created_at=current - timedelta(days=11), updated_at=current - timedelta(hours=5)),
        Endpoint(id="ep_identity", project_id="proj_commerce", name="Identity Sync", url="https://identity.acme.dev/hooks", path="/hooks/identity", method="PATCH", category="Users", events=3104, latency_ms=96, success_rate=99.9, created_at=current - timedelta(days=9), updated_at=current - timedelta(hours=3)),
        Endpoint(id="ep_slack", project_id="proj_internal", name="Slack Notifications", url="https://internal.acme.dev/hooks/slack", path="/hooks/slack", status=EndpointStatus.paused, category="Internal", events=2411, latency_ms=408, success_rate=94.3, created_at=current - timedelta(days=7), updated_at=current - timedelta(hours=1)),
        Endpoint(id="ep_github", project_id="proj_internal", name="GitHub Deploys", url="https://internal.acme.dev/hooks/github/deploys", path="/hooks/github/deploys", category="Engineering", events=592, latency_ms=142, success_rate=100, created_at=current - timedelta(days=5), updated_at=current - timedelta(hours=6)),
    ]
    for endpoint in endpoints:
        store.endpoints[endpoint.id] = endpoint

    events = [
        ("evt_01J8K3P4A9F2", "payment.succeeded", "ep_stripe", EventStatus.delivered, 200, "200 OK", 2, {"amount": 2499, "currency": "usd", "customer": "cus_8f12d"}),
        ("evt_01J8K2T7B6E1", "order.created", "ep_shopify", EventStatus.delivered, 200, "200 OK", 8, {"order_id": "#10492", "total": 129.0}),
        ("evt_01J8K1M9C8D0", "invoice.payment_failed", "ep_billing", EventStatus.failed, 503, "503 Error", 14, {"attempt": 3, "reason": "upstream_timeout"}),
        ("evt_01J8K0H2D7C8", "user.updated", "ep_identity", EventStatus.retrying, 502, "502 Error", 22, {"user_id": "usr_1029"}),
        ("evt_01J8J9R4E6B2", "subscription.created", "ep_stripe", EventStatus.delivered, 201, "201 Created", 31, {"plan": "pro_monthly"}),
        ("evt_01J8J8N6F3A1", "checkout.completed", "ep_stripe", EventStatus.pending, None, "—", 42, {"session": "cs_93bd"}),
        ("evt_01J8J7L8G5Z4", "deploy.finished", "ep_github", EventStatus.delivered, 200, "200 OK", 60, {"branch": "main"}),
        ("evt_01J8J6Q2H4X7", "message.sent", "ep_slack", EventStatus.failed, 429, "429 Error", 60, {"channel": "#alerts"}),
    ]
    for event_id, event_type, endpoint_id, status, response_status, response_label, minutes_ago, payload in events:
        endpoint = store.endpoints[endpoint_id]
        received_at = current - timedelta(minutes=minutes_ago)
        event = HookEvent(id=event_id, project_id=endpoint.project_id, type=event_type, endpoint_id=endpoint_id, endpoint_name=endpoint.name, status=status, method="POST", response_status=response_status, response_label=response_label, received_at=received_at, payload={"id": event_id, "type": event_type, "data": payload}, headers={"content-type": "application/json", "x-hookforge-signature": "sha256=demo"})
        attempts = [DeliveryAttempt(id=f"att_{event_id[-6:]}_1", event_id=event_id, attempt_number=1, status_code=response_status, status=status if status != EventStatus.retrying else EventStatus.failed, latency_ms=184 if response_status else None, detail="Delivered successfully" if status == EventStatus.delivered else "Upstream request timed out", attempted_at=received_at + timedelta(seconds=3))]
        store.add_event(event, attempts)


def overview_metrics(store: MemoryStore) -> dict[str, object]:
    events = list(store.events.values())
    delivered = sum(event.status == EventStatus.delivered for event in events)
    return {
        "events_received": 24892,
        "delivery_rate": round((delivered / len(events)) * 100, 1) if events else 0,
        "average_latency_ms": 184,
        "failed_events": sum(event.status == EventStatus.failed for event in events),
        "active_endpoints": sum(endpoint.status == EndpointStatus.active for endpoint in store.endpoints.values()),
        "updated_at": now(),
    }
