def numIslands(grid):
    if not grid or not grid[0]:
        return 0

    def dfs(row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0':
            return

        grid[row][col] = '0'  # Mark the cell as visited

        # Explore the neighboring cells in all directions
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    num_islands = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '1':
                num_islands += 1
                dfs(row, col)

    return num_islands