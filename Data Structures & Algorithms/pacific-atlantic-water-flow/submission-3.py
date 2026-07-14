class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Return list of cells which are connected to either top/left or right/bottom
        once we know an element can reach an ocean, 
            any cell reaching it-also reaches that ocean - DFS
            So for any (i,j) if (i+-1, j+-1) can reach, then (i,j) can reach
            2 funcs- can reach pacific, can reach atlantic
                if it is on the border, yes to that ocean
                if any neighbor is <=, then call on that
        """
        ROWS = len(heights)
        COLS = len(heights[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        atl = set()
        pac = set()
        ans = []

        def reach_ocean(i,j, visited):
            #work from the borders
            #for each cells on border- call dfs to see all elems touching it and greater than it
            visited.add((i,j))
            for d in dirs:
                new_i = i + d[0]
                new_j = j + d[1]

                if 0<= new_i < ROWS and 0 <= new_j < COLS and heights[new_i][new_j] >= heights[i][j] and (new_i,new_j) not in visited:
                    reach_ocean(new_i, new_j, visited)
        
        for r in range(ROWS):
            reach_ocean(r, 0, pac)
            reach_ocean(r, COLS-1, atl)
        
        for c in range(COLS):
            reach_ocean(0, c, pac)
            reach_ocean(ROWS-1, c, atl)
        
        # print(atl, pac)
        for r in range(ROWS):
            for c in range(COLS):
                # print(r,c, heights[r][c], can_reach_atlantic(r,c), can_reach_pacific(r,c))
                if (r,c) in atl and (r,c) in pac:
                    ans.append([r,c])
        
        return ans
        


        # def can_reach_pacific(i,j):
        #     if i == 0 or j == 0:
        #         pac[i][j] = True
        #         return True
            
        #     can = False
        #     for d in [(0,-1), (-1, 0)]:
        #         new_i = i + d[0]
        #         new_j = j + d[1]
        #         if 0 <= new_i < ROWS and 0 <= new_j < COLS:
        #             if heights[new_i][new_j] <= heights[i][j]:
        #                 can = can_reach_pacific(new_i, new_j)
        #                 if can:
        #                     return True
        #     return False
        
        # def can_reach_atlantic(i,j):
        #     if i == ROWS-1 or j == COLS-1:
        #         return True
            
        #     can = False
        #     for d in [(0,1), (1,0)]:
        #         new_i = i + d[0]
        #         new_j = j + d[1]
        #         if 0 <= new_i < ROWS and 0 <= new_j < COLS:
        #             if heights[new_i][new_j] <= heights[i][j]:
        #                 can = can_reach_atlantic(new_i, new_j)
        #                 if can:
        #                     return True
        #     return False
        
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         # print(r,c, heights[r][c], can_reach_atlantic(r,c), can_reach_pacific(r,c))
        #         if can_reach_pacific(r,c) and can_reach_atlantic(r,c):
        #             ans.append([r,c])
        # print(ans)
        # return ans

            

            