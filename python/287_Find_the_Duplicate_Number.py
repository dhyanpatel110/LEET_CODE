'''
Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3
'''

#CODE:
  class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        
        while True:
        	slow = nums[slow]
        	fast = nums[nums[fast]]
        	if slow == fast:
        		break

        num1= nums[0]
        num2 = slow
        while num1 != num2:
        	num1 = nums[num1]
        	num2 = nums[num2]
        return num2
      
      
      
