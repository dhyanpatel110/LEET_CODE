'''
Example 1:
Input: n = 10, pick = 6
Output: 6

Example 2:
Input: n = 1, pick = 1
Output: 1

Example 3:
Input: n = 2, pick = 1
Output: 1
'''

#CODE:
  class Solution(object):
    def guessNumber(self, n):
        left, right = 1, n
        
        while True:
            m = (left + right) // 2
            res = guess(m)
            if res > 0:
                left = m + 1
            elif res < 0:
                right = m - 1
            else:
                return m
              
              
        
