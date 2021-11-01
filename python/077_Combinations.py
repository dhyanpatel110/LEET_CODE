'''
Example 1:
  Input: n = 4, k = 2
  Output:
  [
    [2,4],
    [3,4],
    [2,3],
    [1,2],
    [1,3],
    [1,4],
  ]
  
Example 2:
  Input: n = 1, k = 1
  Output: [[1]]
'''

CODE:
  class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #method-1
        res = []
        
        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            
            for i in range(start, n+1):
                comb.append(i)
                backtrack(i+1, comb)
                comb.pop()
        backtrack(1, [])
        
        return res
        
        #method-2
        bfs = [[]]
        for num in range(1, n + 1):
            bfs += [arr + [num] for arr in bfs if len(arr) < k]
        return [arr for arr in bfs if len(arr) == k]
    
    
    
    
    
    
