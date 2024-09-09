"""n的阶乘
"""




def calc(n):
    if n == 1 or n == 0:
        return 1
    return n*calc(n-1)

print(calc(5))

def fibnacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        fib = fibnacci(n - 1)
        fib.append(fib[-1] + fib[-2])
        return fib
    
    
print(fibnacci(100))