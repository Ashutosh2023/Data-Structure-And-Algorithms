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
    for i in range(n-2):                   ## fix the i change j and k
        if i>0 and nums[i] == nums[i-1]:   ## if two index are equivalent then continue and if not the first index(else will cause index error)
            continue
        j = i+1
        k = n-1
        while j<k:                         ## change j and k value to get 0
            sum = nums[i] + nums[j] + nums[k]
            if sum < 0:                    ## if sum<0 then increase the sum, how increase j as array is sorted in ascnding order
                j += 1                     ## so the intention is to get j+1 th value to get the bigger value since sum<0
            elif sum > 0:                  ## if sum>0 then decrease sum to get 0
                k -= 1                     ## do that by decreasing k to get a smaller value
            else:
                temp = [nums[i], nums[j], nums[k]]
                result.append(temp)
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j-1]: ## since array can have duplicate values, nums[i] = -1, j = 0, k = 1
                    j += 1                            ## sum is 0 but after i+1, if nums[i+1] = -1 same as nums[i] then will again get the same set
                while k > j and nums[k] == nums[k+1]: ## but we want the distinct triplets
                    k -= 1
    return result

nums = [-1,0,1,2,-1,-4]
result = threeSumOpt(nums)
print(result)