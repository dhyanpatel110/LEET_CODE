'''
Example 1:
  
                1                1 - NULL
               / \              / \
              2   3            2 - 3 - NULL
             / \ / \          / \ / \
            4  5 6  7        4--5-6--7 - NULL

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Example 2:
Input: root = []
Output: []
'''

#CODE:
  """
  # Definition for a Node.
  class Node:
      def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
          self.val = val
          self.left = left
          self.right = right
          self.next = next
  """

  class Solution:
      def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
          if  not root:
              return root
        
          q = collections.deque()
          q.append(root)
        
          while q:
              curr = q.popleft()
              if curr.left and curr.right:
                 curr.left.next = curr.right
                  if curr.next:
                      curr.right.next = curr.next.left
                  q.append(curr.left)
                  q.append(curr.right)
              else:
                  break
          return root
      
      
      
      
      
