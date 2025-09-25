def pascalTriangle(n: int) -> list[list[int]]:
    result = []
    for i in range(0,n):
        temp = [1]*(i+1)
        for j in range(1,i):
            temp[j] = result[-1][j-1] + result[-1][j]
        result.append(temp)
    return result


n = 5
response = pascalTriangle(n)
print(response)


def nth_pascal_row(n):
    if n < 0:
        return []

    # The first element is always 1 (which is nC0)
    row = [1]
    
    # 'res' stores the current binomial coefficient (nCk). 
    # It starts as nC0 = 1.
    res = 1 
    
    # Calculate nC1, nC2, ..., nCn
    # The loop runs for k from 1 up to n
    for k in range(1, n + 1):
        # Apply the formula: nCk = nC(k-1) * (n - k + 1) / k
        # We use integer division (//) since all results must be integers.
        res = res * (n - k + 1) // k
        row.append(res)
    return row

# Example usage:
n = 4
print(f"Row {n}:")
print(nth_pascal_row(n)) # Output: 1 4 6 4 1

# n = 6
# print(f"\nRow {n}:")
# print(nth_pascal_row(n)) # Output: 1 6 15 20 15 6 1


def pascal_row(n: int) -> list[int]:
    row = [1]
    for k in range(1, n + 1):
        row.append(row[-1] * (n - k + 1) // k) # Each element = previous_element * (n - k + 1) // k
    return row

# Example: print 5th row (0-indexed →  [1, 5, 10, 10, 5, 1])
# print(pascal_row(5))
