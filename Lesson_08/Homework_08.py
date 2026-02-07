"""Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент",
який дозволяє змінювати середній бал студента. '
 Виведіть інформацію про студента та змініть його середній бал.)"""

class Student:
    def __init__(self, name, surname, age, grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.grade = grade

    def update_grade(self, new_grade):
        self.grade = new_grade

    def info(self):
        print(f"Студент: {self.name} {self.surname}, вік: {self.age}, середній бал: {self.grade}")

my_student = Student("Den", "Savchuk", 30, 10)
my_student.info()

my_student.update_grade(new_grade=11)
my_student.info()