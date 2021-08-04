from typing import List

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
                #Mid-Right
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