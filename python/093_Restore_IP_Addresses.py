'''
Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
'''

#CODE:
  class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 256 choice for each of the 4 spots but...
        # the order of s stays same
        # we just place the "." between
        
        res = []
        
        if len(s) > 12:
            return res
        
        def backtrack(i, dots, curIP):
            if dots == 4 and i == len(s):  
                res.append(curIP[:-1]) #remove last char "."
                return
            
            if dots  >4:
                return
            
            for j in range(i, min(i+3, len(s))):
                if int(s[i:j+1]) < 256 and (i == j or s[i] != "0"):
                    backtrack(j+1, dots+1, curIP + s[i:j+1] + ".")
        backtrack(0,0,"")
        return res
        
        
        
        
        
       
