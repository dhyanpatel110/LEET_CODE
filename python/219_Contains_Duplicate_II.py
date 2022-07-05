'''
Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

#CODE:
  #METHOD(1):
    class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        check = set()
        for i in range(len(nums)):
            if i > k:
                check.remove(nums[i - k - 1])
            if nums[i] in check:
                return True
            else:
                check.add(nums[i])
        return False
    
  #METHOD(2):
    class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        if len(nums) == len(set(nums)):
            return 0
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and j-i <= k and i != j:
                    return 1
        return 0
        
        
        
