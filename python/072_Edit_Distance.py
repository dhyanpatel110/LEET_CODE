'''
Example 1:
  Input: word1 = "horse", word2 = "ros"
  Output: 3
  Explanation: 
  horse -> rorse (replace 'h' with 'r')
  rorse -> rose (remove 'r')
  rose -> ros (remove 'e')
  
Example 2:
  Input: word1 = "intention", word2 = "execution"
  Output: 5
  Explanation: 
  intention -> inention (remove 't')
  inention -> enention (replace 'i' with 'e')
  enention -> exention (replace 'n' with 'x')
  exention -> exection (replace 'n' with 'c')
  exection -> execution (insert 'u')
'''

#CODE:
  class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[0] * (len(word2) + 1) for i in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if not (i and j):
                    cache[i][j] = i or j
                elif word1[i - 1] == word2[j - 1]:
                    cache[i][j] += cache[i - 1][j - 1]
                else:
                    cache[i][j] += min(cache[i - 1][j], cache[i][j - 1], cache[i - 1][j - 1]) + 1
        return cache[-1][-1]
        
        
        
        
        
        
