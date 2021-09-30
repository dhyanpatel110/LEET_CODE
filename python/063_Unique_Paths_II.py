'''
Example 1:
  Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
  Output: 2
   Explanation: There is one obstacle in the middle of the 3x3 grid above.
   There are two ways to reach the bottom-right corner:
   1. Right -> Right -> Down -> Down
   2. Down -> Down -> Right -> Right
   
Example 2:
  Input: obstacleGrid = [[0,1],[0,0]]
  Output: 1
 '''

#CODE:
  class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        N, M = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [[0 for _ in range(N)] for _ in range(M)]
        
        #first row
        for c in range(N):
            if obstacleGrid[0][c] == 1: break
            dp[0][c] = 1
                
        #first column
        for r in range(M):
            if obstacleGrid[r][0] == 1: break
            dp[r][0] = 1
        
        for r in range(1, M):
            for c in range(1, N):
                if obstacleGrid[r][c] == 1: continue
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[-1][-1]
      
      
      
      
      
