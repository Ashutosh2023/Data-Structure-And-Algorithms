class Solution:
    def hammingWeight(self, x: int) -> int:
        count = 0
        while x > 0:
            x &= (x-1)
            count += 1
        return count

    def minBitFlips(self, start: int, goal: int) -> int:
        setbits = start^goal
        return self.hammingWeight(setbits)
    

Start = 10
Goal = 7
print(Solution().minBitFlips(Start, Goal))