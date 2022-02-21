from fastapi import APIRouter, HTTPException
from starlette import status
from src.server.models.repositories import GetAllResult
from src.server.models.users import User
from src.server.repositories.users import get_all_users, get_user_by_id, get_user_tasks

router = APIRouter()


def get_user(id: int):
    """
    Retrieves information from a single user
    :param id: User id
    :return: User
    """
    user: User = get_user_by_id(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The user with the id '{id}' does not exist.")
    return user


@router.get("/users/", status_code=status.HTTP_200_OK, response_model=GetAllResult, summary="Retrieves all users.")
def users() -> GetAllResult:
    """
    Retrieves all users listed on the users.json file.
    :return: All users
    """
    return GetAllResult(data=get_all_users())


@router.get("/users/{id}", status_code=status.HTTP_200_OK, response_model=User, summary="Retrieves all users.")
def user_by_id(id: int) -> User:
    """
    Retrieves information from a single user
    :param id: User id
    :return: User
    """
    user: User = get_user(id)
    return user


@router.get("/users/{id}/tasks", status_code=status.HTTP_200_OK, response_model=GetAllResult,
            summary="Retrieves all tasks from the specified user.")
def user_tasks(id: int, title: str = None, completed: bool = None) -> GetAllResult:
    """
    Retrieves all tasks from the specified user
    :param id: User id
    :param title: Displays tasks containing the provided string in their title. Defaults to an empty string
    :param completed: Filter tasks based on their attribute “completed”. When not specified, returns all tasks
    :return: All tasks
    """
    user: User = get_user(id)
    return GetAllResult(data=get_user_tasks(user.id, title, completed))
