# 2) Напишіть клас калькулятора де будуть 4 арифметичні дії плюс, мінус, додавання, множення - звичайні методи.
# і зробіть статік метод який буде виводити повідомлення, привіт я калькулятор.
# 3) Напишіть тестовий клас який буде тестити попередній калькулятор тільки додавання і ділення.
#  до кожної математичної дії зробіть 5 тестів(використовуйте параметрайз, не пишіть руками зайвого).
# Зробіть класову фікстуру(класметод) для сетапа і тердауна сетпа буде писати повідомлення в файл коли ми запустили тест
# та текстове повідомлення що ми стартанули. Тердаун буде писати повідомлення що ми закінчили і також час коли закінчили
# використайте вже відому вам бібліотеку дататайм

class Calculator:
    def multiplication(self, first_number, second_number) -> int:
        return first_number * second_number

    def addition(self, first_number, second_number) -> int:
        return first_number + second_number

    def division(self, first_number, second_number) -> int:
        if second_number != 0:
            return first_number / second_number
        raise TypeError("Division by zero is forbidden")

    def subtraction(self, first_number, second_number) -> int:
        return first_number - second_number

    @staticmethod
    def info():
        return "________________ Hello! I'm Calculator ________________"
