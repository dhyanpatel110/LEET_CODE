'''
Example 1:
  Input: nums = [1,2,3]
  Output: [1,3,2]
    
Example 2:
  Input: nums = [3,2,1]
  Output: [1,2,3]
    
Example 3:
  Input: nums = [1,1,5]
  Output: [1,5,1]
'''

CODE:
  class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        length = len(nums)
        if length <= 2:
            return nums.reverse()
        
        pointer = length - 2
        
        while pointer >= 0 and nums[pointer] >= nums[pointer + 1]:
            pointer -= 1
        
        if pointer == -1:
            return nums.reverse()
        
        for x in range(length - 1, pointer ,-1):
            if nums[pointer] < nums[x]:
                nums[pointer],nums[x] = nums[x],nums[pointer]
                break
                    
        nums[pointer + 1 : ] = reversed(nums[pointer + 1:])
        
        
        
        
        
