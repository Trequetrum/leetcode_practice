from typing import List

# Given an m x n matrix, return all elements of the matrix in spiral order.
#         GRID                    SPIRAL
#     | 1  2  3  4  5  |    | -> -> -> -> v  |
#     | 6  7  8  9  10 |    | -> -> -> v  v  |
#     | 11 12 13 14 15 |    | ^  -> v  v  v  |
#     | 16 17 18 19 20 |    | ^  ^  x  v  v  |
#     | 21 22 23 24 25 |    | ^  ^  <- <- v  |
#     | 26 27 28 29 30 |    | ^  <- <- <- <- |
#
# Order:    1,2,3,4,5,10,15,20,25,30,29,28,27,26,21,
#           16,11,6,7,8,9,14,19,24,23,22,17,12,13,18
#
# Constraints:
#   - m == matrix.length
#   - n == matrix[i].length
#   - 1 <= m, n <= 10
#   - -100 <= matrix[i][j] <= 100


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res_length = m * n
        
        # STATES:
        #   0: Going Right
        #   1: Going Down
        #   2: Going Left
        #   3: Going Up
        state = 0

        row_start = 0
        row_end = n - 1
        # col_start = 1 here because state starts with 0
        col_start = 1 
        col_end = m - 1

        res = []

        i = 0
        j = 0
        while len(res) < res_length:
            #print(f"i:{i} j:{j}")
            res.append(matrix[i][j])
            if state == 0:
                if j < row_end:
                    j += 1
                else:
                    state = 1
                    row_end -= 1
                    i += 1
            elif state == 1:
                if i < col_end:
                    i += 1
                else:
                    state = 2
                    col_end -= 1
                    j -= 1
            elif state == 2:
                if j > row_start:
                    j -= 1
                else:
                    state = 3
                    row_start += 1
                    i -= 1
            elif state == 3:
                if i > col_start:
                    i -= 1
                else:
                    state = 0
                    col_start += 1
                    j += 1
        
        return res

get = Solution()
print(get.spiralOrder(
    [   [1 ,2 ,3 ,4 ,20],
        [5 ,6 ,7 ,8 ,21],
        [9 ,10,11,12,22],
        [13,14,15,16,23],
        [24,25,26,27,28],
        [29,30,31,32,33]
    ]))