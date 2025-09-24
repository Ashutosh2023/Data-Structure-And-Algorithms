from collections import Counter
def majorityElement(nums: list[int]) -> list[int]:
    result = []
    n = len(nums)
    m = n//3
    count = Counter(nums)
    for k, v in count.items():
        if v > m:
            result.append(k)
    return result

nums = [3,2,3,4,4,4,4,3,3]
# result = majorityElement(nums)
# print(result)

def majorityElementOptm(nums: list[int]) -> list[int]:
    result = []
    n = len(nums)
    m = n//3
    cnt1 = cnt2 = 0
    el1 = el2 = None
    for i in range(n):
        if(cnt1 == 0 and el2 != nums[i]):
            cnt1 = 1
            el1 = nums[i]
        elif cnt2 == 0 and el1 != nums[i]:
            cnt2 = 1
            el2 = nums[i]
        elif nums[i] == el1:
            cnt1 += 1
        elif nums[i] == el2:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1
    for item in (el1, el2):
        if item is not None and nums.count(item) > m:
            result.append(item)
    return result

nums = [3,2,3,4,4,4,4,3,3]
result = majorityElementOptm(nums)
print(result)


# def majorityElement(self, nums: List[int]) -> List[int]:
#         # Phase 1: find up to two potential candidates
#         cand1 = cand2 = None
#         c1 = c2 = 0
#         for num in nums:
#             if num == cand1:
#                 c1 += 1
#             elif num == cand2:
#                 c2 += 1
#             elif c1 == 0:
#                 cand1, c1 = num, 1
#             elif c2 == 0:
#                 cand2, c2 = num, 1
#             else:
#                 c1 -= 1
#                 c2 -= 1

#         # Phase 2: verify counts
#         res = []
#         for c in (cand1, cand2):
#             if c is not None and nums.count(c) > len(nums)//3:
#                 res.append(c)
#         return res