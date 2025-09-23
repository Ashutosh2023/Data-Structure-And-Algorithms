# def threeSum(nums: list[int]) -> list[list[int]]:
#     hashSet = set(nums)
#     n = len(nums)
#     result = []
#     for i in range(n):
#         for j in range(i+1,n):
#             print(i,j)
#             twoSum = nums[i]+nums[j]
#             target = 0 - twoSum
#             if target in hashSet:
#                 result.append([nums[i], nums[j], target])
#     return result

# nums = [-1,0,1,2,-1,-4]
# result = threeSum(nums)
# print(result)

def threeSum(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    result = []
    for i in range(n):
        hashSet = set()
        for j in range(i+1,n):
            second = 0 - nums[i] - nums[j]
            if second in hashSet:
                result.append([nums[i], nums[j], second])
            hashSet.add(nums[j])

    return result

nums = [-1,0,1,2,-1,-4,3]
result = threeSum(nums)
print(result)