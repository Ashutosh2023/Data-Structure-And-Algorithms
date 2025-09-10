import math

# def checkPrime(n: int) -> bool:
#     if(n<=1):
#         return False
#     for i in range (2, int(n**0.5) + 1):
#         if n%i == 0:
#             return False
#     return True

# def getPrimeFactors(n: int):
#     if n <= 0:
#         raise ValueError("Divisors are defined only for positive integers")
#     small, large = [], []

#     for i in range(1, math.isqrt(n)+1):
#         if n % i == 0:
#             if(checkPrime(i)):
#                 small.append(i)
#             if n // i != i:
#                 if(checkPrime(n//i)):
#                     large.append(n // i)
#     print(small + large[::-1])

# getPrimeFactors(37)

def getPrimeFactorsopt(n: int):
    if n <= 0:
        raise ValueError("Divisors are defined only for positive integers")
    small = []
    for i in range(2, math.isqrt(n)+1):
        if i>=math.isqrt(n)+1:
            break
        if n % i == 0:
            small.append(i)
            while n%i==0:
                n = n//i
    if(n!=1):
        small.append(n)
    print(small)
getPrimeFactorsopt(780)