def is_multiple_of(num1, num2):
    """Is num1 a multiple of num2?"""
    return num1 % num2 == 0


nums_list = []

for i in range(3, 1000):
    if is_multiple_of(i, 3):
        nums_list.append(i)
    if is_multiple_of(i, 5) and not is_multiple_of(i, 3):
        nums_list.append(i)

total = 0
for n in nums_list:
    total += n

print(total)
