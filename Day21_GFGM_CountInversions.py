# Brute Force Count Inversions: O(n^2)
def countInversion(nums: list[int]) -> int:
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i,n):
            if nums[i] > nums[j]:
                count += 1

    return count

# nums = [5,3,2,4,1]
# print(countInversion(nums))


# O(nlogn) solution using the merge sort algo
def merge(nums: list[int], low: int, mid: int, high: int) -> int:
    count = 0
    left = low
    right = mid
    temp = []
    while left<mid and right<high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            count += mid-left
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

    return count

def mergeSort(nums: list[int],low: int, high: int) -> int:
    count = 0
    mid = (low+high)//2
    if mid == low:
        return count
    count += mergeSort(nums, low, mid)
    count += mergeSort(nums, mid, high)
    count += merge(nums, low, mid, high)

    return count

def inversionCount(nums: list[int]):
    count = 0
    count = mergeSort(nums, 0, len(nums))
    return count

nums = [5,3,2,4,1]
print("count::",inversionCount(nums))
print(nums)


#gfg version
class Solution:
    count = 0
    def inversionCount(self, nums):
        # Code Here
        self.count = 0
        self._mergeSort(nums, 0, len(nums))
        return self.count
        
    def _merge(self, nums, low, mid, high):
        left = low
        right = mid
        temp = []
        while left<mid and right<high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                self.count += mid-left
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
    
    def _mergeSort(self, nums: list[int],low: int, high: int):
        mid = (low+high)//2
        if mid == low:
            return
        self._mergeSort(nums, low, mid)
        self._mergeSort(nums, mid, high)
        self._merge(nums, low, mid, high)