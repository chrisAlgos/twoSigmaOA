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
