import numpy as np


def is_prime(n):
    for i in range(2, int(np.ceil(np.sqrt(n)))+1):
        if n % i == 0 and i != n:
            return False
    return True


num = 600851475143
i = 2
factors = []
while i < num:
    while not is_prime(i):
        i += 1
    if num % i == 0:
        num = num / i
        if i not in factors:
            factors.append(i)
    i += 1
print(np.max(factors))
