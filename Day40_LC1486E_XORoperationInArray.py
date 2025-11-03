class Solution:
    def xor_upto(self, n: int) -> int:
        if n % 4 == 0:
            return n
        elif n % 4 == 1:
            return 1
        elif n % 4 == 2:
            return n + 1
        else:
            return 0

    def xorOperation(self, n: int, start: int) -> int:
        s = start >> 1        # divide by 2
        xor_seq = self.xor_upto(s + n - 1) ^ self.xor_upto(s - 1)
        result = xor_seq << 1 # multiply by 2

        # if start is odd and n is odd, flip the last bit
        if (start & 1) and (n & 1):
            result ^= 1
        return result
    
print(Solution().xorOperation(5,0))


def xorOperation(n: int, start: int) -> int:
    result = 0
    for i in range(n):
        result ^= start + 2 * i
    return result

print(xorOperation(4, 3))