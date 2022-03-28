'''
Example 1:
Input: nums = [2,2,3,2]
Output: 3

Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99
'''

#CODE:
  class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return ((sum(set(nums)) * 3) - sum(nums)) // 2
