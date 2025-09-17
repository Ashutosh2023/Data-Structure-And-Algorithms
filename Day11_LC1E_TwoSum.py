class Solution:
    def twoSum( self, arr: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(arr)):
            comp = target - arr[i]
            if comp in seen:
                return [seen[comp],i]
            seen[arr[i]] = i


my_array = [2, 7, 11, 15]
my_target = 9
print(Solution().twoSum(my_array,my_target))