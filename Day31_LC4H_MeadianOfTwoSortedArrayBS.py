# works-> beats 34.52% of the solution::
def medianOf2(a, b):
    n = len(a)
    m = len(b)
    i = 0
    j = 0

    # m1 to store the middle element
    # m2 to store the second middle element
    m1 = -1
    m2 = -1

    # loop till (m+n)/2
    for count in range((m + n) // 2 + 1):
        m2 = m1

        # if both the arrays have remaining elements
        if i != n and j != m:
            if a[i] > b[j]:
                m1 = b[j]
                j += 1
            else:
                m1 = a[i]
                i += 1

        # if only a[] has remaining elements
        elif i < n:
            m1 = a[i]
            i += 1

        # if only b[] has remaining elements
        else:
            m1 = b[j]
            j += 1

    # return median based on odd/even size
    if (m + n) % 2 == 1:
        return m1
    else:
        return (m1 + m2) / 2.0


if __name__ == "__main__":
    arr1 = [-5, 3, 6, 12, 15]
    arr2 = [-12, -10, -6, -3, 4, 10]
    print(medianOf2(arr1, arr2))