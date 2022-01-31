Example 1:
                 3
	              / \
	             9  20
	               /  \
	              15   7

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]
  
#CODE:
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  class Solution:
      def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
          if not inorder or not postorder:
              return None
        
          value = postorder[-1]
          root = TreeNode(value)
          indx = inorder.index(value)
        
          root.left = self.buildTree(inorder[:indx], postorder[:indx])
          root.right = self.buildTree(inorder[indx+1:], postorder[indx: -1])
        
          return root
        
        
        
        
        
