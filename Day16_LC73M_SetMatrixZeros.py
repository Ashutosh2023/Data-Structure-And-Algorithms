#O(m+n) auxillary space to store which row to mark as 0
def setZeros(matrix: list[list[int]]) -> None:
    r = len(matrix)
    c = len(matrix[0]) if r > 0 else 0
    rows = [0]*r
    cols = [0]*c
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                rows[i] = 1
                cols[j] = 1
    for i in range(r):
        for j in range(c):
            if rows[i] == 1 or cols[j] == 1:
                matrix[i][j] = 0


# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
matrix = [[1,0,1],[1,1,1],[1,1,1]]
# setZeros(matrix)
# print(matrix)

#O(1) extra space
#without any extra space use the first row and column as a marker
#then traverse again using those markers...
def setZerosOpt(matrix: list[list[int]]) -> None:
    r = len(matrix)
    c = len(matrix[0]) if r > 0 else 0
    c0 = 1
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j == 0:
                    c0 = 0
                else:
                    matrix[0][j] = 0
    print("second::")
    print(matrix)
    for i in range(1,r):
        for j in range(1,c):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if matrix[0][0] == 0:
        for j in range(c):
            matrix[0][j] = 0
    if c0 == 0:
        for i in range(r):
            matrix[i][0] = 0

# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
matrix = [[1,0,1],[1,1,1],[1,1,1]]
setZerosOpt(matrix)
print(matrix)