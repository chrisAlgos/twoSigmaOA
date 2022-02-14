'''
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state
'''
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        temp = [[board[row][col] for col in range(len(board[0]))] for row in range(len(board))]

        def transform(r, c): 
            nonlocal board
            offsets = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
            liveCount = 0 
            
            for offset in offsets: 
                dr, dc = r+offset[0], c+offset[1]
                if dr<0 or dc<0 or dr>=len(board) or dc>=len(board[0]): continue 
                if temp[dr][dc] == 1: 
                    liveCount+=1 
                    
            if temp[r][c] == 1 and liveCount<2: 
                board[r][c] = 0  
            elif temp[r][c] == 0 and (liveCount == 3): 
                board[r][c] = 1  
            elif  temp[r][c] == 1 and (liveCount>3): 
                board[r][c] = 0
                
        for row in range(len(board)): 
            for col in range(len(board[0])): 
                transform(row, col)
