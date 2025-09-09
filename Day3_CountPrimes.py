import math

def checkPrime(n: int) -> bool:
    for i in range (2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True

# def countPrimes(n: int) -> int:
#     count = 0
#     for p in range(2,n):
#         if checkPrime(p):
#             count += 1
#     return count

# print(countPrimes(10))

# Time Complexity O(nlogn)
# def sieveOfEratosthenes(n: int) -> int:
#     if n == 0 or n == 1:
#         return 0
#     primeList = [True] * (n)
#     primeList[0] = primeList[1] = False
#     for i in range(2, math.isqrt(n)+1):
#         if(primeList[i] == True):
#             j = 2
#             while j*i < n:
#                 primeList[i*j] = False
#                 j += 1
#     return primeList.count(True)

# print(sieveOfEratosthenes(30))

# Time Complexity O(nloglogn)
def countPrimes(n: int) -> int:
    if n <= 2:
        return 0
    primeList = [True] * n
    primeList[0] = primeList[1] = False
    for i in range(2, math.isqrt(n) + 1):
        if primeList[i]:
            j = i * i       # start from i*i
            while j < n:
                primeList[j] = False
                j += i
    return sum(primeList)

print(countPrimes(30))