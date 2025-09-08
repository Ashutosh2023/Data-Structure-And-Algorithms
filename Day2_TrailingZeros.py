import math

def trailingZeros_optimized(n: int) -> int:
    """This function uses legendar's method to calculate trailing zeros
    how many times a prime number p divides n!

    Args:
        n (int): count trailing 0's of this number

    Returns:
        int: count of trailing zeros
    """
    count = 0
    i = 5
    while n//i > 0:
        count += n//i
        i *= 5
    return count

def trailingZeroes_BruteForce(n: int) -> int:
    """_summary_

    Args:
        n (int): the input for which to count 0's in factorial

    Returns:
        int: the count of 0 in the factorial
    """
    if n<0:
        return 0
       
    value = math.factorial(n)
    count = 0
    while value%10 == 0:
        value = value//10
        count += 1
    return count

print(trailingZeros_optimized(9999))