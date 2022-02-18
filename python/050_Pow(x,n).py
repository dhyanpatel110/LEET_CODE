'''
Example 1:
  Input: x = 2.00000, n = 10
  Output: 1024.00000
Example 2:
  Input: x = 2.10000, n = 3
  Output: 9.26100
Example 3:
  Input: x = 2.00000, n = -2
  Output: 0.25000
  Explanation: 2-2 = 1/22 = 1/4 = 0.25
'''

#CODE:
  #METHOD(1):
    class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
    
  #METHOD(2):
    class Solution:
    def myPow(self, x: float, n: int) -> float:
        #any number power of zero is one
        #2^0=1
        if n == 0:
            return 1
        
        #negative power
        #2^-2
        elif n<0:
            return self.myPow(1/x, -n)
        
        #even power
        #2^4
        elif n%2 == 0:
            temp = self.myPow(x, n/2)
            return temp*temp
        
        #odd power
        #2^5
        else :
            return x * self.myPow(x, n-1)
