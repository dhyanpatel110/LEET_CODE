'''
Example 1:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Example 2:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
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
      
      
      
