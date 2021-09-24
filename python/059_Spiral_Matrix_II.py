'''
Example 1:
  Input: n = 3
  Output: [[1,2,3],[8,9,4],[7,6,5]]
  
Example 2:
  Input: n = 1
  Output: [[1]]
'''

#CODE:
  class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for i in range(n)] for j in range(n)]
        left = 0; right = n-1;
        top = 0; down = n-1;
        
        val = 1
        while top <= down and left <= right:
            for i in range(left, right+1):
                ans[top][i] = val
                val += 1
            
            for i in range(top+1, down+1):
                ans[i][right] = val
                val += 1
                
            for i in reversed(range(left, right)):
                if top == down:
                    break
                ans[down][i] = val
                val += 1
            
            for i in reversed(range(top+1, down)):
                if left == right:
                    break
                ans[i][left] = val
                val += 1
            
            top += 1 
            down -= 1
            left += 1 
            right -= 1
            
        return ans
      
      
      
      
      
