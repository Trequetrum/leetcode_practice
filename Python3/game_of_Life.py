from typing import List

# "The Game of Life, also known simply as Life, is a cellular automaton 
# devised by the British mathematician John Horton Conway in 1970."
#
# The board is made up of an m x n grid of cells, where each cell has an 
# initial state: live (represented by a 1) or dead (represented by a 0). 
# Each cell interacts with its eight neighbors (horizontal, vertical, 
# diagonal) using the following four rules:
#   1) Any live cell with fewer than two live neighbors 
#       dies as if caused by under-population.
#   2) Any live cell with two or three live neighbors 
#       lives on to the next generation.
#   3) Any live cell with more than three live neighbors 
#       dies, as if by over-population.
#   4) Any dead cell with exactly three live neighbors 
#       becomes a live cell, as if by reproduction.
#
# The next state is created by applying the above rules simultaneously to 
# every cell in the current state, where births and deaths occur 
# simultaneously. Given the current state of the m x n grid board, return 
# the next state.
#
# Constraints:
#   - m == board.length
#   - n == board[i].length
#   - 1 <= m, n <= 25
#   - board[i][j] is 0 or 1.
#
# Follow-ups: 
#   1) Could you solve it in-place? Remember that the board needs to 
#       be updated simultaneously: You cannot update some cells first and then 
#       use their updated values to update other cells.
#   2) In this question, we represent the board using a 2D array. In principle, 
#       the board is infinite, which would cause problems when the active area 
#       encroaches upon the border of the array (i.e., live cells reach the 
#       border). How would you address these problems?


def safe_and_alive_for(board):
    m = len(board)
    if m < 0: return lambda i, j: False
    n = len(board[0])

    return lambda i, j: i > -1 and j > -1 and i < m and j < n and (
        board[i][j] == 1 or board[i][j] == 3 )
    

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:

        # Board starts with a bunch of ints that are 0 or 1
        #
        # The algothm is this: 
        # - Turn the second bit (binary representation) of every cell that
        #   will be alive in the next generation into a 1.
        # - binary shift right (>> 1) every element in the board
        #
        # Remember
        #   0 = 0b...00
        #   1 = 0b...01
        #   2 = 0b...10
        #   3 = 0b...11

        """
        Do not return anything, modify board in-place instead.
        """
        test = safe_and_alive_for(board)

        for i, row in enumerate(board):
            for j, val in enumerate(row):
                
                count = 0
                # Top-Left
                if test(i-1, j-1):
                    count += 1
                # Top-Top
                if test(i-1, j):
                    count += 1
                # Top-Right
                if test(i-1, j+1):
                    count += 1
                # Mid-Left
                if test(i, j-1):
                    count += 1
                # Mid-Mid skipped
                # Mid-Right
                if test(i, j+1):
                    count += 1
                # Bot-Left
                if test(i+1, j-1):
                    count += 1
                # Bot-Bot
                if test(i+1, j):
                    count += 1
                # Bot-Right
                if test(i+1, j+1):
                    count += 1
                
                # print(f"i:{i} j:{j} c:{count}")
                
                # By default, cells die with `>> 1` later, 
                # so decide which cells stay alive
                if val == 1 and (count == 2 or count == 3):
                    board[i][j] = 3
                if val == 0 and count == 3:
                    board[i][j] = 2
        
        # `>> 1` the board
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                board[i][j] = board[i][j] >> 1