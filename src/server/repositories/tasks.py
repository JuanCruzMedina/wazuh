from collections.abc import Generator
from typing import Optional
from src.server.application.utils import filter_if
from src.server.models.tasks import Task
from src.server.persistence.database import StaticData as Db, load_tasks


def apply_tasks_filters(
    tasks: list[Task], title: Optional[str], completed: Optional[bool]
) -> list[Task]:
    """
    Apply the filters in the task search
    :param tasks: Tasks to filter
    :param title: Title that a task should contain
    :param completed: Status of the tasks to get
    :return: Filtered tasks
    """
    # Filter tasks based on their attribute “completed”. When not specified, returns all tasks.
    tasks = filter_if(completed is not None, lambda d: d.completed == completed, tasks)
    # Filter tasks that do not contain the provided string in their title. Defaults to an empty string.
    tasks = filter_if(title is not None, lambda d: title in d.title, tasks)
    return list(tasks)


@load_tasks
def get_all_tasks(title: Optional[str], completed: Optional[bool]) -> list[Task]:
    """
    Retrieve all tasks
    :param title: Title that a task should contain
    :param completed: Status of the tasks to get
    :return: Tasks filtered based on the parameters
    """
    tasks: list[Task] = list(Db.Tasks)
    tasks = apply_tasks_filters(tasks, title, completed)
    return list(tasks)


@load_tasks
def get_task_by_id(task_id: int) -> Optional[Task]:
    """
    Get a task based on an identifier
    :param task_id:  Task identifier
    :return: Returns the task if found, None otherwise
    """
    for task in Db.Tasks:
        if task.id == task_id:
            return task


@load_tasks
def get_tasks_by_user_id(
    user_id: int, title: Optional[str], completed: Optional[bool]
) -> Generator:
    """
    Get all the tasks of a user based on their identifier
    :param user_id: user id
    :param title: Title that a tasks should contain
    :param completed: Status of the tasks to get
    :return: User tasks generator
    """
    for task in get_all_tasks(title, completed):
        if task.user_id == user_id:
            yield task
