def BinarySearch(nums: list[int], low: int, high: int, target: int) -> int:
        if low > high:
            return -1
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return BinarySearch(nums,low, mid-1, target)
        else:
            return BinarySearch(nums,mid+1, high, target)

nums = [-1,0,3,5,9,12]
idx = BinarySearch(nums, 0, len(nums)-1, 2)
print(idx)