'''
 1
 one time 1
 11
        
 21
 one time 2 ,one time 1
 1211
        
 1211
 one time 1 , one time 2 ,two time 1
 111221

 3322251
 two time 3 , three time 2 , one time 5, one time 1
 23321511
'''

CODE:
  class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
        	return "1"
        
        prev = self.countAndSay(n-1)
        res = ""
        ct = 1
        
        #if tow element not same
        for i in range(len(prev)):
            if i == len(prev)-1 or prev[i] != prev[i+1]:
                res += str(ct) + prev[i]
                ct = 1
            else:
                ct += 1
        return res
      
      
      
      
        
