import pytest
import requests


@pytest.mark.usefixtures("fixture_random")
class TestRandom:
    def test_icon_url_is_not_empty(self):
       assert len(str(self.response.json()["icon_url"])) > 0

    def test_icon_url_is_image(self):
        assert (str(self.response.json()["icon_url"][-3:-1]+self.response.json()["icon_url"][-1])== 'png')

    def test_check_key_value(self):
        key = "value"
        assert self.response.json()[f"{key}"]

@pytest.mark.usefixtures("fixture_query")
class TestQuery:
    def test_status_code(self):
        assert self.status_code == 200
def test_search_by_the_word():
    URL = "https://api.chucknorris.io/jokes/search?query=oil"
    response = requests.request(method="GET", url=URL)
    print(response.json())
@pytest.mark.parametrize("query",
                            requests.request(method="GET", url="https://api.chucknorris.io/jokes/search?query=oil").json())
def test_number_of_jokes(query):
    query=" oil "
    URL = f"https://api.chucknorris.io/jokes/search?query={query}"
    response = requests.request(method="GET", url=URL)
    assert response.json()["total"] == 10

@pytest.mark.parametrize("query",
                            requests.request(method="GET", url="https://api.chucknorris.io/jokes/search?query=oil").json())
def test_joke_exists(query):
    query = " oil "
    URL = f"https://api.chucknorris.io/jokes/search?query={query}"
    response = requests.request(method="GET", url=URL)
    assert response.json()["result"]["value":"Chuck Norris once had an erection while laying face down.... he struck oil"]




