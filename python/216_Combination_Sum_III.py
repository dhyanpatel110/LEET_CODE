'''
Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
'''

#CODE:
  class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def backtrack(num, stack, target):
            if len(stack) == k:
                if target == 0:
                    res.append(stack)
                return 
            
            for x in range(num + 1, 10):
                if x <= target:
                    backtrack(x, stack + [x], target - x)
                else:
                    return
        backtrack(0, [], n)
        
        return res
      
      
      
