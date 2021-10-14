'''
Example 1:
  Input: path = "/home/"
  Output: "/home"
  Explanation: Note that there is no trailing slash after the last directory name.
  
Example 2:
  Input: path = "/../"
  Output: "/"
  Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
  
Example 3:
  Input: path = "/home//foo/"
  Output: "/home/foo"
  Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
  
Example 4:
  Input: path = "/a/./b/../../c/"
  Output: "/c"
'''

#CODE:
  class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""
        for c in path + "/":
                if c == "/":
                    if cur == "..":
                        if stack: stack.pop()
                    elif cur != "" and cur != '.':
                        stack.append(cur)
                    cur = ""
                
                else:
                    cur += c
                    
        return "/" + "/".join (stack)
      
      
      
      
      
