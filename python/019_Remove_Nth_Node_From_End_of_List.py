'''
Example 1:
  Input: head = [1,2,3,4,5], n = 2
  Output: [1,2,3,5]
  
Example 2:
  Input: head = [1], n = 1
  Output: []
  
Example 3:
  Input: head = [1,2], n = 1
    Output: [1]
'''

#CODE:
  class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        fast = slow = head
        for i in range(n):
            fast = fast.next
            
        if fast is None:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
        
        
        
        
        
