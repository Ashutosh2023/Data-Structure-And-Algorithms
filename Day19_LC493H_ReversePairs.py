def reversePairs(nums: list[int]) -> int:
    n = len(nums)
    counter = 0
    for j in range(n-1, 0, -1):
        for i in range(j-1, -1, -1):
            if nums[i] > 2*nums[j]:
                counter += 1
    return counter

nums = [2,4,3,5,1]
print(reversePairs(nums))