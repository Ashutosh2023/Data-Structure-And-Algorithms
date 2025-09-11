# get hcf or gcd of two numbers:
# def gcdOrHcf(x: int, y: int) -> int:
#     ans = 1
#     for i in range (min(x,y), 1, -1):
#         if x%i == 0 and y%i==0:
#             ans = i if i>ans else ans
#     return ans


#subtraction-based Euclidean algorithm for GCD/HCF
#gcd(10^9, 1) will loop 10^9 times 😱.
def gcdOrHcf(x: int, y: int) -> int:
    print("x:",x,"y:",y)
    while x != y:
        t = abs(x-y)
        y = min(x,y)
        x = t
        print("x:",x,"y:",y)
    return x

#same as the below code because i am just decreasing the bigger number by smaller number
##this is much simpler approach
def gcdOrHcfSimpler(x: int, y: int) -> int:
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x

# result = gcdOrHcfSimpler(52,10)
# print(result)



# %%%%%% MODULO version  O(log(min(x,y))) 
#gcd(10^9, 1) will not loop 10^9 times
#since i am decreasing the bigger number by smaller number until it's less than the smaller number
#is this not division by a number and you are left with the remainder which cannot be divided by a smaller number.
def gcdOrHcfOptimized(x: int, y: int) -> int:
    while x>0 and y>0:
        if x > y:
            x = x % y
        else:
            y = y % x
    return max(x,y)
n1 = 36
n2 = 24
GCD = gcdOrHcfOptimized(n1, n2)
LCM = n1*n2/GCD
print("GCD:", GCD) #12
print("LCM:", LCM) #72


##Don't understand this but apparently this is the also good 
##see pepcoding video for GCD and LCM lecture 27
## this is valid because it does not matter if you do modulo of smaller by larger or larger my smaller (24,36) (x,y)
# because when you do smaller by larger it gives remainder as smaller number [x%y 24%36 = 24]
# now one number is larger number and other is the remainder[modulo value y=24 ] which is the smaller number 
# now the module will repeat it self.. but now it's swapped so (36,24) [36%24 == 12] (12, 24)
def gccdOrHcf(x: int, y: int) -> int:
    while y != 0:
        x, y = y, x % y
    return x

print(gccdOrHcf(0,24)) 
