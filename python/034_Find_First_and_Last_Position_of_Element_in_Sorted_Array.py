'''
Example 1:
  Input: nums = [5,7,7,8,8,10], target = 8
  Output: [3,4]
    
Example 2:
  Input: nums = [5,7,7,8,8,10], target = 6
  Output: [-1,-1]
    
Example 3:
  Input: nums = [], target = 0
  Output: [-1,-1]
'''

CODE:
  class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSearch(nums,target,True)
        right = self.binSearch(nums,target,False)
        return[left, right]
        
    def binSearch(self, nums,target,leftBias):
        left,right = 0, len(nums)-1
        i = -1
        while left <= right:
            middle = (left + right) // 2
            if target > nums[middle]:
                left = middle+1
                
            elif target < nums[middle]:
                right = middle-1
                
            else:
                i=middle
                if leftBias:
                    right = middle-1
                else:
                    left = middle+1
        return i
                
        
        
        
        
