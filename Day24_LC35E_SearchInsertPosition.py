def searchInsertPosition(nums: list[int], low: int, high: int, target: int) -> int:
    print(low, high)
    if low > high:
        return low
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] > target:
        return searchInsertPosition(nums,low, mid-1, target)
    else:
        return searchInsertPosition(nums,mid+1, high, target)

nums = [-1,1,4,5,9,12]
idx = searchInsertPosition(nums, 0, len(nums)-1, 2)
print(idx)