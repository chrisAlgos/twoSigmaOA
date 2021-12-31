class Solution:
    '''
    idea: 
    (MAIN) nested for loop through grid: 
           - encounter a "1" (a new island) in the grid, increment count and set off dfs passing current row and col indices
           - every time you enter a dfs, set the grid that is "1" to "0"
           - each dfs(i, j) from the main nested for loop through grid will result in entire island being transformed to "0"s
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c): 
            grid[r][c] = "0" #set current cell to 0  
            direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for i in range(len(direct)): 
                dr, dc = r + direct[i][0], c + direct[i][1] #calculate new coordinates 
                if dr < 0 or dc < 0 or dr >= len(grid) or dc >= len(grid[0]): continue #if out-of-bounds, continue
                if grid[dr][dc] == '0': continue #if not "land", continue
                dfs(dr, dc) #set off dfs on the new coordinates 

        count = 0 
        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                if grid[i][j] == "1": 
                    count += 1
                    dfs(i, j) #set off dfs 
        return count
