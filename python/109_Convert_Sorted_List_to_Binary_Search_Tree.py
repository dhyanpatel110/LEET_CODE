'''

-> Given the head of a singly linked list where elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.
 
Example 1:
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

Example 2:
Input: head = []
Output: []

'''

CODE:
  # Definition for singly-linked list.
  # class ListNode:
  #     def __init__(self, val=0, next=None):
  #         self.val = val
  #         self.next = next
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  class Solution:
      def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
          def traverse(arr):
                  if arr == []: 
                      return
                  node = TreeNode(arr[len(arr)//2])
                  node.left = traverse(arr[:len(arr)//2])
                  node.right = traverse(arr[len(arr)//2+1:])
                  return node
            
          array = []
          while head: array.append(head.val); head = head.next
          return traverse(array)
        
        
        
