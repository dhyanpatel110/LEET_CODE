Example 1:
              3
             / \
            9  20
              /  \
             15   7

Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
  
#CODE:
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  class Solution:
      def minDepth(self, root: Optional[TreeNode]) -> int:
        
          if not root:
              return 0
        
          if not root.left and not root.right:
              return 1
        
          if not root.left and root.right:
              return 1 + self.minDepth(root.right)
        
          if not root.right and root.left:
              return 1 + self.minDepth(root.left)
        
          return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        
        
     
    
        
