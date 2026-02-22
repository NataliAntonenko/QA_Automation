
def sum_two(a,b):
    return a + b
print(sum_two(1,2))


def average(nums):
    return sum(nums) / len(nums)
nums = [1, 2, 3, 4]
print(average(nums))


def sum_even_numbers(lst):
    counter = 0
    for i in lst:
        if i % 2 == 0:
            counter += i
    return counter




