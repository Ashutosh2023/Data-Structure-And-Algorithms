def singleNonDuplicate(nums: list[int], low: int, high: int):
    print(low, high)
    mid = (low + high) // 2
    if low == high:
        return nums[low]
    if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
        return nums[mid]
    if mid%2 == 0:
        if nums[mid] == nums[mid+1]:
            low = mid + 1
        else:
            high = mid - 1
    else:
        if nums[mid] == nums[mid-1]:
            low = mid + 1
        else:
            high = mid - 1
    
    return singleNonDuplicate(nums, low, high)

nums = [1,1,2,3,3,4,4,8,8]
print(singleNonDuplicate(nums,0, len(nums)-1))