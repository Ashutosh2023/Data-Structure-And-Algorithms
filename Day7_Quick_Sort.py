def partition(nums: list[int], low: int, high: int) -> int:
    pivot = nums[low]
    i = low
    j = high
    while j>=i:
        if pivot >= nums[i]:
            i += 1
            continue
        if pivot < nums[j]:
            j -= 1
            continue
        nums[i], nums[j] = nums[j], nums[i]
    nums[low], nums[j] = nums[j], nums[low]
    return j

def quickSort(nums: list[int], low: int, high: int):
    if low<high:
        idx = partition(nums, low, high)
        quickSort(nums, low, idx-1)
        quickSort(nums, idx+1, high)
    print("sort")


# nums = [5, 3, 4]
# quickSort(nums, 0, len(nums)-1)
# print(nums)







#leetcode version
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        self._quickSort(nums, 0, len(nums)-1)
        return nums
    
    def _partition(self, nums: list[int], low: int, high: int) -> int:
        pivot = nums[low]
        i = low
        j = high
        while j>=i:
            if pivot >= nums[i]:
                i += 1
                continue
            if pivot < nums[j]:
                j -= 1
                continue
            nums[i], nums[j] = nums[j], nums[i]
        nums[low], nums[j] = nums[j], nums[low]
        return j

    def _quickSort(self, nums: list[int], low: int, high: int):
        if low<high:
            idx = self._partition(nums, low, high)
            self._quickSort(nums, low, idx-1)
            self._quickSort(nums, idx+1, high)



nums = [5,2,3,1]
print(Solution().sortArray(nums))