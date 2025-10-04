def SearchSqrt(x):
    if x < 2:
        return x
    left, right = 2, x // 2
    while left <= right:
        mid = left + (right - left) // 2
        num = mid * mid
        if num == x:
            return mid
        elif num < x:
            left = mid + 1
        else:
            right = mid - 1
    return right

# print(SearchSqrt(8))

# Time Complexity: O(log n) : recursion
def SqrtBinarySearch(x: int, low: int, high: int) -> int:
    if low > high:
        return high
    mid = low + (high - low) // 2
    num = mid ** 2
    if num == x:
        return mid
    if num > x:
        high = mid-1
    else:
        low = mid+1
    return SqrtBinarySearch(x, low, high)
    
    
def FindSqrt(x: int) -> int:
    if x<2:
        return x
    return SqrtBinarySearch(x, 2, x // 2)

print(FindSqrt(2))