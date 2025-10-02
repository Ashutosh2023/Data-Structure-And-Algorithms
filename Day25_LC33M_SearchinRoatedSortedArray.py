class Solution:
    @staticmethod
    def BinarySearch(nums: list[int], low: int, high: int, target: int) -> int:
        if low > high:
            return -1
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]:  # = for the edge case when low == mid i.e. the last element in recursion chaing
            # first half sorted
            if target >= nums[low] and target < nums[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            #second half sorted
            if target > nums[mid] and target <= nums[high]:
                low = mid+1
            else:
                high = mid-1
        return Solution.BinarySearch(nums,low, high, target)
    
    def search(self, nums: list[int], target: int) -> int:
        return Solution.BinarySearch(nums, 0, len(nums)-1, target)
    
nums = [3,1]
target = 1
print(Solution().search(nums,target))