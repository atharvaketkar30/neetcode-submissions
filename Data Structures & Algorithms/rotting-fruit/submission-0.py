class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Oranges rotting based on connected nature -> DFS/BFS
            Since we convert only ones connected so 1 layer at a time- BFS
        Every iter - We start by looking for all 2 and its neighbours
        increment iter as long as no child with 1 or no new 2
        """
        rotten = collections.deque()
        mins = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh = 0 # to see if stopping condition reached

        # Traverse and first find all rotten and fresh fruits
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    rotten.append((i,j))
        print(rotten)

        while fresh > 0 and rotten:
            num_rotten = len(rotten)
            dirs = [(0,1), (0,-1), (1,0), (-1,0)] 

            for i in range(num_rotten):
                x, y = rotten.popleft() ##current rotten fruit
                for d in dirs:
                    new_x = x + d[0]
                    new_y = y + d[1]

                    if 0<= new_x < ROWS and 0<= new_y < COLS: # if valid
                        if grid[new_x][new_y] == 1:
                            grid[new_x][new_y] = 3 # temp to identify converted
                            rotten.append((new_x,new_y)) # add to rotten list
                            fresh -= 1 # remove from fresh
                            print(grid, rotten)
            
            mins += 1
            
        return -1 if fresh > 0 else mins


                