def sortArrayByParityII(nums: list[int]) -> list[int]:
    res = [0]*len(nums)
    oddPos, evenPos = 1, 0
    for x in nums:
        if x%2 == 1:
            res[oddPos] = x
            oddPos += 2
        else:
            res[evenPos] = x
            evenPos += 2
    return res

nums = [4,2,5,7]
print(sortArrayByParityII(nums))