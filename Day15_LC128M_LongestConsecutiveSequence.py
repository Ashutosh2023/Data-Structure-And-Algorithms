#Time Complexity O(nlogn) due to sorting
def longestConsecutive(nums: list[int]) -> int:
    if(len(nums) == 0):
        return 0
    nums.sort()
    count = 1
    maxcount = 1
    for i in range(1,len(nums)):
        if nums[i]-1 == nums[i-1]:
            count += 1
            maxcount = max(maxcount, count)
            continue
        elif nums[i] == nums[i-1]:
            continue
        count = 1
    return maxcount


def longestConsecutive(nums: list[int]) -> int:
    num_set = set(nums)
    longest = 0
    for n in num_set:
        if n - 1 not in num_set:
            length = 1
            while n + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest


nums = [100,4,200,1,3,2]
nums = [1,2,3,5,6,7,8,9]
nums = [0,3,7,2,5,8,4,6,0,1] #9
# nums = [1,0,1,2] #3
print(longestConsecutive(nums))