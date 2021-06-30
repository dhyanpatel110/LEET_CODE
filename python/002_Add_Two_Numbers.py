#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]
#Explanation: 342 + 465 = 807.
#CODE:
  # Definition for singly-linked list.
  # class ListNode:
  #     def __init__(self, val=0, next=None):
  #         self.val = val
  #         self.next = next
  class Solution:
      def addTwoNumbers(self, l1, l2):
          # dummy head
          head = curr = ListNode(0)
          takeAway = 0
        
          while l1 or l2 or takeAway:
              v1 = v2 = 0
            
              if l1:
                  v1 = l1.val
                  l1 = l1.next
                
              if l2:
                  v2 = l2.val
                  l2 = l2.next
                
              total = v1 + v2 + takeAway
              takeAway = total // 10
              val = total % 10
              curr.next = ListNode(val)
              curr = curr.next
            
          return head.next
       
      
      
      
      
      
