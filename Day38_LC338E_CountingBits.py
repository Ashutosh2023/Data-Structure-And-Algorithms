class Solution:
    def hammingWeight(self, x: int) -> int:
        count = 0
        while x > 0:
            if x & 1:
                count += 1
            x = x >> 1
        return count

    def countBits(self, n: int) -> list[int]:
        result = []
        for i in range(n + 1):
            result.append(self.hammingWeight(i))
        return result
    
x = 5
print(Solution().countBits(x))