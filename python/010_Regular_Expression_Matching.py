'''
Example 1:
  Input: s = "aa", p = "a"
  Output: false
  Explanation: "a" does not match the entire string "aa".
Example 2:
  Input: s = "aa", p = "a*"
  Output: true
  Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:
  Input: s = "ab", p = ".*"
  Output: true
  Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:
  Input: s = "aab", p = "c*a*b"
  Output: true
  Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:
  Input: s = "mississippi", p = "mis*is*p*."
  Output: false
 '''

#CODE:
  class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dfs (i, j):
            if i >= len(s) and j >=len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j+1) < len(p) and p[j+1] == "*":
                return (dfs(i,j+2)) or (match and dfs(i+1, j))
            if match:
               return dfs(i+1,j+1)
            return False
        return dfs(0,0)
        
        
        
        
        
