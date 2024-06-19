from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.dfs(board)

    def dfs(self,board:List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    continue
                for k in range(1,10):
                    if self.isValid(board,i,j,str(k)):
                        board[i][j] = str(k)
                        if self.dfs(board):
                            return True
                        board[i][j] = '.'
                return False
        return True


    def isValid(self,board:List[List[str]],row:int,col:int,val:str):
        for i in range(9):
            if board[row][i] == val:
                return False
            if board[i][col] == val:
                return False
            if board[(row//3)*3+i//3][(col//3)*3+i%3] == val:
                return False
        return True
        