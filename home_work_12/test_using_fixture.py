import pytest


@pytest.mark.usefixtures("fixture_query")
class TestQuery:
    def search_by_the_word(self):
        print(self.response.json())

    def test_status_code(self):
        assert self.status_code == 200

    def test_number_of_jokes(self):
        assert self.response.json()["total"] == 10

    def test_joke_exists(self):
        joke_by_the_word = " oil "
        assert self.response.json()["result"][1]["value"].index(joke_by_the_word)
