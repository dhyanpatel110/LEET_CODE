'''
Example 1:
  Input: head = [1,2,3,4,5], k = 2
  Output: [2,1,4,3,5]

Example 2:
  Input: head = [1,2,3,4,5], k = 3
  Output: [3,2,1,4,5]

Example 3:
  Input: head = [1,2,3,4,5], k = 1
  Output: [1,2,3,4,5]
'''
CODE:
  class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        stack = []
        new_head = ListNode()
        node = new_head
        i = 0
        while head:
            while i != k and head:
                i += 1
                stack.append(head)
                head = head.next
            while i == k and stack:
                node.next = stack.pop()
                node = node.next
                node.next = None
            i = 0
        if stack:
            node.next = stack.pop(0)
        return new_head.next
      
      
      
      
      
