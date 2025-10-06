import math
def GetSumOfDivisor(nums: list[int], divisor: int) -> int:
    sum = 0
    for x in nums:
        sum += math.ceil(x/divisor)
    return sum

# def SearchSmallestDivisor(nums: list[int], threshold: int, low: int, high: int) -> int:
#     min_sum = -1
#     while low <= high:
#         mid = low + (high - low)//2
#         currentSum = GetSumOfDivisor(nums, mid)
#         print(mid, low, high, currentSum)
#         if currentSum<=threshold:
#             min_sum = currentSum
#             high = mid-1
#         else:
#             low = mid+1
#     return min_sum

def SearchSmallestDivisor(nums: list[int], threshold: int, low: int, high: int, min_valid_sum: int = -1) -> int:
    if low > high:
        return low
    mid = low + (high - low)//2
    currentSum = GetSumOfDivisor(nums, mid)
    # print(mid, low, high, currentSum)
    if currentSum <= threshold:
        min_valid_sum = currentSum
        high = mid-1
    else:
        low = mid+1
    return SearchSmallestDivisor(nums, threshold, low, high, min_valid_sum)
    
def minDivisor(nums: list[int], threshold: int) -> int:
    n = len(nums)
    low = 1
    high = max(nums)
    if n == threshold:
        return high
    elif n > threshold:
        return -1
    return SearchSmallestDivisor(nums, threshold, low, high, -1)

nums = [1,2,5,9]
threshold = 6
print(minDivisor(nums, threshold))