'''
Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1
'''


#CODE:
  # The isBadVersion API is already defined for you.
  # def isBadVersion(version: int) -> bool:

  class Solution:
      def firstBadVersion(self, n: int) -> int:
          left, right= 1, n
          while left < right:
              mid = (right + left) // 2
              if isBadVersion(mid):
                  right = mid
              else:
                  left = mid + 1
          return  left
        
        
        
