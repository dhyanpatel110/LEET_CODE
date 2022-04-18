'''
Example 1:
 4 => 2 => 1 => 3
        |
 1 => 2 => 3 => 4    
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
 -1 => 5 => 3 => 4 => 0
            |
 -1 => 0 => 3 => 4 => 5
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []
'''

#CODE:
  # Definition for singly-linked list.
  # class ListNode:
  #     def __init__(self, val=0, next=None):
  #         self.val = val
  #         self.next = next
  class Solution:
     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
          if not head:
              return
          current = head
          values = []
          while current:
              values.append(current.val)
              current = current.next
          values.sort(reverse=True)
          head = ListNode(values.pop())
          node = head
          while values:
              node.next = ListNode(values.pop())
              node = node.next
          return head
        
        
        
