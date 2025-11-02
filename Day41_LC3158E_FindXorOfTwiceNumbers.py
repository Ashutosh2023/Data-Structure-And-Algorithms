#exploit the constraints that the size of the array is max 50 and num[i] is 0 to 50
class Solution:
    def duplicateNumbersXOR(self, nums: list[int]) -> int:
        checker = [False]*51
        result = 0
        for num in nums:
            if checker[num]:
                result ^= num
            else:
                checker[num] = True
        return result
    
nums = [2,14,47,34,19,29,4,38,10,5,45,10,18,11,28,12,39,20,50,9,28,27,36,35,41,35,23,21,5,18,3,11,3,29,25,46,45,42,43,19]
print(Solution().duplicateNumbersXOR(nums))