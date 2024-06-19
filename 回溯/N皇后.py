from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.dfs(n,0,['.'*n]*n,res)
       
        return res

    def dfs(self, n: int, row: int, board: List[str], res: List[List[str]]):
        if row == n:
            res.append(board.copy())
            return
        for col in range(n):
            if self.isValid(row,col,board,n):
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                self.dfs(n,row+1,board,res)
                board[row] = board[row][:col] + '.' + board[row][col+1:]

    def isValid(self, row: int, col: int, board: List[str], n: int) -> bool:
        for i in range(row):
            if board[i][col] == 'Q':
                return False
            
        for (i,j) in zip(range(row-1,-1,-1),range(col-1,-1,-1)):
            if board[i][j] == 'Q':
                return False
            
        for (i,j) in zip(range(row-1,-1,-1),range(col+1,n)):
            if board[i][j] == 'Q':
                return False
        return True
        
