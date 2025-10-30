class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        
        while i >= 0 or j >= 0 or carry:
            # Get digit from a, or 0 if a is exhausted
            digit_a = int(a[i]) if i >= 0 else 0
            # Get digit from b, or 0 if b is exhausted
            digit_b = int(b[j]) if j >= 0 else 0
            
            # Calculate the sum
            current_sum = digit_a + digit_b + carry
            
            # Append the result bit (current_sum % 2)
            res.append(str(current_sum % 2))
            
            # Update the carry (current_sum // 2)
            carry = current_sum // 2
            
            # Move pointers
            i -= 1
            j -= 1
            
        # The result is built in reverse, so reverse and join
        return "".join(res[::-1])