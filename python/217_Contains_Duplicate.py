'''
Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Time complexity O(n2) O(nlogn)  O(n)
Space complexity O(1) O(n)
'''

#CODE:
  #METHOD(1):
  #Time complexity: O(n2)
  #Space complexity: O(1)
  class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

  #METHOD(2):
  #Time complexity: O(nlogn)
  #Space complexity: O(n)
  class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
          hashset  = set()
         	for n in nums:
             		if n in hashset:
                 		return True
            		hashset.add(n)        
          return False

  #METHOD(3):
  class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
          dic=dict()
         	for num in nums:
             		if not num in dic:
                 		dic[num]=1
             		else:
                 		return True
         	return False

        
        
