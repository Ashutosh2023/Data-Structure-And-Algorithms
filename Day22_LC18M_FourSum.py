def fourSum(nums: list[int], target: int) -> list[list[int]]:
    result = set()
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum == target:
                        quadruplet = tuple(sorted((nums[i], nums[j], nums[k], nums[l])))
                        result.add(quadruplet)
    return result

target = 0
nums = [1,0,-1,0,-2,2]
# print(fourSum(nums, target))

## Time: O(n^3) space: O(n) _ O(quad)
def fourSumm(nums: list[int], target: int) -> list[list[int]]:
    result = set()
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            hashSet = set()
            for k in range(j+1, n):
                fourth = target - (nums[i]+ nums[j]+ nums[k])
                if fourth in hashSet:
                    quadruplet = tuple(sorted((nums[i], nums[j], nums[k], fourth)))
                    result.add(quadruplet)
                hashSet.add(nums[k])
                    
    return [list(t) for t in result]

target = 0
nums = [1,0,-1,0,-2,2]
# print(fourSumm(nums, target))

# lets remove the space complexity::
# Time: O(n^3)
# works well passed all test cased 541ms beats 17.91%
def fourSummm(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    result = set()
    for x in range(n):
        for i in range(x+1,n-2):
            j = i+1
            k = n-1
            while j<k:
                sum = nums[x] + nums[i] + nums[j] + nums[k]
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
                else:
                    quadruplet = tuple(sorted((nums[x], nums[i], nums[j], nums[k])))
                    result.add(quadruplet)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
    return [list(t) for t in result]

target = 0
nums = [1,0,-1,0,-2,2]
# print(fourSummm(nums, target))

## a bit more optimized for the duplicate at first for x and i
# works well passed all test cased 371ms beats 74.32%
def fourSummm(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    result = []
    for x in range(n):
        if x > 0 and nums[x] == nums[x-1]:  # Skip duplicates for the outermost pointer 'x'
            continue
        for i in range(x+1,n-2):
            if i > x + 1 and nums[i] == nums[i-1]: # Skip duplicates for the second pointer 'i', check 'i' > x + 1 to ensure we aren't comparing 'i' to 'x' itself
                continue
            j = i+1
            k = n-1
            while j<k:
                current_sum = nums[x] + nums[i] + nums[j] + nums[k]
                if current_sum < target:
                    j += 1
                elif current_sum > target:
                    k -= 1
                else:
                    temp = [nums[x], nums[i], nums[j], nums[k]]
                    result.append(temp)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
    return result

target = 0
nums = [1,0,-1,0,-2,2]
print(fourSummm(nums, target))