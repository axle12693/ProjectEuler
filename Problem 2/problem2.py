memo_fib = {}
def fib(n):
    global memo_fib
    if n not in memo_fib.keys():
        if n == 0:
            memo_fib[n] = 1
        elif n == 1:
            memo_fib[n] = 2
        else:
            memo_fib[n] = fib(n - 1) + fib (n - 2)
    return memo_fib[n]

total = 0
i = 0
while True:
    term = fib(i)
    if term > 4000000:
        break
    if term % 2 == 0:
        total += term
    i += 1
print(total)
