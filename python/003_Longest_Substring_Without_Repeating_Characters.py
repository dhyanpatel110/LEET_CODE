EXAMPLE 1:
  Input: s = "abcabcbb"
  Output: 3
  Explanation: The answer is "abc", with the length of 3.

EXAMPLE 2:
   Input: s = [1,2,3,4,5] median(middle) => 3

EXAMPLE 3:
    Input: s = [1,2,4,7] // median(middle) => 2+4/2 =3

CODE:
  class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        result = 0
        
        for r in range (len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            result = max(result , r-l+1)
        return result

      
      
      
      
