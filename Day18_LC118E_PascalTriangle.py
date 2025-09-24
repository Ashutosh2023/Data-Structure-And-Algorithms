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


def getRow(rowIndex: int) -> list[int]:
    row = [1]
    for k in range(1, rowIndex + 1):
        row.append(row[-1] * (rowIndex - k + 1) // k)
    return row

print(getRow(4))