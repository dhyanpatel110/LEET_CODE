Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
  
Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]
  
#CODE:
  # Definition for singly-linked list.
  # class ListNode:
  #     def __init__(self, val=0, next=None):
  #         self.val = val
  #         self.next = next
  class Solution:
      def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
          if head == None or head.next == None:
              return head
          next = head.next
          
          if next.val == head.val:
              while next != None and next.val == head.val:
                  next = next.next
              return self.deleteDuplicates(next)
          else:
              head.next = self.deleteDuplicates(next)
              return head
