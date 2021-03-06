'''
Example 1:
1 -> 2 -> 3 -> 4 -> 5
          |
5 -> 4 -> 3 -> 2 -> 1
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
'''

#CODE:
  
  METHOD(1):
  class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
      
    
    METHOD(2):
    class Solution:
      def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
          return None
        
        newHead = head
        
        if head.next:
          newHead = self.reverseList(head.next)
          head.next.next = head
          head.next = None
        
        return newHead
      
      
      
