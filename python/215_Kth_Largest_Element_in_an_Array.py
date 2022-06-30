'''
Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''

#CODE:
  #METHOD (1):
    class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]
      
  #METHOD (2)(quick sort):
    class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        
        def quicksort(l, r):
            pivot = nums[r]
            p = l
            
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p] = nums[i]
                    nums[i] = nums[p]
                    p += 1
            nums[p] = nums[r]
            nums[r] = nums[p]
            
            if p > k:   return quicksort(l, p-1)
            elif p < k: return quicksort(p+1, r)
            else: return nums[p]
            
        return quicksort(0, len(nums) - 1)
        
        
  
