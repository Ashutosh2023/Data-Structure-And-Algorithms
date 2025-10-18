#Bit Manipulation
# def countSetBits(x: int) -> int:
#     # print(x.bit_count()) #counts the 1 bits of a number x
#     length = x.bit_length()  #gives the count of number of bits required to represent number x in binary
#     count = 0
#     while length:
#         if x&1:
#             count+=1
#         length -= 1
#         x = x>>1
#     return count

# Time complexity Log(x)-> number of bits it takes to represent x
def countSetBits(x: int) -> int:
    print(x.bit_count()) #counts the 1 bits of a number x
    count = 0
    while x > 0:
        if x & 1:
            count += 1
        x = x >> 1
    return count

# Trick get LSB using n&(n-1) 
# Time Complexity O(t) t->is the count of number of set bits
def countSetBits2(x: int) -> int:
    print(x.bit_count()) #counts the 1 bits of a number x
    count = 0
    while x > 0:
        x &= (x-1)
        count += 1
    return count

n = 37
print(countSetBits2(n))
