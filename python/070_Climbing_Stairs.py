'''
Example 1:
  Input: n = 2
  Output: 2
  Explanation: There are two ways to climb to the top.
  1. 1 step + 1 step
  2. 2 steps
  
Example 2:
  Input: n = 3
  Output: 3
  Explanation: There are three ways to climb to the top.
  1. 1 step + 1 step + 1 step
  2. 1 step + 2 steps
  3. 2 steps + 1 step
'''

#CODE:
  class Solution:
    def climbStairs(self, n: int) -> int:
        
        # dictionary method
        path = { 1:1, 2:2, 3:3}
        
        for x in range(4, n+1):
            path[x] = path[x-1] + path[x-2]
        
        return (path[n])
    
        #  dfs method 
        memo = {}
        def dfs(i):
            if i >= n: return 1 if i == n else 0
            if i not in memo:
                memo[i] = dfs(i + 1) + dfs(i + 2)
            return memo[i]
        return dfs(0)
      
      
      
      
      
