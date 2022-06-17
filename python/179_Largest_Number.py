'''
Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"

'''

#CODE:
  class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)
            
        def compare(n1, n2):
            if n1+n2 > n2+n1:
                return -1
            else:
                return 1
            
        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int("" .join(nums)))
                
        
        
