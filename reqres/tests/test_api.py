import json
from Infra.test_actions.GetLocator import getLocator
from reqres.tests.Scenarios import Scenarios
from Infra.test_base import BaseTest

class TestAPI(BaseTest):

    def setUp(self):
        super().setUp()
        self.page = self.get_page()
        Scenarios.openPage(self, self.page)

    def test(self):
        getLocator(self.page, "text", "LIST USERS").scroll_into_view_if_needed()

        with self.page.expect_response("**/api/users?page=2") as response_info:
            getLocator(self.page, "text", "LIST USERS").click()

        response = response_info.value
        json_response = response.json()

        expected_response = {
            "page": 2,
            "per_page": 6,
            "total": 12,
            "total_pages": 2,
            "data": [
                {"id": 7, "email": "michael.lawson@reqres.in", "first_name": "Michael", "last_name": "Lawson", "avatar": "https://reqres.in/img/faces/7-image.jpg"},
                {"id": 8, "email": "lindsay.ferguson@reqres.in", "first_name": "Lindsay", "last_name": "Ferguson", "avatar": "https://reqres.in/img/faces/8-image.jpg"},
                {"id": 9, "email": "tobias.funke@reqres.in", "first_name": "Tobias", "last_name": "Funke", "avatar": "https://reqres.in/img/faces/9-image.jpg"},
                {"id": 10, "email": "byron.fields@reqres.in", "first_name": "Byron", "last_name": "Fields", "avatar": "https://reqres.in/img/faces/10-image.jpg"},
                {"id": 11, "email": "george.edwards@reqres.in", "first_name": "George", "last_name": "Edwards", "avatar": "https://reqres.in/img/faces/11-image.jpg"},
                {"id": 12, "email": "rachel.howell@reqres.in", "first_name": "Rachel", "last_name": "Howell", "avatar": "https://reqres.in/img/faces/12-image.jpg"}
            ],
            "support": {
                "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
                "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
            }
        }
        self.assertEqual(json_response, expected_response, f"API response does not match expected JSON.\nReceived: {json.dumps(json_response, indent=2)}")
        print("API response matches expected JSON.")

