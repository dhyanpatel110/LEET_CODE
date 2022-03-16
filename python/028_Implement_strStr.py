'''
Example 1:
  Input: haystack = "hello", needle = "ll"
  Output: 2

Example 2:
  Input: haystack = "aaaaa", needle = "bba"
  Output: -1
    
Example 3:
  Input: haystack = "", needle = ""
  Output: 0
'''

#CODE:
  class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        for i in range(len(haystack)):
            if haystack[i : i+len(needle)] == needle:
                return i
        return -1
      
      
      
      
      
