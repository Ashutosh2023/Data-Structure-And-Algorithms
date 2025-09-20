def reArrangeArray(nums: list[int]) -> list[int]:
    result = []
    alt = 1
    i = j = 0
    count = 0
    while count<len(nums):
        if alt == 1:
            if i<len(nums) and nums[i] > 0:
                result.append(nums[i])
                alt = -1
                count += 1
            i += 1
        elif alt == -1:
            if nums[j] < 0:
                result.append(nums[j])
                alt = 1
                count += 1
            j += 1
    return result

nums = [1, 2, 3, -1, -2, -3]
# print(reArrangeArray(nums))


def reArrangeArray(nums: list[int]) -> list[int]:
    result = []
    alt = 1
    i = j = 0
    count = 0
    while count<len(nums):
        if alt == 1:
            if i<len(nums) and nums[i] > 0:
                result.append(nums[i])
                alt = -1
                count += 1
            i += 1
        elif alt == -1:
            if nums[j] < 0:
                result.append(nums[j])
                alt = 1
                count += 1
            j += 1
    return result

#different solution this also takes exta space...
def rearrangeArray(self, nums: list[int]) -> list[int]:
    positives = [x for x in nums if x > 0]
    negatives = [x for x in nums if x < 0]

    result = []
    for p, n in zip(positives, negatives):
        result.append(p)
        result.append(n)
    return result

nums = [1, 2, 3, -1, -2, -3]
# print(reArrangeArray(nums))

#extra spaces
def rearrangeArrayopt(self, nums: list[int]) -> list[int]:
    res = [0]*len(nums)
    pos, neg = 0, 1
    for x in nums:
        if x > 0:
            res[pos] = x
            pos += 2
        else:
            res[neg] = x
            neg += 2
    return res

nums = [1, 2, 3, -1, -2, -3]
print(reArrangeArray(nums))

# If you don’t care about preserving the original relative order of positives or negatives, 
# you can do it in O(1) extra space:
# Do a Dutch National Flag–style partition to put all positives on one side,
# negatives on the other (O(n) time, O(1) space).
# Then interleave by swapping elements from the positive and negative halves into alternating positions.
# But this will scramble the order inside each sign group, which would fail LeetCode’s tests.