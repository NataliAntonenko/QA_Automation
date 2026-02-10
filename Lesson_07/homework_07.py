# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    multiplier = 1                                             #Initialize the appropriate variable
    while True:                                                  #Complete the while loop condition.
        result = number * multiplier                                #десь тут помила, а може не одна
        if  result > 25:
            break                                              #Enter the action to take if the result is greater than 25
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1                                       #Increment the appropriate variable

example = multiplication_table(3)
print (example)

#multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two(a,b):
    return a + b
print(sum_two(1,2))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def average(nums):
    return sum(nums) / len(nums)

nums = [1, 2, 3, 4]
print(average(nums))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(s):
    result = ""
    for char in s:
        result = char + result
    return result

my_input = input()
my_reverse = reverse_string(my_input)
print(my_reverse)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def find_longest_word(sentence):
    words = sentence.split()
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

find_input = input()
my_long_word = find_longest_word(find_input)
print(my_long_word)




# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
"Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті"

def sum_even_numbers(lst):
    counter = 0
    for i in lst:
        if i % 2 == 0:
            counter += i
    return counter

# task 8
"""Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
 Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1. 
 Данні в лісті можуть бути будь якими"""

def filter_strings(lst):
    lst2 = []
    for item in lst:
        if isinstance(item, str):
            lst2.append(item)
    return lst2

# task 9
""" Напишіть цикл, який буде вимагати від користувача ввести слово, 
в якому є літера "h" (враховуються як великі так і маленькі). 
Цикл не повинен завершитися, якщо користувач ввів слово без букви "h"."""


def input_string_with_h():
    user_input = input()
    while "h" not in user_input.lower():
        print("Symbol h is not found. Try again:")
        user_input = input()
    return user_input

# task 10
"""  Порахувати кількість унікальних символів в строці. 
Якщо їх більше 10 - вивести в консоль True, інакше - False. 
Строку отримати за допомогою функції input()
"""

def unique_symbols():
    my_string = input()
    unique = set(my_string)
    result = len(unique) > 10
    print(result)
    return result


