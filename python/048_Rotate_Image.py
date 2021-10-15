'''
Example 1:
  Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
  Output: [[7,4,1],[8,5,2],[9,6,3]]
  
Example 2:
  Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
  Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
  
Example 3:
  Input: matrix = [[1]]
  Output: [[1]]
  
Example 4:
  Input: matrix = [[1,2],[3,4]]
  Output: [[3,1],[4,2]]
'''

#CODE:
  class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        
        #transpos the matrix A^T
        for row in range(N):
            for col in range(row):
                matrix[row][col],matrix[col][row] = matrix[col][row],matrix[row][col]
                
        #reverse the matrix        
        for row in matrix:
            row.reverse()
                
 


