class Solution:
    @staticmethod
    def BinarySearch(nums: list[int], low: int, high: int) -> int:
        if low > high:
            return -1
        mid = (low + high) // 2
        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return mid
        elif nums[mid] > nums[mid-1]:
            low = mid+1
        else: 
            high = mid-1
        return Solution.BinarySearch(nums,low, high)
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1
        return Solution.BinarySearch(nums, 1, n-2)

nums = [1,2,1,3,2]
peak = Solution().findPeakElement(nums)
print(peak)