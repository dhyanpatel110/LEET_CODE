'''
Example 1:
Input: nums = [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence with differences (6, -3, 5, -7, 3).

Example 2:
Input: nums = [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length.
One is [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).

Example 3:
Input: nums = [1,2,3,4,5,6,7,8,9]
Output: 2
'''

#CODE:
  class Solution(object):
    def wiggleMaxLength(self, nums):
        dp = [nums[i-1] - nums[i] for i in range(1, len(nums)) if nums[i-1] - nums[i] != 0]
        if not dp:
            return 1
        
        cur = 2
        
        for i in range(1,len(dp)):
            if dp[i-1] > 0 and dp[i] < 0 or dp[i-1] < 0 and dp[i] > 0:
                cur += 1
        
        return cur
        
        
        
