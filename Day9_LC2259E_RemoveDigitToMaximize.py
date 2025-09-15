# O(n2)
def removeDigit(number: str, digit: str) -> str:
    dig = int(digit)
    digit_list = [int(digit) for digit in number]
    
    value = ""
    for i in range(len(digit_list)):
        temp = digit_list.copy()
        if(digit_list[i] == dig):
            temp.pop(i)
            t = "".join(map(str, temp))
            if t > value:
                value = t
    return value


print(removeDigit("2142","2"))


# O(n)
# Removing an earlier occurrence of digit can give a bigger result if the next digit is larger.
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        for i in range(len(number) - 1):
            if number[i] == digit and number[i + 1] > digit:
                return number[:i] + number[i+1:]
        j = number.rfind(digit)
        return number[:j] + number[j+1:]

print(Solution().removeDigit("1231","1"))