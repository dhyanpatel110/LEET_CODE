'''
Example 1:
  Input: dividend = 10, divisor = 3
  Output: 3
  Explanation: 10/3 = truncate(3.33333..) = 3.
    
Example 2:
  Input: dividend = 7, divisor = -3
  Output: -2
  Explanation: 7/-3 = truncate(-2.33333..) = -2.
    
Example 3:
  Input: dividend = 0, divisor = 1
  Output: 0
    
Example 4:
  Input: dividend = 1, divisor = 1
  Output: 1
'''

CODE:
  class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        min_number = -2**31
        max_number = 2**31 - 1
        result = abs(dividend) // abs(divisor)
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            return min(result, max_number)
        else:
            return max(-result, min_number)
          
          
          
          
          
