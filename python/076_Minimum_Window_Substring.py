'''
Example 1:
  Input: s = "ADOBECODEBANC", t = "ABC"
  Output: "BANC"
  Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
    
Example 2:
  Input: s = "a", t = "a"
  Output: "a"
  Explanation: The entire string s is the minimum window.
    
Example 3:
  Input: s = "a", t = "aa"
  Output: ""
  Explanation: Both 'a's from t must be included in the window.
  Since the largest window of s only has one 'a', return empty string.
'''

CODE:
  class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lookup = Counter(t)
        mx = float("inf")
        output = ""
        S = len(s)
        start, end = 0, 0
        count = len(lookup)
        #ADOBECODEBANC
        
        while end < S:
            #end pointer
            while end < S and count != 0:
                if s[end] in lookup:
                    lookup[s[end]] -= 1
                    if lookup[s[end]] == 0:
                        count -= 1
                end += 1
            
            #start pointer
            while start < end and count == 0:
                if end - start < mx:
                    mx = end - start
                    output = s[start:end]
                if s[start] in lookup:
                    lookup[s[start]] += 1
                    if lookup[s[start]] > 0:
                        count += 1
                start += 1
        return output
      
      
      
      
      
