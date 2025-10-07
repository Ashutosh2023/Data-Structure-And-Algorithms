# 0ms Beats 100%  Time: O(n)
def missingNum(nums: list[int], k: int) -> int:
    n = len(nums)
    count = 0
    counter = 1
    i = 0
    while i<n and count<k:
        if nums[i] > counter:
            count += 1
        elif nums[i] == counter:
            i += 1
        counter += 1
    return counter+k-count-1

nums = [5,7,10,12]
k = 5
# print(missingNum(nums, k))

def missingNum2(nums: list[int], k: int, low: int, high: int) -> int:
    while low<=high:
        mid = low + (high - low)//2
        missingNums = nums[mid]-(mid+1)
        print(low, high, mid, "::",nums[mid],"-", mid+1, "=", nums[mid]-(mid+1))
        if missingNums < k:
            low = mid + 1
        else:
            high = mid - 1
    print(low, high)
    print(nums[high],"+",k,"-(",nums[high],"-(",high+1,"))=", k-(high+1))
    return k+(high+1)  #This simply represents k plus what more numbers are missing before nums[high]

nums = [2,3,4,7,11]
k = 5
print(missingNum2(nums, k, 0, len(nums)-1))