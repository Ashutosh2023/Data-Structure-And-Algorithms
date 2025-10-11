class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        maxdepth = 0
        for char in s:
            if char == '(':
                depth += 1
                maxdepth = max(depth, maxdepth)
                    
            elif char == ')':
                depth -= 1
        
        return maxdepth
    
parantheses = "(1+(2*3)+((8)/4))+1"
# parantheses = "(1)+((2))+(((3)))"
# parantheses = "()()"
print(Solution().maxDepth(parantheses))