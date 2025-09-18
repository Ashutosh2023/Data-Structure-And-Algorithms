#Kadane's Algorithm very close to Kadane's algo but 
#there is a bug is all values are negative it will return zero but it should return largest negative num
#[-2,-1,-5] -> -1
def maxSumSubarray(arr: list[int]) -> int:
    maxSum = currSum = 0
    for i in range(len(arr)):
        currSum = currSum + arr[i]
        if(currSum > maxSum):
            maxSum = currSum
        if currSum < 0:
            currSum = 0
    return maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4]
# print(maxSumSubarray(nums))


#complete kadane's algo handles all negative value
# def maxSumSubarray(arr: list[int]) -> int:
#     maxSum = currSum = arr[0]
#     for i in range(1, len(arr)):
#         currSum = currSum + arr[i]
#         if(currSum > maxSum):
#             maxSum = currSum
#         if currSum < arr[i]:
#             currSum = arr[i]
#     return maxSum

#short form
def maxSumSubarray(arr: list[int]) -> int:
    maxSum = currSum = arr[0]
    for i in range(1, len(arr)):
        currSum = max(arr[i], currSum + arr[i])
        maxSum = max(maxSum, currSum)
    return maxSum

# nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [1]
# nums = [5,4,-1,7,8]
nums = [-2,-1,-5]
print(maxSumSubarray(nums))