'''
Example 1:
  Input: x = 121
  Output: true
    
Example 2:
  Input: x = 10
  Output: false
  Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''

#CODE:
  class Solution:
    def isPalindrome(self, x: int) -> bool:
        return (str(x) == str(x)[::-1])
