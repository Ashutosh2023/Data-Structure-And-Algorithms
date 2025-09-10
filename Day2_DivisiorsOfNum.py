import math

# def getDivisors(n: int):
#     if n <= 0:
#         raise ValueError("Divisors are defined only for positive integers")
#     divisorList = []
#     for i in range (1, math.isqrt(n)+1):
#         if n%i == 0:
#             divisorList.append(i)
#             if n//i != i:
#                 divisorList.append(n//i)
#     # print(sorted(divisorList)) #[1, 2, 3, 4, 6, 9, 12, 18, 36]
#     print(divisorList)          #[1, 36, 2, 18, 3, 12, 4, 9, 6]
    
# getDivisors(36)


# get proper sorted data
def getDivisors(n: int):
    if n <= 0:
        raise ValueError("Divisors are defined only for positive integers")
    small, large = [], []

    for i in range(1, math.isqrt(n) + 1):
            if n % i == 0:
                small.append(i)
                if n // i != i:
                    large.append(n // i)
    print(small + large[::-1])

getDivisors(36)