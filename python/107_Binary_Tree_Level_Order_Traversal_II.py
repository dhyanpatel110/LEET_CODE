Example 1:
          
               3
              / \
             9  20
               /  \
              15   7

Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]

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
      def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
          result = []
        
          if root == None:
              return result
        
          Queue = []
          Queue.append(root)
        
          while len(Queue)>0:
              nodes = []
              for i in range (len(Queue)):
                  node=Queue.pop(0)
                  nodes.append(node.val)
                  if node.left != None:
                      Queue.append(node.left)
                  if node.right != None: 
                      Queue.append(node.right)
              result.insert(0,nodes)
        
          return result
        
        
        
        
        
