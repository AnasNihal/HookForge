from fastapi import APIRouter, HTTPException, status

from ..models import Project, ProjectCreate
from ..store import MemoryStore, now


def router_for(store: MemoryStore) -> APIRouter:
    router = APIRouter(prefix="/api/projects", tags=["projects"])

    @router.get("", response_model=list[Project])
    def list_projects() -> list[Project]:
        return sorted(store.projects.values(), key=lambda project: project.updated_at, reverse=True)

    @router.get("/{project_id}", response_model=Project)
    def get_project(project_id: str) -> Project:
        project = store.projects.get(project_id)
        if project is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
        return project

    @router.post("", response_model=Project, status_code=status.HTTP_201_CREATED)
    def create_project(payload: ProjectCreate) -> Project:
        project_id = store.next_id("proj")
        project = Project(id=project_id, name=payload.name, environment=payload.environment, updated_at=now())
        store.projects[project_id] = project
        return project

    return router
