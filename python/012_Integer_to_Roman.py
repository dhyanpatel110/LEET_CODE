'''
Example 1:
  Input: num = 9
  Output: "IX"

Example 2:
  Input: num = 58
  Output: "LVIII"
  Explanation: L = 50, V = 5, III = 3.

Example 3:
  Input: num = 1994
  Output: "MCMXCIV"
  Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

#CODE:
  Language: python3
  class Solution(object):
     def intToRoman(self, num):
         roman_dim = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
                      [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'],
                      [9,'IX'], [5, 'V'], [4, 'IV'], [1, 'I']]
         if num == 0:
             return ''
         roman_str = ''
         current, dim = num, 0
         while current != 0:
             while current // roman_dim[dim][0] == 0:
                 dim += 1
             while current - roman_dim[dim][0] >= 0:
                 current -= roman_dim[dim][0]
                 roman_str += roman_dim[dim][1]
         return roman_str
      
  Language: python    
  class Solution(object):
    def intToRoman(self, num):
        values = [1000, 900, 500, 400,
                  100, 90, 50, 40,
                  10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD",
                   "C", "XC", "L", "XL",
                   "X", "IX", "V", "IV",
                   "I"]
        roman = ''
        i = 0
        while num > 0:
            k = num / values[i]
            for j in range(k):
                roman += symbols[i]
                num -= values[i]
            i += 1
        return roman

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.intToRoman(90)
    
    
    
    
      
