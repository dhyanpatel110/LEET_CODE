'''
Example 1:
Input: num = 16
Output: true

Example 2:
Input: num = 14
Output: false
'''

#CODE:
  #METHOD(1):
    class Solution:
      def isPerfectSquare(self, num: int) -> bool:
          # o(sqrt(n))
          for i in range(1, num + 1):
              if i * i == num:
                  return True
              if i * i > num:
                  return False
  #METHOD(2):
    class Solution:
      def isPerfectSquare(self, num: int) -> bool:
          # o(logn)
          left, right = 1, num
          while left <= right:
              mid = (left + right) // 2
              if mid * mid > num:
                  right = mid - 1
              elif mid * mid < num:
                  left = mid + 1
              else:
                  return True
          return False
        
        
        
