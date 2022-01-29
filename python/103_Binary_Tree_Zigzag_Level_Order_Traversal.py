'''
Example 1:
            3
           / \
          9  20
            /  \
           15   7

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
'''

#CODE:
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  class Solution:
      def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
          output = []
          def dfs(node, level, output):
              if not node:
                  return
              if len(output) <= level:
                  output += [[]]
              dfs(node.left, level+1, output)
              dfs(node.right, level+1, output)
              if level % 2 == 0:
                  output[level].append(node.val)
              else:
                  output[level].insert(0, node.val)
        
          dfs(root, 0, output)
          return output
            
        
        
        
        
