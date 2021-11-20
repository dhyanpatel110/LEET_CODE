'''
Example 1:
  Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
  Output: true
  
Example 2:
  Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
  Output: false
'''

#CODE:
  class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
        	return 0
        left, right = 0, len(matrix[0])-1

        while left < len(matrix) and right >= 0:
        	if matrix[left][right] == target:
        		return True 
        	elif matrix[left][right] < target:
        		left += 1
        	else:
        		right -= 1
        return False
      
      
      
      
      
