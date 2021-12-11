'''
Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321
'''
  
#CODE:
  class Solution:
    def reverse(self, num: int) -> int:
        sum = 0
        sign = 1
        
        if num < 0:
            sign = -1
            num = num * -1
            
        while num > 0:
            res = num%10
            sum = sum*10+res
            num = num//10
        
        if not -2147483648<sum<2147483647:
            return 0
        return sign*sum
   
       

    
    
