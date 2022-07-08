'''
Example 1:

Input: s = "1 + 1"
Output: 2

Example 2:
Input: s = " 2-1 + 2 "
Output: 3

Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
'''


#CODE:
  class Solution:
    def calculate(self, s: str) -> int:
        cur = res = 0
        
        sign = 1
        stack = []
        
        for char in s:
            if char.isdigit():
                cur = cur*10 + int(char)
            elif char in ['+', '-']:
                res += sign * cur
                sign = 1 if char == '+' else '-'
                cur = 0
                
            elif char == "(":
                stack = append(res)
                stack.append(sign)
                sign = 1
                res = 0
                
            elif char == ")":

                res += sign * cur
            
                res *= stack.pop()
            
                res += stack.pop()
                
                cur = 0
        return res + sign * cur
    
    
    
