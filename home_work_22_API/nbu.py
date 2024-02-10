# Підключіться до API НБУ ( документація тут https://bank.gov.ua/ua/open-data/api-dev ),
# отримайте курс валют і запишіть його в текстовий файл такому форматі (список):

# "[дата створення запиту]"
# 1. [назва валюти 1] to UAH: [значення курсу до валюти 1]
# 2. [назва валюти 2] to UAH: [значення курсу до валюти 2]
# 3. [назва валюти 3] to UAH: [значення курсу до валюти 3]
# n. [назва валюти n] to UAH: [значення курсу до валюти n]
#
# P.S.не забувайте про DRY(Don't Repeat Yourself), KISS(Keep It Simple, Stupid), перевірки
import pytest


@pytest.mark.usefixtures("exchange_rate")
class NBU:

    def exchange_date(self):
        return self.response.json()[0]['exchangedate']

    def country(self):
        for key in range(0, len(self.response.json())):
            return f'{self.response.json()[key]["txt"]}'

    def rate(self):
        for key in range(0, len(self.response.json())):
            return f'{self.response.json()[key]["rate"]}'


nbu = NBU()
with open("NBU.txt", "a") as file:
    file.write(f'{nbu.exchange_date()}')
    # file.write(f'{nbu.country()} to UAH: {nbu.exhange_rate()}')

# def test_er(self):
#     print(type(self.response.json()[0]))
#     pass
# exchangedate
