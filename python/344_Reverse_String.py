'''
Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''

#CODE:
  class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left , right = 0, len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left = left + 1
            right = right - 1
        
        
  
