# Виберіть який з наступних магічних методів і реалізуйте його в простому класі:
# __ne__: To check if two objects are not equal.
# __lt__: To check if one object is less than another.
# __le__: To check if one object is less than or equal to another.
# __gt__: To check if one object is greater than another.
# __ge__: To check if one object is greater than or equal to another.
# І написати свою логіку яку ви хочте.
# Створіть два обьєта класа в якому ви це реалізували і зробіть перевірку що все працює

class Student:
    def __init__(self, name):
        self.name = name

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.name != other.name
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Student):
            return len(self.name) < len(other.name)
        else:
            return False

    def __le__(self, other):
        if isinstance(other, Student):
            return self == other or self < other
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Student):
            return len(self.name) > len(other.name)
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, Student):
            return self == other or self > other
        else:
            return False


student_1 = Student("Ivan")
student_2 = Student("Irina")
print("****************** Testing metod __ne__ *************************")
print(f"{student_1 != student_2} \n I'm not {student_2.name}. My name is {student_1.name} \n")

print("****************** Testing metod __lt__ *************************")
print(f"{student_1 < student_2} \n {len(student_1.name)} is less than {len(student_2.name)} \n")

print("****************** Testing metod __le__ *************************")
print(f"{student_1 == student_2 or student_1 < student_2} \n "
      f"{len(student_1.name)} is less than or equal than {len(student_2.name)} \n")

print("****************** Testing metod __gt__ *************************")
print(f"{student_2 > student_1} \n "
      f"{len(student_2.name)} is greater than {len(student_1.name)} \n")

print("****************** Testing metod __ge__ *************************")
print(f"{student_1 == student_2 or student_2 > student_1} \n "
      f"{len(student_2.name)} is greater than or equal {len(student_1.name)} \n")
