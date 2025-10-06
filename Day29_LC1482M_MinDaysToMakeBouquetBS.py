def countAdjacentBlooms(nums: list[int], k: int, day: int) -> int:
    boquetCount = 0
    count = 0
    for x in nums:
        if x <= day:
            count += 1
        else:
            count = 0
        if count == k:
            boquetCount += 1
            count = 0
    return boquetCount

def SearchBloomDay(nums: list[int], m: int, k: int, low: int, high: int) -> int:
    if low > high:
        return low
    mid = low + (high - low)//2
    currentBouquets = countAdjacentBlooms(nums, k, mid)
    if currentBouquets >= m:
        high = mid-1
    else:
        low = mid+1
    return SearchBloomDay(nums, m, k, low, high)
    
def minDays(bloomDays: list[int], m: int, k: int) -> int:
    n = len(bloomDays)
    if m*k > n:    # less flowers than required
        return -1 
    low = min(bloomDays)
    high = max(bloomDays)
    return SearchBloomDay(bloomDays, m, k, low, high)

nums = [1,10,3,10,2]
k = 1
m = 3
print(minDays(nums, m, k))