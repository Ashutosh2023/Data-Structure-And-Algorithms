class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for i in nums:
            result ^= i
        return result

nums = [2,2,1]
print(Solution().singleNumber(nums))