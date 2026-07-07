class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Input- Grid of 0 and 1
        Op- Among all children connected horizontal & vertical
        Output- How many connected 1 parent-child combos

        Start at top right
        0
       0   1
      1  1   1
        
        
        
        DFS to count 1s, mark that node as visited
        Start at 0,0 = 0
        Children = (1,0), (0,1) = 1
        Node = (0,1)
            Children (0,2) (1,2) (0,0)
        So as long as we find a visited 1, same island

        """

        visited = set()
        islands = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(i, j):
            for dir in directions:
                new_i = i + dir[0]
                new_j = j + dir[1]
                if new_i >= 0 and new_i < ROWS and new_j >= 0 and new_j < COLS:
                    if grid[new_i][new_j] == "1" and (new_i, new_j) not in visited:
                        visited.add((new_i, new_j))
                        dfs(new_i, new_j)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    visited.add((r,c))
                    dfs(r, c)
                    islands += 1
        
        return islands


