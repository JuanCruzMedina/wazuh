from fastapi import FastAPI

from src.server.routes.tasks import router as tasks_router
from src.server.routes.users import router as users_router

app = FastAPI(title="Test API")
app.include_router(tasks_router, tags=["Task"])
app.include_router(users_router, tags=["User"])
