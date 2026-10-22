from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.store import MemoryStore
from app.seed import overview_metrics, seed_store
from app.routes.projects import router_for as projects_router_for

app = FastAPI(title="HookForge API", version="0.1.0", description="Webhook observability API for the HookForge dashboard.")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
store = MemoryStore()
seed_store(store)
app.include_router(projects_router_for(store))

@app.get("/")
def home():
    return {"name": "HookForge API", "version": app.version, "docs": "/docs"}


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "hookforge-api"}


@app.get("/api/metrics/overview")
def metrics_overview() -> dict[str, object]:
    return overview_metrics(store)



