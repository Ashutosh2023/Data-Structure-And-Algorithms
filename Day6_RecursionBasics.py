def printCount(n: int):
    print(n)
    if n == 4: #base condition
        return
    printCount(n+1)

# printCount(0)

def printBacktrack(a: int, b: int):
    if a<b:
        printBacktrack(a+1,b)
    print(a)

# printBacktrack(1,5)

# This is the parameterized way:
def printSumP(n: int, sum: int):
    if n==0:
        print(sum)
        return
    printSumP(n-1, sum+n)

# printSumP(6,0)


#This is the functional way, so that you can return something for all the calls:
def printSumF(n: int) -> int:
    if n==0:
        return 0
    return n + printSumF(n-1)

# print(printSumF(6))

def factorial(n: int) -> int:
    if n==1:
        return 1
    return n * factorial(n-1)
print(factorial(5))