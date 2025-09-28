def reversePairs(nums: list[int]) -> int:
    n = len(nums)
    counter = 0
    for j in range(n-1, 0, -1):
        for i in range(j-1, -1, -1):
            if nums[i] > 2*nums[j]:
                counter += 1
    return counter

nums = [2,4,3,5,1]
# print(reversePairs(nums))

# O(nlogn) solution using the merge sort algo
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

def countPairs(nums: list[int], low: int, mid: int, high: int) -> int:
    right = mid
    count = 0
    for i in range( low, mid):
        while right < high and nums[i] > 2*nums[right]:
            right += 1
        count += right - (mid)  # += means every element that was good for smaller i is also good to the next greater i
                                # so no need to count them again just do add the previous count
    return count

def mergeSort(nums: list[int],low: int, high: int) -> int:
    count = 0
    mid = (low+high)//2
    if mid == low:
        return count
    count += mergeSort(nums, low, mid)
    count += mergeSort(nums, mid, high)
    count +=  countPairs(nums, low, mid, high)
    merge(nums, low, mid, high)
    return count

nums = [1,3,2,3,1]
print("count::",mergeSort(nums, 0, len(nums)))
print(nums)