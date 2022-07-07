'''
Example 1:
Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:
Input: root = []
Output: 0

Example 3:
Input: root = [1]
Output: 1
'''


#CODE:
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  class Solution:
      def countNodes(self, root: Optional[TreeNode]) -> int:
          if not root: return 0
          l = self.getDepth(root.left)
          r = self.getDepth(root.right)
          if l == r:
              return (1 << l) + self.countNodes(root.right)
          return (1 << r) + self.countNodes(root.left)
    
      def getDepth(self, root):
          if not root: return 0
          return 1 + self.getDepth(root.left)
  
  
  
