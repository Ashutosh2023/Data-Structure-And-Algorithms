#My code::Wrong fails for -ve values..
def maxProductSubarray(nums: list[int]) -> int:
    maxProduct = 0
    currProduct = 1
    for i in range(len(nums)):
        if nums[i] == 0:
            currProduct = 1
            continue
        currProduct = currProduct * nums[i]
        maxProduct = max(maxProduct, currProduct)
    return maxProduct

# # nums = [-2,0,-1]
# nums = [2,3,4,0,6,6]
# # nums = [-2,3,-4]
# print(maxProductSubarray(nums))


def maxProductSubarray(nums: list[int]) -> int:
    prefix = suffix = 1
    maxProd = nums[0]
    n = len(nums)
    for i in range(n):
        if(prefix == 0):
            prefix = 1
        if(suffix == 0):
            suffix = 1
        prefix *= nums[i]
        suffix *= nums[n - i -1]
        maxProd = max(maxProd, prefix, suffix)
    return maxProd

nums = [-2,0,-1]
nums = [2,3,-2,4]
nums = [-2,-3,-4]
nums = [-2]
print(maxProductSubarray(nums))