def PowerOf(x: int, n: int) -> int:
    ans = 1
    while n>0:
        if(n%2 == 1):
            n -= 1
            ans *= x
        x *= x
        n = n//2
    return ans

print(PowerOf(2, 5))