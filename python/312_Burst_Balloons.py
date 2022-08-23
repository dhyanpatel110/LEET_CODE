'''
Example 1:
Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

Example 2:
Input: nums = [1,5]
Output: 10
'''

#CODE:
  class Solution(object):
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        dp ={}
        
        def dfs(l, r):
            if l > r:
                return 0
            if(l, r) in dp:
                return dp[(l, r)]
            
            if len(nums) > 1 and len(set(nums)) == 1:
                return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]
        
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]
    
        return dfs(1, len(nums) - 2)

    
    
