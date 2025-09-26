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
nums = [-2,-3,-4]   #above code do not know which pair will give max value, it is taking first pair, bcoz it's working in one direction only
print(maxProductSubarray(nums))

## The idea is to get select the perfect negative number in case of odd number of negative values
## then take max from the prefix to the suffix of the -ve value
## that can be done if we have max value of products when starting from front and also from the back 
## which mean before and after each value would have been calculated and saved in maxprod
def maxProductSubarray(nums: list[int]) -> int:
    prefix = suffix = 1
    maxProd = nums[0]
    n = len(nums)
    for i in range(n):
        if(prefix == 0):  ## 0 means prefix product before 0 cannot be considered as it becomes 0
            prefix = 1
        if(suffix == 0):  ## take elements between zeros and record them in maxprod and make prefix and suffix 1 every time
            suffix = 1
        prefix *= nums[i]
        suffix *= nums[n - i -1]
        maxProd = max(maxProd, prefix, suffix)
    return maxProd

# nums = [-2,0,-1]
# nums = [2,3,-2,4]
nums = [-2,-3,-4]
# nums = [-2]
print(maxProductSubarray(nums))