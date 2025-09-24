def mergeSortedArray(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1


nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
mergeSortedArray(nums1, m, nums2, n)
print(nums1)