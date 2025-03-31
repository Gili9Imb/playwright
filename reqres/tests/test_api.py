import json
import os
from Infra.test_actions.GetLocator import getLocator
from reqres.tests.Scenarios import Scenarios
from Infra.test_base import BaseTest

class TestAPI(BaseTest):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)

    def setUp(self):
        super().setUp()
        self.page = self.get_page()
        Scenarios.openPage(self, self.page)

    def save_response_to_file(self, data, filePath):
        with open(filePath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"API response saved to {filePath}")

    def load_expected_response(self,filePath):
        if not os.path.exists(filePath):
            raise FileNotFoundError(f"Expected response file '{filePath}' not found.")
        with open(filePath, "r", encoding="utf-8") as f:
            return json.load(f)

    def listen_to_response_after_click(self,endpoint,clickMethod,clickLocator,filePath):
        with self.page.expect_response(endpoint) as response_info:
            getLocator(self.page, clickMethod, clickLocator).click()

        response = response_info.value
        json_response = response.json()

        if not os.path.exists(filePath):
            self.save_response_to_file(json_response,filePath)

        expected_response = self.load_expected_response(filePath)
        self.assertEqual(json_response, expected_response, f"API response does not match expected JSON.\nReceived: {json.dumps(json_response, indent=2)}")
        print("API response matches expected JSON.")

    def test_response_list_users(self):
        response_file = r"C:\Users\gnimb\Dev\playwright\playwright\reqres\expected_response.json"
        end_point = "**/api/users?page=2"

        getLocator(self.page, "text", "LIST USERS").scroll_into_view_if_needed()
        self.listen_to_response_after_click(end_point, "text","LIST USERS",response_file)


