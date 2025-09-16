def findMaxConsecutiveOnes(arr):
    max_count = 0
    count = 0
    for num in arr:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    print(max_count) 

findMaxConsecutiveOnes([1,0,1,1,1,1,1,0,1])