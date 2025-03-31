import json
import os
from Infra.test_actions.GetLocator import getLocator
from reqres.tests.Scenarios import Scenarios
from Infra.test_base import BaseTest

class TestAPI(BaseTest):
    RESPONSE_FILE = r"C:\Users\gnimb\Dev\playwright\playwright\reqres\expected_response.json"

    def setUp(self):
        super().setUp()
        self.page = self.get_page()
        Scenarios.openPage(self, self.page)

    def save_response_to_file(self, data):
        with open(self.RESPONSE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"API response saved to {self.RESPONSE_FILE}")

    def load_expected_response(self):
        if not os.path.exists(self.RESPONSE_FILE):
            raise FileNotFoundError(f"Expected response file '{self.RESPONSE_FILE}' not found.")
        with open(self.RESPONSE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    def test(self):
        getLocator(self.page, "text", "LIST USERS").scroll_into_view_if_needed()

        with self.page.expect_response("**/api/users?page=2") as response_info:
            getLocator(self.page, "text", "LIST USERS").click()

        response = response_info.value
        json_response = response.json()

        if not os.path.exists(self.RESPONSE_FILE):
            self.save_response_to_file(json_response)

        expected_response = self.load_expected_response()
        self.assertEqual(json_response, expected_response, f"API response does not match expected JSON.\nReceived: {json.dumps(json_response, indent=2)}")
        print("API response matches expected JSON.")
