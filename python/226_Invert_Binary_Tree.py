'''
Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
'''

#CODE:
  class Solution:
      def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
          #ROOT IS NULL RETURN NONE
          if not root:
              return None
        
          #SWAP THE CHILDREN
          tmp = root.left
          root.left = root.right
          root.right = tmp
        
          self.invertTree(root.left)
          self.invertTree(root.right)
        
          return root
        
        
        
