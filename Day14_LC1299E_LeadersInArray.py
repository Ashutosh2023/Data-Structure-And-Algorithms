def leadersInArray(arr: list[int]) -> list[int]:
    result = []
    n = len(arr)
    k = -1
    result.append(k)
    for i in range(n-1, 0, -1):
        if k<=arr[i]:
            k = arr[i]
        result.insert(0,k)
    return result

arr = [17,18,5,4,6,1]
print(leadersInArray(arr))