"""
 According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state.

Follow up:

    Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
    In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

"""
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        42ms
        """
        if len(board)<=0:
            return
        row=len(board)
        column=len(board[0])
        board_copy=[[0 for i in range(column)] for j in range(row)]

        def is_alive(i,j):
            died_num=0
            alive_num=0
            if i-1>=0:
                if j-1>=0:
                    if board[i - 1][j - 1] == 0:
                        died_num += 1
                    else:
                        alive_num += 1
                if j+1<column:
                    if board[i - 1][j + 1] == 0:
                        died_num+=1
                    else:
                        alive_num+=1
                if board[i - 1][j] == 0:
                    died_num += 1
                else:
                    alive_num += 1

            if i + 1 < row:
                if j - 1 >= 0:
                    if board[i + 1][j - 1] == 0:
                        died_num += 1
                    else:
                        alive_num += 1
                if j + 1 < column:
                    if board[i + 1][j + 1] == 0:
                        died_num += 1
                    else:
                        alive_num += 1
                if board[i + 1][j] == 0:
                    died_num += 1
                else:
                    alive_num += 1

            if j - 1 >= 0:
                if board[i][j - 1] == 0:
                    died_num += 1
                else:
                    alive_num += 1
            if j + 1 < column:
                if board[i][j + 1] == 0:
                    died_num += 1
                else:
                    alive_num += 1
            return died_num,alive_num

        for i in range(row):
            for j in range(column):
                died_num, alive_num=is_alive(i,j)
                if alive_num<2 and board[i][j]==1:
                    board_copy[i][j]=0
                elif (alive_num==2 or alive_num==3) and board[i][j]==1:
                    board_copy[i][j]=1
                elif alive_num>3 and board[i][j]==1:
                    board_copy[i][j]=0
                elif alive_num==3 and board[i][j]==0:
                    board_copy[i][j]=1

        for i in range(row):
            for j in range(column):
                board[i][j]=board_copy[i][j]

import collections
class Solution_1(object):
    def gameOfLife(self, board):
        live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
        live = self.gameOfLifeInfinite(live)
        for i, row in enumerate(board):
            for j in range(len(row)):
                row[j] = int((i, j) in live)

    def gameOfLifeInfinite(self, live):
        ctr = collections.Counter((I, J) for i, j in live for I in range(i - 1, i + 2) for J in range(j - 1, j + 2) if I != i or J != j)
        return {ij
                for ij in ctr
                if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}

board=[[1,1],[1,0]]
(Solution().gameOfLife(board))
print(board)