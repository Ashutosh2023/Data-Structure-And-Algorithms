#single recursion call
def fibonacci(a, b, n) -> int:
    if n == 0:
        return b
    return fibonacci(b, a+b, n-1)

n = 7
# print(fibonacci(0,1,n-2))

#multiple call
def f(n):
    if(n<=1):
        return n
    return f(n-1) + f(n-2)

print(f(7))