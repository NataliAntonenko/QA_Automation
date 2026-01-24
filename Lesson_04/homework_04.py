adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

new_change_01 = adwentures_of_tom_sawer.replace("\n", " ")
print(new_change_01)

# task 02 ==
""" Замініть .... на пробіл
"""
new_change_2 = new_change_01.replace("....", " ")
print(new_change_2)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
parts = " ".join(new_change_2.split())
print(parts)


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count = 0
for symbol in adwentures_of_tom_sawer:
    if symbol == "h":
        count += 1

print(count)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
capital = 0

for word in adwentures_of_tom_sawer.split():
    if word[0].istitle():
        capital += 1

print(capital)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
tom = adwentures_of_tom_sawer.find("Tom")
if tom != -1:
    tom_second = adwentures_of_tom_sawer.find("Tom", tom + 1)
    print(f"Вдруге зустрічається на позиції {tom_second}.")
else:
    print("Підстрічка не знайдена.")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
import re
adwentures_of_tom_sawer_sentences = re.split(r"(?<!\.)[.](?!\.)\s", parts)
print(adwentures_of_tom_sawer_sentences)


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

lowcase = adwentures_of_tom_sawer_sentences[3].lower()
print(lowcase)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
start = "By the time"
counter = 1

for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith(start):
        print(f"Речення {counter} починається з 'By the time'")
    counter += 1

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

last_sentence = adwentures_of_tom_sawer_sentences[-1].split()
print(last_sentence)

word_quantity = 0
for words in last_sentence:
    word_quantity += 1

print(word_quantity)
