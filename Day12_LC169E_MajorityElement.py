#This uses extra space
def majorityElement(arr):
    k = len(arr) // 2
    count = {}
    for i in arr:
        count[i] = count.get(i, 0) + 1
        if count[i] > k:
            return i


#assume that input will always have a majority element
arr = [1,2,3,1,2,1,1,1]
# print(majorityElement(arr))


#optimized solution
#O(1) extra space, use the Boyer–Moore Voting Algorithm
def majorityElementOptm(arr) -> int:
    majority = arr[0]
    count = 1
    for i in range (1,len(arr)):
        if arr[i] == majority:
            count+=1
        else:
            count-=1
        if count == 0:
            majority = arr[i]
            count = 1
    return majority

nums = [2,2,1,1,1,2,2]
print(majorityElementOptm(nums))