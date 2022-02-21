from pydantic import BaseModel, Field


class Task(BaseModel):
    """
    Class that represents a task.
    """

    user_id: int = Field(..., ge=1, description="User ID should do the task.")
    id: int = Field(..., ge=1, description="Task identifier.")
    title: str = Field(..., description="Task title.")
    completed: bool = Field(
        default=False, description="Determines if the task was completed."
    )

    class Config:
        schema_extra = {
            "user_id": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False,
        }
