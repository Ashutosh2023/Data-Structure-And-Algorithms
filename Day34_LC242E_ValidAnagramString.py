from collections import defaultdict
def isAnagram(s: str, t: str) -> bool:  # fail for "aa", "cc"
    xor = 0
    for i in range(len(s)):
        xor ^= ord(s[i])
    for j in range(len(t)):
        xor ^= ord(t[j])
    if xor == 0:
        return True
    else:
        return False

def isAnagram2(s: str, t: str) -> bool:
    hashmap = defaultdict(int)
    for char in s:
        hashmap[char] += 1
    for char in t:
        hashmap[char] -= 1
    for count in hashmap.values():
        if count != 0:
            return False
    return True

s = "anagram"
t = "nagaram"
print(isAnagram2(s, t))