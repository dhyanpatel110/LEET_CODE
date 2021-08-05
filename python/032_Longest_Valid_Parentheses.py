'''
Example 1:
  Input: s = "(()"
  Output: 2
  Explanation: The longest valid parentheses substring is "()".
    
Example 2:
  Input: s = ")()())"
  Output: 4
  Explanation: The longest valid parentheses substring is "()()".
    
Example 3:
  Input: s = ""
  Output: 0
'''

CODE:
  class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        result = 0
        
        for i in range (len(s)):
            if(s[i] == "(" ):
                stack.append(i)
            else:
                stack.pop()
                
                if(len(stack)) == 0:
                    stack.append(i)
                else:
                    result = max(result, (i-stack[-1]))
        return result
                    
        
        
        
        
