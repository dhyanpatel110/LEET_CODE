'''
Example 1:

  	    5
	     / \
	    4   8
	   /   / \
	  11  13  4
	 /  \    / \
	7    2  5   1

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:
              1
             / \
            2   3

Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:
Input: root = [1,2], targetSum = 0
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
      def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
          self.output = []
        
          def dfs(node, path, sm):
              sm += node.val
              tmp = path + [node.val]
              if node.left:
                  dfs(node.left, tmp, sm)
              if node.right:
                  dfs(node.right, tmp, sm)
              if not node.left and not node.right and sm==targetSum:
                  self.output.append(tmp)
        
          if not root:
              return[]
          dfs(root, [], 0)
          return self.output
      
      
      
      
      
