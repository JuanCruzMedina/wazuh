"""
File where task endpoints are tested
"""

import enum
import unittest
from typing import Any

from starlette import status
from starlette.testclient import TestClient

from src.server.app import app
from src.server.models.repositories import GetAllResult
from src.server.models.tasks import Task

client = TestClient(app)

TASKS_COUNT = 200


def get_tasks(data: list[dict[str, Any]]):
    """
    Get the tasks of a dictionary
    :param data: Dictionary containing tasks
    :return: tasks in the dictionary
    """
    return [Task(**task) for task in data]


def verify_tasks(data: list[dict[str, Any]]):
    """
    Check tasks properties
    :param data: Dictionary containing tasks
    :return: True if the tasks properties are correct
    """
    tasks = get_tasks(data)
    for task in tasks:
        # primitive attributes
        assert task.id != ""
        assert task.user_id != ""
        assert task.title != ""
    return True


class TestTasksRouter(unittest.TestCase):
    """
    Class where task router tests are performed
    """

    class Endpoints(str, enum.Enum):
        """
        Task router endpoints
        """
        tasks = '/tasks/'
        task_by_id = '/tasks/{}'

    def test_tasks(self):
        """
        Test the method that allows to get all tasks, without passing parameters
        """

        response = client.get(self.Endpoints.tasks)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        result = GetAllResult(**response.json())
        self.assertEqual(TASKS_COUNT, result.total_items)
        self.assertEqual(result.total_items, len(result.data))
        self.assertTrue(verify_tasks(result.data))

    def test_tasks_by_title_ok(self):
        """
        Test the method that allows to get all tasks, by title
        """
        words = ['delectus', 'aut', 'autem', 'veritatis', 'pariatur']

        for word in words:
            response = client.get(self.Endpoints.tasks, params={"title": word})
            self.assertEqual(status.HTTP_200_OK, response.status_code)
            result = GetAllResult(**response.json())
            self.assertEqual(result.total_items, len(result.data))
            self.assertTrue(verify_tasks(result.data))

    def test_tasks_by_title_empty(self):
        """
        Test the method that allows to get all tasks, by title
        """
        words = ['messi', 'maradona']

        for word in words:
            response = client.get(self.Endpoints.tasks, params={"title": word})
            self.assertEqual(status.HTTP_200_OK, response.status_code)
            result = GetAllResult(**response.json())
            self.assertEqual(result.total_items, len(result.data))
            self.assertEqual(0, result.total_items)

    def test_tasks_by_status(self):
        """
        Test the method that allows to get all tasks, by status
        """
        response_completed_tasks = client.get(self.Endpoints.tasks, params={"completed": True})
        self.assertEqual(status.HTTP_200_OK, response_completed_tasks.status_code)
        result_completed_tasks = GetAllResult(**response_completed_tasks.json())
        self.assertEqual(result_completed_tasks.total_items, len(result_completed_tasks.data))
        self.assertTrue(verify_tasks(result_completed_tasks.data))

        response_not_completed_tasks = client.get(self.Endpoints.tasks, params={"completed": False})
        self.assertEqual(status.HTTP_200_OK, response_not_completed_tasks.status_code)
        result_not_completed_tasks = GetAllResult(**response_not_completed_tasks.json())
        self.assertEqual(result_not_completed_tasks.total_items, len(result_not_completed_tasks.data))
        self.assertTrue(verify_tasks(result_not_completed_tasks.data))

        tasks_count_by_status = result_completed_tasks.total_items + result_not_completed_tasks.total_items

        response_all_tasks = client.get(self.Endpoints.tasks)
        self.assertEqual(status.HTTP_200_OK, response_all_tasks.status_code)
        result_all_tasks = GetAllResult(**response_all_tasks.json())
        self.assertEqual(result_all_tasks.total_items, len(result_all_tasks.data))
        self.assertTrue(verify_tasks(result_all_tasks.data))

        self.assertEqual(TASKS_COUNT, result_all_tasks.total_items, tasks_count_by_status)

    def test_task_by_id_ok(self):
        """
        Test the method that allows you to get all the tasks by their identifier,
        when the identifier passed as a parameter corresponds to an existing task
        """

        for task_id in range(1, TASKS_COUNT + 1):
            response = client.get(self.Endpoints.task_by_id.format(task_id))
            self.assertEqual(status.HTTP_200_OK, response.status_code)
            task = response.json()
            self.assertTrue(verify_tasks([task]))

    def test_task_by_id_fail(self):
        """
        Try the method that allows you to get all the tasks by their identifier,
        when the identifier passed as a parameter does not correspond to an existing task
        """

        response = client.get(self.Endpoints.task_by_id.format(TASKS_COUNT + 1))
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)


if __name__ == '__main__':
    unittest.main()
