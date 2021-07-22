'''
Example 1:
  Input: head = [1,2,3,4]
  Output: [2,1,4,3]
'''

CODE:
  class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        d1 = d = ListNode(0)
        d.next = head
        
        while d.next and d.next.next:
            
            p = d.next
            q = d.next.next
            d.next,p.next,q.next = q,q.next,p
            d = p
        return d1.next
      
      
      
      
      
