'''
Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
'''

CODE:
  class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
            l = 0
            total = 0
            res = float("inf")
            
            for r in range(len(nums)):
                total += nums[r]
                while total >= target:
                    res = min(r-l+1, res)
                    total -= nums[l]
                    l += 1
            return 0 if res == float("inf") else res
                    
            
            
