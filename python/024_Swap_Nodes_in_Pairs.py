'''
Example 1:
  Input: head = [1,2,3,4]
  Output: [2,1,4,3]
  
  | col 1      | col 2      |
|------------|-------------|
| <img src="https://media.wired.com/photos/5926db217034dc5f91becd6b/master/w_582,c_limit/so-logo-s.jpg" width="250"> | <img src="https://mk0jobadderjftub56m0.kinstacdn.com/wp-content/uploads/stackoverflow.com-300.jpg" width="250"> |
'''
ODE:
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
      
      
      
      
      
