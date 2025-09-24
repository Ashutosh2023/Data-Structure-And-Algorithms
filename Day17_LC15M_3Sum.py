#time complexity O(n^2) and space: O(n)
def threeSum(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    result = set()
    for i in range(n):
        hashSet = set()
        for j in range(i+1,n):
            target = -(nums[i] + nums[j])
            if target in hashSet:
                triplet = tuple(sorted((nums[i], nums[j], target)))
                result.add(triplet)
            hashSet.add(nums[j])

    return [list(t) for t in result]

nums = [-1,0,1,2,-1,-4]
# result = threeSum(nums)
# print(result)

def threeSumOpt(nums: list[int]) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    result = []
    for i in range(n-2):
        if i>0 and nums[i] == nums[i-1]:
            continue
        j = i+1
        k = n-1
        while j<k:
            sum = nums[i] + nums[j] + nums[k]
            if sum < 0:
                j += 1
            elif sum > 0:
                k -= 1
            else:
                temp = [nums[i], nums[j], nums[k]]
                result.append(temp)
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                while k > j and nums[k] == nums[k+1]:
                    k -= 1
    return result

nums = [-1,0,1,2,-1,-4]
result = threeSumOpt(nums)
print(result)