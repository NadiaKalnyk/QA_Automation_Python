import random
import string


def generate_password(length, use_numbers=True, use_lowercase=True, use_uppercase=True, use_cyrillic=True):
    characters = ''
    if use_numbers:
        characters += string.numbers
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_cyrillic:
        characters += 'qwertyuiopasdfghjklzxcvbnm'

    password = ''.join(random.choice(characters) for i in range(length))
    return password


def main():
    use_numbers = input("Використовувати цифри? (так/ні): ").lower() == 'так'
    use_lowercase = input("Використовувати малі літери? (так/ні): ").lower() == 'так'
    use_uppercase = input("Використовувати великі літери? (так/ні): ").lower() == 'так'
    use_cyrillic = input("Використовувати кирилицю? (так/ні): ").lower() == 'так'
    length = int(input("Введіть довжину пароля: "))

    password = generate_password(length, use_numbers, use_lowercase, use_uppercase, use_cyrillic)
    print("Згенерований пароль:", password)


main()
