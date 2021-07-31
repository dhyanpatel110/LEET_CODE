'''
Example 1:
  Input: nums = [1,3,5,6], target = 5
  Output: 2
    
Example 2:
  Input: nums = [1,3,5,6], target = 2
  Output: 1
    
Example 3:
  Input: nums = [1,3,5,6], target = 7
  Output: 4
    
Example 4:
  Input: nums = [1,3,5,6], target = 0
  Output: 0
    
Example 5:
  Input: nums = [1], target = 0
  Output: 0
'''

CODE:
  class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if target == nums[mid]:
                return mid
            
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
                
        return left
      
      
      
      
      
