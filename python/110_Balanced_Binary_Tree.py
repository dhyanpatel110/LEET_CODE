'''
Example 1:
              3
             / \
            9  20
               / \
              15  7

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
               1
              / \
             2   2
            / \
           3   3
          / \
         4   4
          
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
'''

#CODE:
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  class Solution:
      def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
          def dfs(root):
              if not root:
                  return [True, 0]
        
              left = dfs(root.left)
              right = dfs(root.right)
              balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
        
              return [balanced, 1 + max(left[1], right[1])]
    
          return dfs(root)[0]
    
    
    
    
    
