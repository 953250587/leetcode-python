"""
Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:

You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
Example:
X..X
...X
...X
In the above board there are 2 battleships.
Invalid Example:
...X
XXXX
...X
This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
Follow up:
Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?
"""
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        62ms
        """
        self.board=board
        self.r=len(board)
        if self.r<=0:
            return 0
        self.l=len(board[0])
        def dfs(i,j):
            while j+1<self.l and self.board[i][j+1]=='X':
                self.board[i][j+1]='.'
                j+=1
            while i+1<self.r and self.board[i+1][j]=='X':
                self.board[i+1][j]='.'
                i+=1
        count=0
        for i in range(self.r):
            for j in range(self.l):
               if self.board[i][j]=='X':
                   dfs(i,j)
                   count+=1
        print(self.board)
        return count

    def countBattleships_1(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        49ms
        """
        counter = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'X':
                    if not ((r >= 1 and board[r - 1][c] == 'X') or (c >= 1 and board[r][c - 1] == 'X')):
                        counter += 1

        return counter
board=[["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
print(Solution().countBattleships(board))
