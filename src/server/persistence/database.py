import io
import json
import os

from src.server.models.tasks import Task
from src.server.models.users import User

os.chdir(os.path.dirname(os.path.abspath(__file__)))

USERS_PATH: str = "../data/users.json"
TASKS_PATH: str = "../data/tasks.json"


class StaticData:
    """
    Class that contains the static information of the jsons.
    It is used to simulate the database.
    """

    Users: list[User] = []
    Tasks: list[Task] = []


def load_users(function):
    """
    It allows to load the static information corresponding to the users, in case it is not previously loaded.
    It is used in the user repository
    """

    def wrapper(*args, **kwargs):
        if not StaticData.Users:
            print("Loading users...")
            with io.open(USERS_PATH, "r", encoding="utf-8") as jsonFile:
                StaticData.Users = [User(**user) for user in json.load(jsonFile)]
                print(f"Number of uploaded 'users' - {len(StaticData.Users)}")

        return function(*args, **kwargs)

    return wrapper


def load_tasks(function):
    """
    It allows to load the static information corresponding to the tasks, in case it is not previously loaded.
    It is used in the user repository
    """

    def wrapper(*args, **kwargs):
        if not StaticData.Tasks:
            print("Loading tasks...")
            with io.open(TASKS_PATH, "r", encoding="utf-8") as jsonFile:
                StaticData.Tasks = [Task(**task) for task in json.load(jsonFile)]
                print(f"Number of uploaded tasks - {len(StaticData.Tasks)}")

        return function(*args, **kwargs)

    return wrapper
