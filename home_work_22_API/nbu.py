# Підключіться до API НБУ ( документація тут https://bank.gov.ua/ua/open-data/api-dev ),
# отримайте курс валют і запишіть його в текстовий файл такому форматі (список):
#
# "[дата створення запиту]"
# 1. [назва валюти 1] to UAH: [значення курсу до валюти 1]
# 2. [назва валюти 2] to UAH: [значення курсу до валюти 2]
# 3. [назва валюти 3] to UAH: [значення курсу до валюти 3]
# n. [назва валюти n] to UAH: [значення курсу до валюти n]
#
# P.S.не забувайте про DRY(Don't Repeat Yourself), KISS(Keep It Simple, Stupid), перевірки
import requests


class NBU:
    def __init__(self, response=requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")):
        self.response = response

    def exchange_date(self):
        return self.response.json()[0]['exchangedate']

    def country(self):
        country_names = [i['txt'] for i in self.response.json()]  # gptChat
        return country_names

    def rate(self):
        rate_values = [i['rate'] for i in self.response.json()]  # gptChat
        return rate_values

    def contry_to_UAH_rate(self):
        result_dict = dict(zip(self.country(), self.rate()))
        for key, value in result_dict.items():
            country_and_rate = f'{key} to UAH: {value}'
            return country_and_rate  # вивід у консоль правильний, якщо змінити print на return -> у файл записує лише перше значення + текст не виводить

    def writting_to_file(self):
        with open("NBU.txt", "w") as file:
            file.write(f'{self.exchange_date()} \n{self.contry_to_UAH_rate()}')
