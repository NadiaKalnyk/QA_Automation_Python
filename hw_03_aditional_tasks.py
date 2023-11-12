# Задача №1
# Сформуйте стрінг, в якому міститься інформація про певне слово.
# "Word [тут слово] has [тут довжина слова, отримайте з самого слова] letters",
# наприклад "Word 'Python' has 6 letters". Для отримання слова для аналізу скористайтеся константою або функцією input().
# string_a = "Loren ipsun dolor sit anet, consectetur adipisci elit, sed eiusnod tenpor incidunt ut labore et dolore nagna aliqua"
# word = "Loren"
# if word in string_a:
#     print(f"Word {word} has {len(word)} letters")
# else:
#     print(f"No word {word} in the string")

# Задача №2
# Напишіть калькулятор, який запитує два числа якщо це множення, додавання, ділення, віднімання. Або одне число якщо це
# зняття коріння або піднесення до степіня. Виводить на екран результат.
print("What operation: '*,+,-,/,sqr,^' do ou want to use?")
operation = input().lower()
if operation == 'sqr' or operation== '^':
    number_1 = input("Enter number = ")
    number_1 = float(number_1)
    if  operation == 'sqr':
        print(f"Root of the number {number_1} is {round(number_1 ** 0.5, 2)}")
    elif operation == '^':
        print(f"{number_1}^2 = {round(number_1 ** 2, 2)}")
elif operation == '*' or operation == '+' or operation == '/' or operation == '-':
    number_1 = float(input("Enter number1 = "))
    number_2 = float(input("Enter number2 = "))
    if operation == '*':
        print(f"{number_1} * {number_2} = {number_1 * number_2}")
    elif operation == '+':
        print(f"{number_1} + {number_2} = {number_1 + number_2}")
    elif operation == '/':
        print(f"{number_1} / {number_2} = {round(number_1 / number_2, 2)}")
    elif operation == '-':
        print(f"{number_1} - {number_2} = {number_1 - number_2}")
else:
    print("Wrong operation. Please select: '* , +, -, /, sqr, ^'")
