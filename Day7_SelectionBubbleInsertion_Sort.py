# find the minimum index first, then swaps once per outer loop.
def selectionSort(arr) -> int:
    for i in range(len(arr)-1):
        minIdx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIdx]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]

arr = [2,6,4,8,9,3,1]
selectionSort(arr)
print(arr)

# In Bubble Sort, we compare adjacent elements (arr[j] and arr[j+1]) and push the largest element to the end in each pass.
def bubbleSort(arr) -> int:
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [2,6,4,8,9,3,1]
bubbleSort(arr)
print(arr)

# Insertion sort takes a element and place it at the correct position
# As the value of i increases the array till 0 to i is always sorted for that above condition is applied for on each 0 to i::
def insertionSort(arr):
    for i in range(len(arr)):
        j = i
        while j>0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1


arr = [2,6,4,8,9,3,1]
insertionSort(arr)
print(arr)
