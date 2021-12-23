'''
Example 1:
  Input: nums = [1,2,0]
  Output: 3
    
Example 2:
  Input: nums = [3,4,-1,1]
  Output: 2
    
Example 3:
  Input: nums = [7,8,9,11,12]
  Output: 1
'''

#CODE:
  METHOD(1):
  class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set()
        output = 1
        
        for n in nums:
            seen.add(n)
            while output in seen:
                output += 1
        return output
      
     
  METHOD(2):
    class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ls = len(nums)
        index = 0
        while index < ls:
            # nums[nums[index] - 1] == nums[index] means that the num is in right position
            if nums[index] <= 0 or nums[index] > ls or nums[nums[index] - 1] == nums[index]:
                index += 1
            else:
                # swap current num to correct position
                pos = nums[index] - 1
                nums[index], nums[pos] = nums[pos], nums[index]
        res = 0
        while res < ls and nums[res] == res + 1:
            res += 1
        return res + 1
  
  
  
  
        
