'''
Example 1:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
'''

#CODE:
  class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        res = set()
        
        for left in range(len(s) - 9):
            cur = s[left:left + 10]
            if cur in seen:
                res.add(cur)
            seen.add(cur)
        return list(res)
      
      
      
