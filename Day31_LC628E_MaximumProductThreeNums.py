# if array contains only positive integers
def maxprod(nums: list[int]) -> int:
    i = j = k = -2**31
    for x in nums:
        if x > k:
            i = j
            j = k
            k = x
        elif x > j:
            i = j
            j = x
        elif x > i:
            i = x
    return i*j*k

def maxprod2(nums: list[int]) -> int:
    nums.sort()
    return(max(nums[0]*nums[1]*nums[len(nums)-1], nums[len(nums)-1]*nums[len(nums)-2]*nums[len(nums)-3]))

nums = [-100,-98,-1,2,3,4]
print(maxprod2(nums))
