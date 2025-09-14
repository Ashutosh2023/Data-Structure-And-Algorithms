# 26. Remove Duplicates from Sorted Array

def removeDuplicates(arr: list[int]) -> int:
    i = 0
    j = 1
    while i < len(arr) and j < len(arr):
        if(arr[j]== arr[i]):
            j+=1
        else:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
            j+=1
    print(i+1) ##this will be the value k till where the array is distinct and sorted...
    print(arr)

removeDuplicates([0,0,1,1,1,2,2,3,3,4])
            