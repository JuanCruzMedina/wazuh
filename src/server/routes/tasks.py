from fastapi import APIRouter, HTTPException
from starlette import status
from src.server.models.repositories import GetAllResult
from src.server.models.tasks import Task
from src.server.repositories.tasks import get_all_tasks, get_task_by_id

router = APIRouter()


@router.get(
    "/tasks/",
    status_code=status.HTTP_200_OK,
    response_model=GetAllResult,
    summary="Retrieves all tasks " "listed on the tasks.json " "file",
)
def tasks(title: str = None, completed: bool = None) -> GetAllResult:
    """
    Retrieves all tasks listed on the tasks.json file
    :param title: Displays tasks containing the provided string in their title. Defaults to an empty string
    :param completed: Filter tasks based on their attribute “completed”. When not specified, returns all tasks
    :return: All tasks
    """
    return GetAllResult(data=get_all_tasks(title, completed))


@router.get(
    "/tasks/{id}",
    status_code=status.HTTP_200_OK,
    response_model=Task,
    summary="Retrieves information from a " "single task.",
)
def task_by_id(id: int) -> Task:
    """
    Retrieves information from a single task.
    :param id: Task identifier
    :return: Task
    """
    task: Task = get_task_by_id(id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The task with the id '{id}' does not exist.",
        )
    return task
