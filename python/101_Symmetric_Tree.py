Example 1:

            1
           / \
          2   2
         / \ / \
        3  4 4  3
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

            1
           / \
          2   2
           \   \
           3    3
Input: root = [1,2,2,null,3,null,3]
Output: false

#CODE:
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  class Solution:
      def isSymmetric(self, root: Optional[TreeNode]) -> bool:
          if root is None:
              return True
        
          return self.isMirror(root.left, root.right)
    
      def isMirror(self, leftroot, rightroot):
          if leftroot and rightroot:
              return leftroot.val == rightroot.val and self.isMirror(leftroot.left, rightroot.right) and self.isMirror(leftroot.right, rightroot.left)
          return leftroot == rightroot
    
       
      
      
      
