'''
Example 1:
  Input: s = "Hello World"
  Output: 5
  Explanation: The last word is "World" with length 5.
  
Example 2:
  Input: s = "   fly me   to   the moon  "
  Output: 4
  Explanation: The last word is "moon" with length 4.
  
Example 3:
  Input: s = "luffy is still joyboy"
  Output: 6
  Explanation: The last word is "joyboy" with length 6.
'''

#CODE:
  class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # method 1: string split version
        if s.split():
            return len(s.split()[-1])
        return 0
       
        # method 2:manual string length count
        count = 0
        for letter in s[::-1]:
            if letter == " ":
                if count >= 1:
                    return count
            else:
                count += 1
        return count
                    
        
        
        
        
