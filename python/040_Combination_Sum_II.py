'''
Example 1:
  Input: candidates = [10,1,2,7,6,1,5], target = 8
  Output: 
  [
  [1,1,6],
  [1,2,5],
  [1,7],
  [2,6]
  ]
  
Example 2:
  Input: candidates = [2,5,2,1,2], target = 5
  Output: 
  [
  [1,2,2],
  [5]
  ]
'''

CODE:
  class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def recursive(candidates, target, currList, index):
        	if target < 0:
        		return
        	if target == 0:
        		result.append(currList)
        		return

        	previous = -1
        	for start in range(index, len(candidates)):
        		if previous != candidates[start]:
	        		recursive(candidates, target - candidates[start], currList + [candidates[start]], start+1)
	        		previous = candidates[start]


        recursive(candidates, target, [], 0)
        return result
      
      
      
      
      
