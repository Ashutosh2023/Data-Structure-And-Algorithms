class Solution:
    @staticmethod
    def BinarySearch(nums: list[int], low: int, high: int) -> int:
        if low == high:
            return low
        mid = (low + high) // 2
        print(low,high,mid)
        if nums[mid] > nums[high]:  #This is the tricky part to find the condition
            low = mid+1
        else:
            high = mid
        return Solution.BinarySearch(nums,low, high)
    
    def findMin(self, nums: list[int]) -> int:
        minIdx = Solution.BinarySearch(nums, 0, len(nums)-1)
        return nums[minIdx]
    
nums = [11,13,15,17]
print(Solution().findMin(nums))