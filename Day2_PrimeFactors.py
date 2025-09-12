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
            while n%i==0:  ## if it was divisible by 2 then divide the number until it is divisible by 2
                n = n//i   ## exhaust all 2 
    if(n!=1):
        small.append(n)
    print(small)
getPrimeFactorsopt(780)


# def getAllPrimeFactors(n: int, factors: set):
#         # factor 2 separately
#         while n % 2 == 0:
#             factors.add(2)
#             n //= 2

#         # odd factors
#         for i in range(3, math.isqrt(n) + 1, 2):
#             while n % i == 0:
#                 factors.add(i)
#                 n //= i

#         # if anything left, it is prime
#         if n > 1:
#             factors.add(n)