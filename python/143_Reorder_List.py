'''
Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
'''

CODE:
  # Definition for singly-linked list.
  # class ListNode:
  #     def __init__(self, val=0, next=None):
  #         self.val = val
  #         self.next = next
  class Solution:
      def reorderList(self, head: Optional[ListNode]) -> None:
          """
          Do not return anything, modify head in-place instead.
          """
          #find middle
         slow = head
          fast = head.next
        
         while fast and fast.next:
              slow = slow.next
              fast = fast.next.next
            
          #reverse second half
          second = slow.next
          prev = slow.next = None
          while second:
              tmp = second.next
              second.next = prev
              prev = second
              second = tmp
        
          #merge two half
          first = head
          second = prev
        
          while second:
              tmp1, tmp2 = first.next, second.next
              first.next = second
              second.next = tmp1
              first,second = tmp1,tmp2
        
        
