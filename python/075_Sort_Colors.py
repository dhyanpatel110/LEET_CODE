'''
Example 1:
  Input: nums = [2,0,2,1,1,0]
  Output: [0,0,1,1,2,2]
    
Example 2:
  Input: nums = [2,0,1]
  Output: [0,1,2]
    
Example 3:
  Input: nums = [0]
  Output: [0]
    
Example 4:
  Input: nums = [1]
  Output: [1]
'''

#CODE:
  #METHOD(1):
    class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for i in range(l):
            for j in range(l-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                        
  #METHOD(2):
    class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #quick shot
        l, r = 0, len(nums)-1
        i = 0
        
        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1
            
        #bubble shot
        l = len(nums)
        for i in range(l):
            for j in range(l-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                        
                      
                      
                      
                      
                      
  
