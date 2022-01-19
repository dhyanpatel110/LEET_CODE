Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
  
#CODE:
  class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}
        def dfs(i):
            if i in dp:
                return dp[i]
            
            if s[i] == "0":
                return 0
            
            res = dfs(i+1)
            if (i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                res += dfs(i+2)
            dp[i] = res
            return res
        return dfs(0)
                
   
  
  
  
