'''
Example 1:
  Input: nums = [1,2,3]
  Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    
Example 2:
  Input: nums = [0]
  Output: [[],[0]]
'''

CODE:
  class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #method-1
        res = []
        
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            #decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)
            
            #decision not to include nums[i]
            subset.pop()
            dfs(i+1)
            
        dfs(0)
        return res
    
        #method-2
        result = [[]]
        for num in nums:
        	for j in range(len(result)):
        		result.append(result[j] + [num])
        return result
