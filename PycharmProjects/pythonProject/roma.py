class Student:
    def __init__(self, name, grade):  # исправлено __init__
        self.name = name
        self.__grade = grade  # приватный атрибут

    def get_grade(self):
        return self.__grade

    def set_grade(self, value):
        if 0 <= value <= 100:
            self.__grade = value
        else:
            print("Ошибка: оценка должна быть от 0 до 100")

student = Student("Romka", 85)
print(student.get_grade())

student.set_grade(92)
print(student.get_grade())

student.set_grade(10)
