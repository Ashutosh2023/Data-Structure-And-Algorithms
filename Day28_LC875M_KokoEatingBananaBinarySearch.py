# Brute Force O(n^2) Time Complexity
import math
def countHours(nums: list[int], rate: int) -> int:
    currHrs = 0
    for x in nums:
        currHrs += math.ceil(x/rate)
    return currHrs
def binarySearchMinEatingSpeed(nums: list[int], h: int, low: int, high: int) -> int:
    if low > high:
        return low
    mid = low + (high - low) // 2
    midHours = countHours(nums, mid)
    if midHours <= h:
        high = mid-1
    else:
        low = mid+1
    return binarySearchMinEatingSpeed(nums, h, low, high)

def minEatingspeed(nums: list[int], h: int) -> int:
    maxRate = max(nums)
    return binarySearchMinEatingSpeed(nums, h, 1, maxRate)
    # for i in range(1, maxRate+1):
    #     currHours = countHours(nums, i)
    #     if currHours <= h:
    #         return i
    return -1


piles = [30,11,23,4,20]
h = 5
print(minEatingspeed(piles, h))

