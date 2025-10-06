def countDays(nums: list[int], capacity: int) -> int:
    days = 1
    currLoad = 0
    for x in nums:
        if currLoad + x <= capacity:
            currLoad += x
        else:
            days += 1
            currLoad = x
    return days

def searchMinumumCapacity(nums: list[int], days: int, low: int, high: int) -> int:
    minCapacity = 0
    while low <= high:
        mid = low + (high - low)//2
        currDays = countDays(nums, mid)
        print(mid, low, high, currDays)
        if currDays <= days:
            high = mid-1
            minCapacity = mid
        else:
            low = mid+1
    return minCapacity

def shipWithinDays(nums: list[int], days: int) -> int:
    low = max(nums)
    high = sum(nums)
    return searchMinumumCapacity(nums, days, low, high)

nums = [1,2,3,1,1]
days = 4
print(shipWithinDays(nums, days))