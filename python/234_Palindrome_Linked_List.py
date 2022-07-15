'''
Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
'''

#CODE:
  #METHOD(1):
  class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        
        while head:
            nums.append(head.val)
            head = head.next
            
        l,r = 0, len(nums)-1
        
        while l <= r:
            if nums[l] != nums[r]:
                return False
            
            l += 1
            r -= 1
        return True
      
  #METHOD(2):
  class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev, curr = None, head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
      
      
      
