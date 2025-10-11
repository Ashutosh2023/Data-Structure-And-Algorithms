#brute force
def RotateStringChecker(s: str, goal: str) -> bool:
    for i in range(len(s)):
        temp = s[i:] + s[0:i]
        print(temp, goal)
        if temp == goal:
            return True
    return False

# Double String Trick
# s = "abcde"
# goal = "cdeab"
# s + s = "abcdeabcde"
# "cdeab" is a substring → ✅
def RotateStringChecker(s: str, goal: str) -> bool:
    # lengths must match, else impossible
    if len(s) != len(goal):
        return False
    return goal in (s + s)
s = "abcde"
goal = "cdeab"
print(RotateStringChecker(s, goal))