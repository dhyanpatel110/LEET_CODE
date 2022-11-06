'''
Example 1:
  Input: lists = [[1,4,5],[1,3,4],[2,6]]
  Output: [1,1,2,3,4,4,5,6]
  Explanation: The linked-lists are:
  [
     1->4->5,
     1->3->4,
     2->6
  ]
  merging them into one sorted list:
  1->1->2->3->4->4->5->6
  
'''

#CODE:
  class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.node = []
        dummy = head = ListNode(0)
        
        for l in lists:
            while l:
                self.node.append(l.val)
                l = l.next
                
        for x in sorted(self.node):
            dummy.next = ListNode(x)
            dummy = dummy.next
        return head.next
      
      
      
      
      
