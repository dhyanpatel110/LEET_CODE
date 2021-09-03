'''
Example 1:
  Input: n = 4
  Output: 2
  Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
  
Example 2:
  Input: n = 1
  Output: 1
'''

#CODE:
  class Solution:
    def totalNQueens(self, n: int) -> int:
        def backTrack(i):
            nonlocal ans
            if i == n:
                ans += 1
                return
            
            for j in range(n):
                if not cols[j] and not diagonals[i+j] and not antiDiagonals[i-j]:
                    cols[j] = True
                    diagonals[i+j] = True
                    antiDiagonals[i-j] = True
                    
                    backTrack(i+1)
                    
                    cols[j] = False
                    diagonals[i+j] = False
                    antiDiagonals[i-j] = False
                    
        cols = [False] * n   
        diagonals = defaultdict(bool)
        antiDiagonals = defaultdict(bool)
        ans = 0
        
        backTrack(0)
        return ans
                    
                   
          
          
          
