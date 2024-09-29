class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        def dfs(x, y):
            # If the current position is out of bounds or is water ('0'), return
            if x < 0 or x >= num_rows or y < 0 or y >= num_cols or grid[x][y] == '0':
                return
            # mark it as seen so change it to 0s
            grid[x][y] = '0'
            dfs(x + 1, y)
            dfs(x - 1, y)  
            dfs(x, y + 1)  
            dfs(x, y - 1)  
        island_count = 0
        
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == '1':
                    island_count += 1
                    dfs(i, j) 
                    
        return island_count