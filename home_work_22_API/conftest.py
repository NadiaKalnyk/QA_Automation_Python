import pytest
import requests


@pytest.fixture(scope="class")
def exchange_rate(request):
    response = requests.request(method="GET",
                                url="https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date=20200302&json")
    request.cls.response = response
    yield response
