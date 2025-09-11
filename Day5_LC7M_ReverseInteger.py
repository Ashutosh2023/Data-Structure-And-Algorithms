# This is faster
# class Solution:
#     def is_32bit_integer(n: int) -> bool:
#         return -2**31 <= n <= 2**31-1
#     def reverse(self, x: int) -> int:
#         isneg = x<0
#         x = int(str(abs(x))[::-1])
#         if not Solution.is_32bit_integer(x):
#             return 0
#         if isneg:
#             return -1 * x
#         return x

#This is the maths version of above
def reverse(x: int) -> int:
    isneg = x<0
    x = abs(x)

    ans = 0
    while True:
        ans = ans * 10 + x%10
        x //= 10
        if x == 0:
            break
    return -ans if isneg else ans

result = reverse(-0)
print(result)