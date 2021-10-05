'''
Example 1:
  Input: s = "0"
  Output: true
  
Example 2:
  Input: s = "e"
  Output: false
  
Example 3:
  Input: s = "."
  Output: false
  
Example 4:
  Input: s = ".1"
  Output: true
'''

#CODE:
  class Solution:
    def isNumber(self, s: str) -> bool:
        
        digit,dec,e,symbol = False, False, False, False
        
        for c in s:
            if c in '0123456789':
                digit = True
            elif c in '+-':
                if symbol or digit or dec:
                    return False
                else:
                    symbol = True
                    
            elif c in 'Ee':
                if not digit  or e:
                    return False
                else:
                    e = True
                    symbol = False
                    digit = False
                    dec = False
                    
            elif c == '.':
                if dec  or e:
                    return False
                else:
                    dec = True
            else:
                return False
            
        return  digit
      
      
      
      
      
