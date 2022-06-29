'''
Example 1:
Input: s = "aacecaaa"
Output: "aaacecaaa"

Example 2:
Input: s = "abcd"
Output: "dcbabcd"
'''


#CODE:
  class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        index = 1
        
        for i in range(1, n+2):
            # CHECK s[:i] IS A PALINDROME ?
            if s[:i][::-1] == s[:i]:
                index = i
               
        return s[index:][::-1] + s
        
        
        
