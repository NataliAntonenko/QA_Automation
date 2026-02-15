"""Завдання 1

Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, Manager та Developer, які успадковуються від Employee. Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.

Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer. Цей клас представляє керівника з команди розробників. Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ), а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.

Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead"""

class Employee:
    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary
        super().__init__(**kwargs)

class Manager(Employee):
    def __init__(self, department, **kwargs):
        self.department = department
        super().__init__(**kwargs)

class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        self.programming_language = programming_language
        super().__init__(**kwargs)

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        self.team_size = team_size
        super().__init__(
            name=name,
            salary=salary,
            department=department,
            programming_language=programming_language
        )

tl = TeamLead("Mike", 3000, "IT", "Python", 12)
print("Has attribute 'name'?", hasattr(tl, "name"))
print("Has attribute 'salary'?", hasattr(tl, "salary"))
print("Has attribute 'department'?", hasattr(tl, "department"))
print("Has attribute 'programming_language'?", hasattr(tl, "programming_language"))
print("Has attribute 'team_size'?", hasattr(tl, "team_size"))