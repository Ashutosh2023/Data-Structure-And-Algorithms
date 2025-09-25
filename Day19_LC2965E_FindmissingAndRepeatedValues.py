def findMissingAndRepeatedValues(grid: list[list[int]]) -> list[int]:
    n = len(grid)
    marker = [0] * (n * n)
    ans = [0, 0]
    for i in range(n):
        for j in range(n):
            marker[grid[i][j] - 1] += 1
    for i in range(n * n):
        if marker[i] == 0:
            ans[1] = i + 1           # missing
        elif marker[i] == 2:
            ans[0] = i + 1           # repeated
    return ans


grid = [[9,1,7],[8,9,2],[3,4,6]]
ans = findMissingAndRepeatedValues(grid)
print(ans)