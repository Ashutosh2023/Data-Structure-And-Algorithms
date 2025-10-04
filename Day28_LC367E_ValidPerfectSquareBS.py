# Time Complexity: O(log n) : recursion
def SqrtBinarySearch(x: int, low: int, high: int) -> bool:
    if low > high:
        return False
    mid = low + (high - low) // 2
    print(mid)
    num = mid ** 2
    if num == x:
        return True
    if num > x:
        high = mid-1
    else:
        low = mid+1
    return SqrtBinarySearch(x, low, high)
    
    
def FindSqrt(x: int) -> bool:
    if x < 2:
        return True
    else:
        return SqrtBinarySearch(x, 2, x // 2)

print(FindSqrt(9))