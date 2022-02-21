from typing import Optional

from src.server.application.utils import filter_if
from src.server.models.tasks import Task
from src.server.models.users import User
from src.server.repositories.tasks import get_tasks_by_user_id
from src.server.persistence.database import StaticData as Db, load_users


def apply_users_filters(users: list[User], street: Optional[str], city: Optional[str], company_name: Optional[str]) \
        -> list[User]:
    def word_format(w: Optional[str]):
        return w.lower() if w is not None else None

    street, city, company_name = word_format(street), word_format(city), word_format(company_name)

    users = filter_if(street is not None, lambda d: street in d.address.street.lower(), users)
    users = filter_if(city is not None, lambda d: city in d.address.city.lower(), users)
    users = filter_if(company_name is not None, lambda d: company_name in d.company.name.lower(), users)
    return list(users)


@load_users
def get_all_users(street: Optional[str], city: Optional[str], company_name: Optional[str]) -> list[User]:
    """
    Retrieve all users
    :return: users
    """
    users: list[User] = list(Db.Users)
    users = apply_users_filters(users, street, city, company_name)
    return list(users)


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
def get_user_tasks(
        user_id: int, title: Optional[str], completed: Optional[bool]
) -> list[Task]:
    """
    Retrieve user tasks
    :param user_id: user id
    :param title: Title that a task should contain
    :param completed: Status of the tasks to get
    :return: user tasks
    """
    return list(get_tasks_by_user_id(user_id, title, completed))
