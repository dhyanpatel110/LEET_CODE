'''
Example 1:
Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.

Example 2:
Input: nums = [9], target = 3
Output: 0

'''

#CODE:
  class Solution(object):
    def combinationSum4(self, nums, target):
        dp = {0 : 1}
        
        for total in range (1, target+1):
            dp[total] = 0
            for n in nums:
                dp[total] += dp.get(total-n , 0)
                
        return dp[target]
      
      
      
