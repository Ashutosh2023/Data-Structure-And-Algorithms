#count digits
def countDigits(x: int) -> int:
    count = 0
    while x != 0:
        x//=10
        count += 1
    return count

def armstrongNumber(x: int) -> bool:
    temp = x
    order = countDigits(x)
    result = 0
    while x != 0:
        result += pow(x%10, order)
        x //= 10
    return temp == result

result = armstrongNumber(9272)
print(result)