Example 1:
  
    1                  1
   / \                  \
  2   5       =>         2
 / \   \                  \
3   4   6                  3
                            \
                             4
                              \
                               5
                                \
                                 6


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]
  
#CODE:
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  class Solution:
      def flatten(self, root: Optional[TreeNode]) -> None:
          """
          Do not return anything, modify root in-place instead.
          """
          def dfs(root):
              if not root:
                  return None
            
              leftTail = dfs(root.left)
              rightTail = dfs(root.right)
            
              if root.left:
                  leftTail.right = root.right
                  root.right = root.left
                  root.left = None
              last = rightTail or leftTail or root
              return last
          dfs(root)
      
      
      
      
    
