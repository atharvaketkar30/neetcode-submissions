class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        A = 0
        maxA = 0
        def dfs(i,j):
            
            if i >= ROWS or j >= COLS or i < 0 or j < 0:
                return 0
            if grid[i][j] == 0:
                return 0
            
            visited.add((i,j))
            area = 1
            
            for d in dirs:
                new_i = i + d[0]
                new_j = j + d[1]

                if 0 <= new_i < ROWS and 0 <= new_j < COLS:
                    if (new_i, new_j) not in visited and grid[new_i][new_j]==1:
                        print(new_i,new_j)
                        
                        area += dfs(new_i, new_j)
            
            return area

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    A = dfs(i,j)
                    # print(visited)
                    maxA = max(A, maxA)

        return maxA
