my_string = input()
print(my_string)
unique = set(my_string)

if len(unique) > 10:
    print(True)
else:
    print(False)

