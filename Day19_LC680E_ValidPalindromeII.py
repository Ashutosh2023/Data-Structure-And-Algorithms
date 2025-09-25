def palindrome(s: str) -> bool:
    i = 0
    j = len(s) - 1
    del_Counter = 0
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            del_Counter += 1
            if del_Counter > 1:
                return False
            if s[i] == s[j-1]:
                j -= 1
            elif s[i+1] == s[j]:
                i += 1
            else:
                return False
    return True if del_Counter <= 1 else False

s = "eceec"             #for this test case we don't know which one to omit i or j
print(palindrome(s))


##check palindrome after a mismatch or return true if no mismatch
def validPalindrome(s: str) -> bool:
    def is_pal(l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    i, j = 0, len(s) - 1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return is_pal(i + 1, j) or is_pal(i, j - 1) ## check both possiblities of any is palindrom then return true.
    return True
