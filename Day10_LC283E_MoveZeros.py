def MoveZeros(arr: list[int]):
    i = 0
    j = 0
    while j<len(arr):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        if arr[i] != 0:
            i+=1
            j+=1
            continue
        elif arr[i] == 0:
            j+=1
        
    print(arr)

MoveZeros([0,1,0,3,12])

def moveZeroesOpt(arr: list[int]) -> None:
    insert_pos = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[insert_pos] = arr[insert_pos], arr[i]
            insert_pos += 1
    print(arr)

moveZeroesOpt([0,1,0,3,12])