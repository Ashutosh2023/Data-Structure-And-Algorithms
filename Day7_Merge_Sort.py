def merge(nums: list[int], low: int, mid: int, high: int):
    left = low
    right = mid
    temp = []
    while left<mid and right<high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right += 1
        
    while left<mid:
        temp.append(nums[left])
        left += 1
    while right<high:
        temp.append(nums[right])
        right += 1
    
    for i in range(low, high):
        nums[i] = temp[i-low]

def mergeSort(nums: list[int],low: int, high: int):
    mid = (low+high)//2
    if mid == low:
        return
    mergeSort(nums, low, mid)
    mergeSort(nums, mid, high)
    merge(nums, low, mid, high)

# nums = [-1,5,3,4,0]
# mergeSort(nums, 0, len(nums))
# print(nums)

#leetcode version
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        self._mergeSort(nums, 0, len(nums))
        return nums

    def _mergeSort(self, nums: list[int], low: int, high: int):
        if high - low <= 1:
            return

        mid = (low + high) // 2
        
        self._mergeSort(nums, low, mid)
        self._mergeSort(nums, mid, high)

        self._merge(nums, low, mid, high)

    def _merge(self, nums: list[int], low: int, mid: int, high: int):
        left = low
        right = mid
        temp = []
        
        while left < mid and right < high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
            
        while left < mid:
            temp.append(nums[left])
            left += 1
            
        while right < high:
            temp.append(nums[right])
            right += 1
        
        for i in range(low, high):
            nums[i] = temp[i - low]

nums = [-1,5,3,4,0]
Solution().sortArray(nums)
print(nums)