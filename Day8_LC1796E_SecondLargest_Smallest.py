# Leetcode 1796 Second Largest Digit in a String...
def secondLargest(s):
    digitsSet = {int(char) for char in s if char.isdigit()}
    arr = list(digitsSet)
    if(len(arr) == 1 or not arr):
        print(-1)
    max = arr[1]
    max_his = -2**31

    for i in arr:
        if i > max:
            max_his = max
            max = i
        if i>max_his and i<max:
            max_his = i
    print(max)
    print(max_his)

secondLargest("dfa12321afd")

def secondSmallest(s):
    digitsSet = {int(char) for char in s if char.isdigit()}
    arr = list(digitsSet)
    if(len(arr) == 1 or not arr):
        print(-1)
    min = arr[1]
    min_his = 2**31-1

    for i in arr:
        if i < min:
            min_his = min
            min = i
        if i>min_his and i<min:
            min_his = i
    print(min)
    print(min_his)

secondSmallest("dfa12321afd")