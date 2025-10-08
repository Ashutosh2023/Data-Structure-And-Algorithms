def subarraysLessThanMax(nums: list[int], m: int):
    count = 0
    currsum = 0
    for x in nums:
        currsum+=x
        if currsum > m:
            count += 1
            currsum = x
    return count+1

def searchMinLargest(nums: list[int], k: int, low: int, high: int):
    while low<=high:
        mid = low + (high-low)//2
        count = subarraysLessThanMax(nums, mid)
        if count > k:
            low = mid+1
        else:
            high = mid-1
    return low

def allocateBooks(nums: list[int], k: int):
    low = max(nums)
    high = sum(nums)
    return searchMinLargest(nums, k, low, high)

nums = [12, 34, 67, 90]
k = 2
# print(subarraysLessThanMax(nums, 113))
print(allocateBooks(nums, k))