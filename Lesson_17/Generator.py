# 1. Напишіть генератор, який повертає послідовність парних чисел від 0 до N

def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

# 2. Створіть генератор, який генерує послідовність Фібоначчі до певного числа N
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

# 3. Реалізуйте ітератор для зворотного виведення елементів списку.
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

#4. Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration

        result = self.current
        self.current += 2
        return result

#5. Напишіть декоратор, який логує аргументи та результати викликаної функції.
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции: {func.__name__}")
        print(f"Аргументы: args={args}, kwargs={kwargs}")

        result = func(*args, **kwargs)

        print(f"Результат: {result}")
        return result

    return wrapper

#6. Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Виникла помилка при виконанні {func.__name__}: {e}")
            # Можно вернуть значение по умолчанию или None
            return None
    return wrapper