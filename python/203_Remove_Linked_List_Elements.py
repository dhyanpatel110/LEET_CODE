'''
Example 1:
1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
               |
     1 -> 2 -> 3 -> 4 -> 5

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []
'''

CODE:
  # Definition for singly-linked list.
  # class ListNode:
  #     def __init__(self, val=0, next=None):
  #         self.val = val
  #         self.next = next
  class Solution:
      def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
          dummy = ListNode(next = head)
          prev = dummy
          curr = head
        
          while curr:
              nxt = curr.next
            
              if curr.val == val:
                  prev.next = nxt
              else:
                  prev = curr
            
              curr = nxt
          return dummy.next
        
        
        
