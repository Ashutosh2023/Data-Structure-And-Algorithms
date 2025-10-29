class Solution:
    def hammingDistance(self, n1: int, n2: int) -> int:
        x = n1 ^ n2 
        setBits = 0

        while (x > 0) :
            setBits += x & 1
            x >>= 1
        
        return setBits 