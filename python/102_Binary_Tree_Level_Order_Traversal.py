Example 1:
              3
             / \
            9  20
              /  \
             15   7

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

#CODE:
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  class Solution:
      def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
          res = []
          q = collections.deque()
          q.append(root)
        
          while q:
              qLen = len(q)
              level = []
            
              for i in range(qLen):
                  node = q.popleft()
                  if node:
                      level.append(node.val)
                      q.append(node.left)
                      q.append(node.right)
              if level:
                  res.append(level)
                
          return res
            
          
          
          
        
