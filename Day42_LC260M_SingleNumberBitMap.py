from typing import List

class Solution:
    def singleNumber(self, arr: List[int]) -> List[int]:
        xor_all = 0
        for num in arr:
            xor_all ^= num

        # get rightmost set bit
        rightmost_set_bit = xor_all & -xor_all

        a = b = 0
        for num in arr:
            if num & rightmost_set_bit:
                a ^= num
            else:
                b ^= num

        return [a, b]
    
nums = [1,2,1,3,2,5]
print(Solution().singleNumber(nums))