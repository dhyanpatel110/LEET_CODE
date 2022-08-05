'''
Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false
'''

#CODE:
  class Solution:
    def isHappy(self, n: int) -> bool:
        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem: return False
            else: mem.add(n)
        else: return True
        
        
        
