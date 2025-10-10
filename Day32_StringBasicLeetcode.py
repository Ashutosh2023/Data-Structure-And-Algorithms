class Solution:
    def reverseWords(self, s: str) -> str:
        s2 = s.split()
        return " ".join(s2[::-1])
    
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[0:i+1]
        return ""
    
s ="the sky is blue"
print(Solution().reverseWords(s))

num ="3542768"
print(Solution().largestOddNumber(num))