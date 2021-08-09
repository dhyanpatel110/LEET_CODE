'''
Example 1:
  Input: num1 = "2", num2 = "3"
  Output: "6"
    
Example 2:
  Input: num1 = "123", num2 = "456"
  Output: "56088"
'''

CODE:
  class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1,num2]:
            return "0"
        
        res = [0]*(len(num1) + len(num2))
        #reverse string
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                res[i1 + i2] += int(num1[i1]) * int(num2[i2])
                res[i1 + i2 + 1] += (res[i1 +i2] // 10)
                res[i1 + i2] = res[i1 + i2] % 10
                
        res = res[::-1] #reverse 
        beg = 0
        
        while beg < len(res) and res[beg] == 0:
            beg += 1
            
        res = map(str,res[beg:])
        return"".join(res)
      
      
      
      
      
