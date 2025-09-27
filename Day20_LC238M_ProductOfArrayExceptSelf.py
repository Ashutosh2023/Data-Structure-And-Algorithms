#space O(2n)
def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    list1 = [1]*n
    list2 = [1]*n
    prefixProd = suffixProd = 1
    for i in range(n):
        prefixProd *= nums[i]
        suffixProd *= nums[n-i-1]
        list1[i] = prefixProd
        list2[n-i-1] = suffixProd

    nums[0] = list2[1]
    for i in range(1,n-1):
        nums[i] = list1[i-1] * list2[i+1]
    nums[n-1] = list1[n-2]
    return nums
    
# nums = [-1,1,2,-3,3]
# nums = [-1,1,0,-3,3]
# print(productExceptSelf(nums))

# Observation if it has more than 1 Zeros then all the values in array would be zero
# if there is one zero then on the place where zero was you will get a integer value others will be zero
def productExceptSelf(nums: list[int]) -> list[int]:
    zeros = 0
    idx = -1
    prod = 1
    n = len(nums)
    for i in range(n):
        if nums[i] == 0:
            zeros += 1
            idx = i
        else:
            prod *= nums[i]
    
    ans = [0] * n
    if zeros == 0:
        for i in range(n):
            ans[i] = prod//nums[i]
    elif zeros == 1:
        ans[idx] = prod
    
    return ans
    
nums = [-1,1,2,-3,3]
nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))