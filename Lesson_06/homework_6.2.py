my_string_1 = input()

letter = "h"
while letter not in my_string_1.lower():
    print("Symbol h is not found. Try again:")
    my_string_1 = input()
print("Symbol h is found:")
print(my_string_1)
