import json
import os
from Infra.test_actions.locators_methods import getLocator
from reqres.tests.scenarios import Scenarios
from Infra.test_base import BaseTest


def load_expected_response(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Expected response file '{file_path}' not found.")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_response_to_file(data, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"API response saved to {file_path}")


class TestAPI(BaseTest):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)

    def setUp(self):
        super().setUp()
        self.page = self.get_page()
        Scenarios.openPage(self, self.page)

    def test_response_list_users(self):
        response_file_path = r"C:\Users\gnimb\Dev\playwright\playwright\reqres\expected_response.json"
        end_point = "**/api/users?page=2"

        getLocator(self.page, "text", "LIST USERS").scroll_into_view_if_needed()
        self.compare_response_after_click(end_point, "text", "LIST USERS", response_file_path)


    def compare_response_after_click(self, end_point, clickMethod, clickLocator, file_path):
        with self.page.expect_response(end_point) as response_info:
            getLocator(self.page, clickMethod, clickLocator).click()

        response = response_info.value
        json_response = response.json()

        if not os.path.exists(file_path):
            save_response_to_file(json_response, file_path)

        expected_response = load_expected_response(file_path)
        self.assertEqual(json_response, expected_response, f"API response does not match expected JSON.\nReceived: {json.dumps(json_response, indent=2)}")
        print("API response matches expected JSON.")