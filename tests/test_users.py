"""
File where user endpoints are tested.
"""

import enum
import unittest
from typing import Any

from starlette import status
from starlette.testclient import TestClient

from src.server.app import app
from src.server.models.repositories import GetAllResult
from src.server.models.users import User
from tests.test_tasks import verify_tasks

client = TestClient(app)

# Number of users in the json file
USERS_COUNT = 10


def get_users(data: list[dict[str, Any]]) -> list[User]:
    """
    Get the users of a dictionary
    :param data: Dictionary containing users
    :return: users in the dictionary
    """
    return [User(**user) for user in data]


def verify_users(data: list[dict[str, Any]]):
    """
    Check user properties
    :param data: Dictionary containing users
    :return: True if the users properties are correct
    """
    users = get_users(data)
    for user in users:
        # primitive attributes
        assert user.id != ""
        assert user.username != ""
        assert user.email != ""
        assert user.name != ""
        assert user.website != ""
        assert user.email != ""
        # Company
        assert user.company.name != ""
        assert user.company.bs != ""
        assert user.company.catchPhrase != ""
        # Address
        assert user.address.city != ""
        assert user.address.suite != ""
        assert user.address.street != ""
        assert user.address.zipcode != ""
    return True


class TestUserRouter(unittest.TestCase):
    """
    Class where user router tests are performed
    """

    class Endpoints(str, enum.Enum):
        """
        User router endpoints
        """

        users = '/users/'
        user_by_id = '/users/{}'
        users_tasks = '/users/{}/tasks'

    def test_users(self) -> None:
        """
        Test the method that allows to obtain all the users
        """

        response = client.get(self.Endpoints.users)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        result = GetAllResult(**response.json())
        self.assertEqual(USERS_COUNT, result.total_items)
        self.assertEqual(result.total_items, len(result.data))
        self.assertTrue(verify_users(result.data))

    def test_user_by_id_ok(self) -> None:
        """
        Tests the method that allows obtaining a user based on its identifier,
        when the identifier passed as a parameter belongs to a user
        """

        for user_id in range(1, USERS_COUNT + 1):
            response = client.get(self.Endpoints.user_by_id.format(user_id))
            self.assertEqual(status.HTTP_200_OK, response.status_code)
            user = response.json()
            self.assertTrue(verify_users([user]))

    def test_user_by_id_fail(self) -> None:
        """
        Test the method that allows to obtain a user from its identifier,
        when the identifier passed as parameter does not belong to a user
        """

        response = client.get(self.Endpoints.user_by_id.format(USERS_COUNT + 1))
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_users_tasks_ok(self) -> None:
        """
        Test the method that allows to obtain a user's tasks from its identifier,
        when the identifier passed as parameter belongs to a user
        """

        for user_id in range(1, USERS_COUNT + 1):
            response = client.get(self.Endpoints.users_tasks.format(user_id))
            self.assertEqual(status.HTTP_200_OK, response.status_code)
            result = GetAllResult(**response.json())
            self.assertTrue(result.total_items >= 0)
            self.assertTrue(verify_tasks(result.data))

    def test_users_tasks_fail(self) -> None:
        """
        Test the method that allows to obtain a user's tasks from its identifier,
        when the identifier passed as a parameter does not belong to a user
        """

        response = client.get(self.Endpoints.users_tasks.format(USERS_COUNT+1))
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)


if __name__ == '__main__':
    unittest.main()
