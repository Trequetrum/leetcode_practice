from typing import List


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