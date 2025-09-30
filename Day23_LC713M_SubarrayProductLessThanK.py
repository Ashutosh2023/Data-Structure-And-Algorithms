## could be brute force O(n^2) if all the items are 1 (this say if k is too big and product is never greater than K)
def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    count = 0
    if k == 0:
        return count
    n = len(nums)
    for i in range(n):
        prod = 1
        j = i
        while j < n:
            prod *= nums[j]
            if prod >= k:
                break
            count += 1
            j += 1
    return count


# nums, k = [10,5,2,6], 100
# nums, k = [1,2,3], 0
# print(numSubarrayProductLessThanK(nums, k))



def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    if k<= 1:
        return 0
    prod = 1
    left = 0
    count = 0
    for right, val in enumerate(nums):
        prod *= val
        while prod >= k:
            prod //= nums[left]
            left += 1
        count += right-left + 1        # all subarrays ending at `right` with start >= left are valid
                                       # left, left+1, …, right
    return count

# nums, k = [10,5,2,6], 100
# nums, k = [1,2,3], 0
nums, k = [1,1,1], 1
print(numSubarrayProductLessThanK(nums, k))