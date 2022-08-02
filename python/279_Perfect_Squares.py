'''
Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9
'''

#CODE:
  class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1);
        dp[0] = 0
        
        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1+ dp[target - square])
        return dp[n]
    
    
               
