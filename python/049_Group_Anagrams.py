'''
Example 1:
  Input: strs = ["eat","tea","tan","ate","nat","bat"]
  Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    
Example 2:
  Input: strs = [""]
  Output: [[""]]
    
Example 3:
  Input: strs = ["a"]
  Output: [["a"]]
    
Explanation(Hint):
  ["eat","tea","tan","ate","nat","bat"] => sorted => [aet, aet, ant, aet, ant, abt]
  
  map:
    aet => eat, tea, ate
    ant => tan, nat
    abt => bat
'''

#CODE:
  class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            d["".join(sorted(s))].append(s)
        return d.values()
        
        
        
        
        
