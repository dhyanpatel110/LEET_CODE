'''
Example 1:

Input: s = "babad"
Output: "bab" = 3
Note: "aba" is also a valid answer
  
Example 2:

Input: s = "baddad"
Output: "adda" = 4
'''

#CODE:
  class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        
        for i in range (len(s)):
            #odd length
            l = i
            r = i
            
            while l>=0 and r<len(s) and s[l] == s[r]:
                if(r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                
                l -= 1
                r += 1
                
            #even length
            l = i
            r = i+1
            
            while l>=0 and r<len(s) and s[l] == s[r]:
                if(r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                
                l -= 1
                r += 1
        return res
 



