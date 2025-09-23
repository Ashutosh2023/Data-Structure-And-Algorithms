def spiralMatrix(matrix: list[list[int]]) -> list[int]:
    spiral = []
    n = len(matrix)
    m = len(matrix[0])
    left , right = 0, m-1
    top , bottom = 0, n-1

    while top <= bottom  and left <= right:
        for i in range(left, right+1):
            spiral.append(matrix[top][i])
        top += 1
        for i in range(top , bottom+1): 
            spiral.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left-1, -1):
                spiral.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top-1, -1):
                spiral.append(matrix[i][left])
            left += 1

    return spiral

# matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]  #test case:: if top <= bottom:
# matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]  #test case:: if left <= right: then loop
spiral = spiralMatrix(matrix)
print(spiral)