from collections import defaultdict
class Solution:
    def countSubarrayxorK(self, nums: list[int], k: int) -> int:
        # prefixXor maps the (cumulative XOR value : frequency of that value)
        prefixXor = defaultdict(int)
        
        # Initialize with prefixXor[0] = 1. 
        # This handles the case where the subarray starts at index 0 
        # (i.e., when current_xor ^ k = 0)
        prefixXor[0] = 1
        
        count = 0
        current_xor = 0
        
        for i in range(len(nums)):
            # 1. Update the running XOR sum
            current_xor ^= nums[i]
            
            # 2. Calculate the required prefix XOR value
            # required_prefix_xor = current_xor ^ k
            required_prefix_xor = current_xor ^ k
            
            # 3. Check if the required prefix exists in the map
            if required_prefix_xor in prefixXor:
                # If it exists, add its frequency to the total count
                count += prefixXor[required_prefix_xor]
                
            # 4. Update the map with the frequency of the current XOR sum
            # Must use current_xor, not nums[i]
            prefixXor[current_xor] += 1
            
        return count

nums = [4,2,2,6,4]
k = 6
print(Solution().countSubarrayxorK(nums, k))