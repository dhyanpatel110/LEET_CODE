'''
Example 1:
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:
Input: n = 0
Output: 0
'''

CODE:
  class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n != 0:
            n = n//5
            res += n
        return res
    
            
        
