class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        depth = 0
        
        for char in s:
            if char == '(':
                depth += 1
                if depth > 1:
                    result.append(char)
                    
            elif char == ')':
                if depth > 1:
                    result.append(char)
                depth -= 1
        
        return "".join(result)
    
parantheses = "(()())(())"
# parantheses = "(()())(())(()(()))"
# parantheses = "()()"
print(Solution().removeOuterParentheses(parantheses))