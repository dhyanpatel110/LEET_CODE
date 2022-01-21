Example 1:

            2
           / \
          1   3
Input: root = [2,1,3]
Output: true

Example 2:
  
            5
           / \
          1   4
             / \
            3   6
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

#CODE:
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  
  class Solution:
      def isValidBST(self, root: Optional[TreeNode]) -> bool:
          def valid(node, left, right):
              if not node:
                  return True
            
              if not (node.val < right and node.val > left):
                  return False
            
              return(valid(node.left, left, node.val)) and (valid(node.right, node.val, right))
        
          return valid(root, float('-inf'), float('inf'))
        
        
        
        
        
