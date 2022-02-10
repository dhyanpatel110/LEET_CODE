'''
Example 1:
             1
	          / \
	         2   3

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
            -10
	          / \
	         9  20
	           /  \
	          15   7

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
'''

#CODE:
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  class Solution:
      def maxPathSum(self, root: Optional[TreeNode]) -> int:
          res = [root.val]
        
          #return max path sum without split
          def dfs(root):
              if not root:
                  return 0
            
              leftMax = dfs(root.left)
              rightMax = dfs(root.right)
              leftMax = max(leftMax, 0)
              rightMax = max(rightMax, 0)
            
              #compute max path sum WITH split
              res[0] = max(res[0], root.val + leftMax + rightMax)
            
              return root.val + max(leftMax, rightMax)
        
          dfs(root)
          return res[0]
