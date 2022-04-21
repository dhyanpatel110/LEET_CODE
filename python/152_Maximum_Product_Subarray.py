'''
Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

CODE:
  class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res  = max(nums)
        curMin,curMax = 1, 1
        
        for n in nums:
            if n == 0:
                curMin,curMax = 1, 1
                continue
            tmp = curMax * n
            curMax = max(n*curMax, n*curMin, n)
            curMin = min(tmp, n*curMin, n)
            res = max(res, curMax)
        return res
              

            
