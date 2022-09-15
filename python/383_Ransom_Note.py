'''
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
'''

#CODE:
  class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ran = sorted(list(ransomNote))
        mag = sorted(list(magazine))
        
        for char in mag:
            if ran and char == ran[0]:
                ran.pop(0)
        
        if ran:
            return False
        else:
            return True
        
        
        
