'''
Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
'''

CODE:
  class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 # n ^ 0 = n
        for n in nums:
            res = n^res
        return res
        
        
        
        
