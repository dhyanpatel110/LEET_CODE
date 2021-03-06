'''
Example 1:
                
               1
              / \
             2   3

Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

0*10+1 = 1
1*10+2 = 12

Example 2:

                4
               / \
              9   0
             / \
            5   1

Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

0*4+4 = 4
4*10+9 = 49
9*10+5 = 95

'''

#CODE:
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  class Solution:
      def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
          def dfs (cur, num):
              if not cur:
                  return 0
            
              num = num*10 + cur.val
              if not cur.left and not cur.right:
                  return num
              return dfs(cur.left, num) + dfs(cur.right, num)
          return dfs(root, 0)
    
     
      
