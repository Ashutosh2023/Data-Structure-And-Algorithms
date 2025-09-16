def MissingNumbers(nums: list[int]):
    sumVal = sum(nums)
    n = len(nums)
    mathVal = (n*(n+1))//2
    return mathVal - sumVal

print(MissingNumbers([9,6,4,2,3,5,7,0,1]))