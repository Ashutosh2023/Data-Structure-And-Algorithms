# When nums[low] == nums[mid] == nums[high], we can’t know which side is sorted.
# So the safe move is:
# shrink the window from both ends (low += 1, high -= 1)
# and continue
class Solution:
    @staticmethod
    def BinarySearch(nums: list[int], low: int, high: int, target: int) -> bool:
        if low > high:
            return False
        mid = (low + high) // 2
        print(low,high, mid)
        if nums[mid] == target:
            return True
        if nums[low] == nums[mid] == nums[high]: #we can’t know which side is sorted
            return (Solution.BinarySearch(nums, low+1, high-1, target))
        if nums[low] <= nums[mid]:
            if target >= nums[low] and target < nums[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if target > nums[mid] and target <= nums[high]:
                low = mid+1
            else:
                high = mid-1
        return Solution.BinarySearch(nums,low, high, target)
    
    def search(self, nums: list[int], target: int) -> bool:
        return Solution.BinarySearch(nums, 0, len(nums)-1, target)
    
nums = [1,0,1,1,1]
target = 0
print(Solution().search(nums,target))