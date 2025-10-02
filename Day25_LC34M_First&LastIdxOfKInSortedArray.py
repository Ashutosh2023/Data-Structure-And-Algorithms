class Solution:
    @staticmethod
    def BinarySearchFirst(nums: list[int], low: int, high: int, target: int) -> int:
        if low > high:
            return -1
        mid = (low + high) // 2
        if nums[mid] == target and (mid == 0 or nums[mid] > nums[mid-1]):
            return mid
        if nums[mid] >= target:
            return Solution.BinarySearchFirst(nums,low, mid-1, target)
        else:
            return Solution.BinarySearchFirst(nums,mid+1, high, target)
        
    @staticmethod   
    def BinarySearchLast(nums: list[int], low: int, high: int, target: int) -> int:
        if low > high:
            return -1
        mid = (low + high) // 2
        if nums[mid] == target and (mid+1 == len(nums) or nums[mid] < nums[mid+1]):
            return mid
        if nums[mid] > target:
            return Solution.BinarySearchLast(nums,low, mid-1, target)
        else:
            return Solution.BinarySearchLast(nums,mid+1, high, target)
    
    def searchRange(self, nums: list[int], target: int) -> int:
        first = last = -1
        first = Solution.BinarySearchFirst(nums, 0, len(nums)-1, target)
        last = Solution.BinarySearchLast(nums, 0, len(nums)-1, target)

        return [first, last]
    
nums = [1,2,3,4,5,6,7]
target = 7
print(Solution().searchRange(nums,target))