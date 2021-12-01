'''
Example 1:
  Input: s = "III"
  Output: 3
    
Example 2:
  Input: s = "LVIII"
  Output: 58
  Explanation: L = 50, V= 5, III = 3.
'''

#CODE:
  class Solution:
    def romanToInt(self, s: str) -> int:
        roman_table = {"I" : 1,
                       "V" : 5,
                       "X" : 10,
                       "L" : 50,
                       "C" : 100,
                       "D" : 500,
                       "M" : 1000,
                      }
        
        num = 0
        last = "I"
        
        for numeral in s[::-1]:
            if roman_table[numeral] < roman_table[last]:
                num -= roman_table[numeral]
            else:
                num += roman_table[numeral]
            last = numeral
        return num
            
 


