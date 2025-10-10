def extractPrefix(item: str, prefix: str) -> str:
    match = []
    for i,(a, b) in enumerate(zip(item, prefix)):
        if a == b:
            match.append(a)
        else:
            break
    return "".join(match)

def longestCommonPrefix(strs: list[str]) -> str:
    prefix = strs[0]
    for x in strs:
        prefix = extractPrefix(x, prefix)
    return prefix


strs = ["flower","flow","flight"]
# print(longestCommonPrefix(strs))

# better approach sort lexographically and then compare the first and the last element only
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()
        s1 = strs[0]
        s2 = strs[-1]
        
        prefix_length = 0
        min_len = min(len(s1), len(s2))
        
        while prefix_length < min_len and s1[prefix_length] == s2[prefix_length]:
            prefix_length += 1
            
        return s1[:prefix_length]
    
strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))