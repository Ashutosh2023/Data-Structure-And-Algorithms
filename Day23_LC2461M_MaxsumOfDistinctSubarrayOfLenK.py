from collections import defaultdict
#work but TLE
def maximumSubarraySum(nums: list[int], k: int) -> int:
    maxSum = 0
    count = 0
    for i in range(len(nums)-k+1):
        dist = set()
        j = 0
        sum = 0
        count = 0
        while j<k:
            if nums[j+i] not in dist:
                count += 1
            else:
                break
            dist.add(nums[j+i])
            sum += nums[j+i]
            j += 1
        print(sum,dist)
        if count == k:
            maxSum = max(sum, maxSum)
    print(maxSum)

# nums = [9,9,9,1,2,3]
# k = 3
# maximumSubarraySum(nums,k)


#optm
def maximumSubarraySum(nums: list[int], k: int):
    distMap = defaultdict(int)
    maxSum = sum = 0
    i = j = 0
    while j < len(nums):
        if j-i >= k:
            distMap.pop(nums[i])
            sum -= nums[i]
            i += 1
            if nums[j] in distMap:
                idx = distMap.pop(nums[j])
                while i <= idx:
                    sum -= nums[i]
                    i += 1
            distMap[nums[j]] = j
            sum += nums[j]
            j += 1
            if sum > maxSum:
                maxSum = sum
        else:
            if nums[j] in distMap:
                idx = distMap.pop(nums[j])
                while i <= idx:
                    sum -= nums[i]
                    i += 1
            distMap[nums[j]] = j
            sum += nums[j]
            if j-i == k-1 and sum > maxSum:
                maxSum = sum
            j += 1
        print(distMap, sum, i, j, maxSum)
    print(maxSum)

nums = [1,1,1,1,1,1]
k = 3
maximumSubarraySum(nums,k)



        
        
