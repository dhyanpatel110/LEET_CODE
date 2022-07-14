''
Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1
  
Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16
  
Example 3:
Input: n = 3
Output: false
'''

#CODE:
  #METHOD(1);
  class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n <= 0:
            return False
        return n & (n-1) == 0
      
  #METHOD(2);
  class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 2 ==  0:
            n /= 2
        return n == 1
        
        
        
        
