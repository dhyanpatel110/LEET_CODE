'''
Example 1:
  Input: m = 3, n = 7
  Output: 28
  
Example 2:
  Input: m = 3, n = 2
  Output: 3
  
Explanation:
  From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
  1. Right -> Down -> Down
  2. Down -> Down -> Right
  3. Down -> Right -> Down
  
Example 3:
  Input: m = 7, n = 3
  Output: 28
  
Example 4:
  Input: m = 3, n = 3
  Output: 6
'''

#CODE:
  class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        
        for i in range(m-1):
            newRow = [1] * n
            for j in range (n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]
      
      
      
      
      
