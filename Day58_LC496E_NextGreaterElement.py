class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Map from number -> next greater element in nums2
        next_greater = {}
        stack = []  # Monotonic decreasing stack

        # Process nums2 from right to left
        for num in reversed(nums2):
            # Pop all smaller or equal elements (they can't be next greater for 'num')
            while stack and stack[-1] <= num:
                stack.pop()
            
            # If stack not empty, top is next greater; otherwise -1
            next_greater[num] = stack[-1] if stack else -1
            
            # Push current number onto stack
            stack.append(num)

        # Build result for nums1 using the map
        return [next_greater[num] for num in nums1]


