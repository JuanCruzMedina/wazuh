from typing import Optional

from src.server.models.tasks import Task
from src.server.models.users import User
from src.server.repositories.tasks import get_tasks_by_user_id
from src.server.persistence.database import StaticData as Db, load_users


@load_users
def get_all_users() -> list[User]:
    """
    Retrieve all users
    :return: users
    """
    return list(Db.Users)


@load_users
def get_user_by_id(user_id: int) -> Optional[User]:
    """
        Get a user based on an identifier
        :param user_id:  user identifier
        :return: Returns the user if found, None otherwise
        """
    for user in Db.Users:
        if user.id == user_id:
            return user


@load_users
def get_user_tasks(user_id: int, title: Optional[str], completed: Optional[bool]) -> list[Task]:
    """
    Retrieve user tasks
    :param user_id: user id
    :param title: Title that a task should contain
    :param completed: Status of the tasks to get
    :return: user tasks
    """
    return list(get_tasks_by_user_id(user_id, title, completed))
