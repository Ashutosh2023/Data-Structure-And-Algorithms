from collections import defaultdict


def majorityElement(nums: list[int]) -> list[int]:
    result = []
    n = len(nums)
    m = n//3
    count = defaultdict(int)
    for num in nums:
        count[num] += 1
    for k, v in count.items():
        if v > m:
            result.append(k)
    return result

nums = [3,2,3,4,4,4,4,3,3]
result = majorityElement(nums)
print(result)