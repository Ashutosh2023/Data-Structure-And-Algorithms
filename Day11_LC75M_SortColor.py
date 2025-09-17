def sortColors(arr: list[int]) -> None:
        i = 0
        k = 0
        j = len(arr)-1
        while k<=j:
            if arr[k] == 0:
                arr[i], arr[k] = arr[k], arr[i]
                i += 1
                k += 1
            elif arr[k] == 1:
                k += 1
            else:
                arr[k], arr[j] = arr[j], arr[k]
                j -= 1

arr = [0,1,0,2,1,0,2]
sortColors(arr)
print(arr)