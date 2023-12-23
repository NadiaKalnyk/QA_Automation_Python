import pytest
import requests


@pytest.fixture(scope="class")
def fixture_random(request):
    response = requests.request(method="GET", url="https://api.chucknorris.io/jokes/random")
    request.cls.response = response
    yield response


@pytest.fixture(scope="class")
def fixture_query(request):
    query = " oil "
    URL = f"https://api.chucknorris.io/jokes/search?query={query}"
    response = requests.request(method="GET", url=URL)
    status_code = response.status_code
    request.cls.status_code = status_code
    request.cls.response = response
    yield response, status_code
