'''
Example 1:
  Input: nums = [4,5,6,7,0,1,2], target = 0
  Output: 4
    
Example 2:
  Input: nums = [4,5,6,7,0,1,2], target = 3
  Output: -1
  
Explanation:
  target = 4
  [0,1,2,4,5,6,7]  target=mid
   |    |      |
   l    m      r

  target = 1
  [4,5,6,7,0,1,2] our target value is right side
   |     |     |
   l     m     r

  [4,5,6,7,0,1,2] 
           | | |       
           l m r
'''

CODE:
  class Solution:
    def search(self, nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid

                if nums[left] <= nums[mid]:
                    if nums[left]<= target <= nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    if nums[mid] <= target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1

            return -1

        
        
        
        
