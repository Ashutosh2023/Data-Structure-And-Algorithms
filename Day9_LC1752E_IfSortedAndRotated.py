# Optimized solution
# if the value of digit next to a digit is drops only 1 time then it's because of rotation 
# if more than once then it is unsorted.
def checkArray(nums):
    count_drop = 0
    n = len(nums)
    for i in range(n):
        print(i, "::", (i+1) % n)
        if nums[i] > nums[(i+1) % n]:
            count_drop += 1
            print(count_drop)
            if count_drop > 1:
                return False
    return True

nums = [1,2,1]
print(checkArray(nums))
