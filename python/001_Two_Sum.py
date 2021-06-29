# EXAMPLE:
  Input: nums = [2,7,11,15], target = 9
  Output: [0,1]
  Output: Because nums[0] + nums[1] == 9, we return [0, 1].
  
# CODE:
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return[i , j]
                  
                  
                  
                  
                  
