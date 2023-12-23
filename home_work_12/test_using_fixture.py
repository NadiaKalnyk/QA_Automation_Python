import pytest
import requests


@pytest.mark.usefixtures("fixture_query")
class TestQuery:
    def test_status_code(self):
        assert self.status_code == 200
    def test_search_by_the_word(self):
        print(self.response.json())
    def test_number_of_jokes(self):
        assert self.response.json()["total"] == 10
    def test_joke_exists(self):
        joke = "Chuck Norris can satisfy an oil well."
        assert self.response.json()["result"][1]["value"] == joke