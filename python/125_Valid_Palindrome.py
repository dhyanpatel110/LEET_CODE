'''
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''

#CODE:
 #METHOD-1:
    class Solution:
      def isPalindrome(self, s: str) -> bool:
          newStr = ""
        
          for c in s:
              if c.isalnum():
                  newStr += c.lower()
          return newStr == newStr[::-1]
    
 #METHOD-2:
    class Solution:
      def isPalindrome(self, s: str) -> bool:
          l = 0
          r = len(s) - 1
        
          while l < r:
              while l < r and not self.alphaNum(s[l]):
                  l += 1
              while l < r and not self.alphaNum(s(r)):
                  r -= 1
              if s[l].lower != s[r].lower():
                  return False
            
              l = l + 1
              r = r - 1
          return True
    
      def alphaNum(self, c):
          return(ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))
                
