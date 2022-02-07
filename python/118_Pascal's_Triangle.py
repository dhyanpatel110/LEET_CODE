'''
Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
'''

#CODE:
  class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j+1])
            res.append(row)
        return res
        
        
        
        
        
        
