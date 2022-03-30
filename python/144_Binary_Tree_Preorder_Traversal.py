'''
Example 1:

           1
            \
             2
            /
           3

Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]
'''

#CODE:
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  class Solution:
      def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
          result = []
        
          def recursive(root, result):
              if not root:
                  return 
              result.append(root.val)
              recursive(root.left, result)
              recursive(root.right, result)
          recursive(root, result)
          return result
        
  
  
