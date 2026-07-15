class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if row >= rows or col >= cols or row < 0 or col < 0 or grid[row][col] == 0:
                return 1

            if (row, col) in visited:
                return 0

            visited.add((row, col))

            perim = dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)

            return perim

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return dfs(row, col)

