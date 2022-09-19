'''
Example 1:
Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.

Example 2:
Input: s = "", t = "y"
Output: "y"
'''

#CODE:
  class Solution(object):
    def findTheDifference(self, s, t):
        diff = 0
        for char in s:
            diff ^= ord(char)
        for char in t:
            diff ^= ord(char)
        return chr(diff)
        
        
        
