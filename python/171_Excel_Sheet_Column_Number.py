'''
Example 1:
Input: columnTitle = "A"
Output: 1

Example 2
Input: columnTitle = "AB"
Output: 28

Example 3:
Input: columnTitle = "ZY"
Output: 701
'''

CODE:
  class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for char in columnTitle:
            x = ord(char) - ord('A') + 1
            res = res * 26 + x
        return res
        
        
        
        
