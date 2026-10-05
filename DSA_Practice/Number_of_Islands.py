
grid = [
    ['1', '1', '0', '0'],
    ['1', '0', '0', '1'],
    ['0', '0', '1', '1']
]

def dfs(row, col):
    if row < 0 or row >= len(grid):
        return
    if col < 0 or col >= len(grid[0]):
        return
    if grid[row][col] == '0':
        return
    
    grid[row][col] = '0'
    dfs(row + 1, col)
    dfs(row - 1, col)
    dfs(row, col + 1)
    dfs(row, col - 1)

count = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '1':
            count += 1
            dfs(i, j)

print(count)
