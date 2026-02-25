def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_tail(n, actual=0, siguiente=1):
    if n == 0:
        return actual
    return fibonacci_tail(n - 1, siguiente, actual + siguiente)

import time 
inicio = time.time()
print(fibonacci(3))
print(time.time() - inicio)