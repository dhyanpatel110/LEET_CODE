'''
Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
Input: triangle = [[-10]]
Output: -10
'''

#CODE:
  class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [0] * (len(triangle) + 1)
        
        for row in triangle[:: -1]:
            for i, n in enumerate(row):
                dp[i] = n +min(dp[i], dp[i + 1])
        
        return dp[0]
        
        
        
