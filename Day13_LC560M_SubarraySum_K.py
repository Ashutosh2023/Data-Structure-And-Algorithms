def subarraySumK(arr: list[int], k) -> int:
    n = len(arr)
    count = 0
    for i in range(n):
        currSum = 0
        if currSum == k:
                count += 1
        for j in range(i,n):
            currSum += arr[j]
            if currSum == k:
                count += 1
    return count

nums = [1,1,1]
# print(subarraySumK(nums, 1))

# Why count += prefix_map[prefix_sum - k] instead of count += 1?
# 👉 Because there may be multiple previous prefix sums that make a valid subarray.
def subarraySumEqualsKOpt(arr: list[int], k) -> int:
    count = 0
    prefix_sum = 0
    prefix_map = {0:1}

    for num in arr:
        prefix_sum += num

        if prefix_sum - k in prefix_map:
            print("before::",count,"val:", prefix_map[prefix_sum-k])
            count += prefix_map[prefix_sum-k]
            print("after::",count)
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
        print("num::",num," prefix_sum::", prefix_sum," count::", count)
        print("map::", prefix_map)
        print()
    return count

nums = [4,-1,1,-1,1]
print(subarraySumEqualsKOpt(nums, 0))  # if you run this it will be 4:3 after summing there are two changes where 
#you would get the prefixsum as 4 means that two subarrays sum == 0 if we do not conside array till prefix sum = 4