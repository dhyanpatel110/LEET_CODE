'''
Example 1:
  Input: head = [1,2,3,4,5], k = 2
  Output: [4,5,1,2,3]
  
Example 2:
  Input: head = [0,1,2], k = 4
  Output: [2,0,1]
'''

#CODE:
  class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        #get length
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length
        if k == 0:
            return head
        
        #move to the pivot and rotate
        cur = head
        for i in range (length - k - 1):
            cur = cur.next
        newHead = cur.next
        cur.next = None
        tail.next = head
        return newHead
      
      
      
      
      
