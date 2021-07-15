Example 1:
  Input: nums = [-1,2,1,-4], target = 1
  Output: 2
  Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

CODE:
  class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = sum(nums[:3])
        
        for i in range(len(nums)):
            start = i+1
            end = len(nums)-1
            
            while start < end:
                sumhere = nums[i] + nums[start] + nums[end]
                if abs(sumhere-target) < abs(result-target):
                    result = sumhere
                if sumhere < target:
                    start += 1
                else:
                    end -= 1
        return result
                
        
        
        
        
