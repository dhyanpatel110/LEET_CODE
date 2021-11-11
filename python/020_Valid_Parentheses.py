"""
Example 1:
  Input: s = "()[]{}"
  Output: true
    
Example 2:
  Input: s = "(]"
  Output: false
    
Example 3:
  Input: s = "{[]}"
  Output: true
"""
    
#CODE:
  class Solution:
    def isValid(self, s: str) -> bool:
        replace = True
        while replace:
            start_length = len(s)
            for inner in ["{}","()","[]"]:
                s = s.replace(inner,"")
            if start_length == len(s):
                replace = False
        return s ==""
      
      
      
      
      
