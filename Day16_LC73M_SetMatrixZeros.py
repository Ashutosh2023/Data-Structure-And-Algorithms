#O(m+n) auxillary space to store which row to mark as 0
def setZeros(matrix: list[list[int]]) -> None:
    r = len(matrix)
    c = len(matrix[0]) if r > 0 else 0
    print(c, r)
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
matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeros(matrix)
print(matrix)