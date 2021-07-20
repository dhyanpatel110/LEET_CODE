'''
Example 1:
  Input: n = 1
  Output: ["()"]
    
Example 2:
  Input: n = 2
  Output: ["()()","(())"]
    
Example 3:
  Input: n = 3
  Output: ["((()))","(()())","(())()","()(())","()()()"]
'''
CODE:
  class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
      
        result = []
        stack = []

        def backtracking(openN,closeN):
            if openN == closeN == n:
                result.append("".join(stack))
                return 
            
            if openN < n:
                stack.append("(")
                backtracking(openN+1, closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(")")
                backtracking(openN, closeN+1)
                stack.pop()
                
        backtracking(0, 0)
        return result
      
      
      
      
      
  
