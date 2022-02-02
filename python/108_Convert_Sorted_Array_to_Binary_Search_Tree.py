Example 1:
                0
	             / \
	           -3   9
	           /   /
	         -10  5

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
               
                0
	             / \
	           -10  5
	             \   \
	             -3   9
            
Example 2:

              3  1
             /    \
            1      3
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
 

#CODE:
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  class Solution:
      def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
          #L = left of the middle
          #R = right of the middle
        
          def helper(L, R):
              if L > R:
                  return None
            
              middle = (L + R) // 2
              root = TreeNode(nums[middle])
              root.left = helper(L, middle-1)
              root.right = helper(middle+1, R)
              return root
        
          return helper(0, len(nums)-1)
        
        
        
        
        
