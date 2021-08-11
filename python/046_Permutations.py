'''
Example 1:
  Input: nums = [1,2,3]
  Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    
Example 2:
  Input: nums = [0,1]
  Output: [[0,1],[1,0]]
    
Example 3:
  Input: nums = [1]
  Output: [[1]]
'''

#CODE:
  #METHOD(1):
    import itertools
    class Solution:
      def permute(self, nums: List[int]) -> List[List[int]]:
          return itertools.permutations(nums)
       
  #METHOD(2):
    class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        if len(nums) == 1:
            return[nums[:]]
        
        for i in range(len(nums)):
            #[1,2,3] => [2,3] 1 will pop 
            n = nums.pop(0)
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
            
        return result
        
