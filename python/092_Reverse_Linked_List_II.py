'''
Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
'''

  #CODE:
  # Definition for singly-linked list.
  # class ListNode:
  #     def __init__(self, val=0, next=None):
  #         self.val = val
  #         self.next = next
  class Solution:
      def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
          dummy = ListNode(0, head)
        
          #1) reach node at position "left"
          leftPrev, cur = dummy, head
          for i in range(left-1):
              leftPrev, cur = cur, cur.next
        
          # Now  cur="left" , leftPrev="node before left"
          #2) reverse from left to right
          prev = None
          for i in range(right-left+1):
              tmpNext=cur.next
             cur.next = prev
              prev,cur = cur, tmpNext
            
          #3) update pointers
          leftPrev.next.next = cur  #cur is node after "right"
          leftPrev.next = prev   #prev is "right" 
          return dummy.next
        
        
        
        
