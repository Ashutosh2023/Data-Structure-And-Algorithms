#explaination in copy
def singleNumber(nums):
    result = 0
    for i in range(32):  # check all 32 bits
        bit_sum = 0
        for num in nums:
            if (num >> i) & 1:
                bit_sum += 1
        # take mod 3
        if bit_sum % 3:
            # handle negative numbers (Python uses infinite-bit signed ints)
            if i == 31:  # sign bit
                result -= (1 << i)
            else:
                result |= (1 << i)
    return result

nums = [2,2,3,2]
print(singleNumber(nums))


#another optimized solution that i don't get
def singleNumberOptm(nums):
    ones, twos = 0, 0
    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones
    return ones

nums = [2,2,3,2]
print(singleNumberOptm(nums))