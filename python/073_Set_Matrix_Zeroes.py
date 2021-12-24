'''
Example 1:
  Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
  Output: [[1,0,1],[0,0,0],[1,0,1]]
  
Example 2:
  Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
  Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
'''

#CODE:
  class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_size = len(matrix[0])
        col_size = len(matrix)
        rows_to_zero = set()
        cols_to_zero = set()
        for i in range(col_size):
            for j in range(row_size):
                if matrix[i][j] == 0:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)
        for i in range(col_size):
            if i in rows_to_zero:
                matrix[i] = [0] * row_size
            for j in cols_to_zero:
                matrix[i][j] = 0
                
                
                
                
                
