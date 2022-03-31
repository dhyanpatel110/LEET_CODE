'''
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
'''

#CODE:
  # Definition for singly-linked list.
  # class ListNode:
  #     def __init__(self, x):
  #         self.val = x
  #         self.next = None

  class Solution:
      def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
         s = set()
          while head:
             if head not in s:
                  s.add(head)
                  head = head.next
             else:
                  break
          return head
        
        
        
