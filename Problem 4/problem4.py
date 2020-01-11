def is_palindrome(num):
    num_str = str(num)
    while len(num_str) > 0:
        if num_str[0] == num_str[-1]:
            num_str = num_str[1:-1]
        else:
            return False
    return True


largest = 0
for a in range(100, 1000):
    for b in range(100, 999):
        c = a * b
        if c > largest:
            if is_palindrome(c):
                largest = c

print(largest)
