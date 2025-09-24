# n & (n - 1) performs a bitwise AND.
# The result is 0 because there is no bit position where both have a 1.

# 4 (0100)
# 3 (0011)
# &: 0000
def isPowerOfTwo(self, n: int) -> bool:
    return (n > 0) and ((n & (n - 1)) == 0)