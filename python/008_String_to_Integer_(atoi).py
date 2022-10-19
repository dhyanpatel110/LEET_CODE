'''
42 {42}
-42 {-42}
4193 with wprds {word started with numneric 4193 is accepted other words are avoide}
words and 987 {word starting with string so hole sentance are avoide}
-91283472332 {it is out of range  conver to -2147483648}
'''

#CODE:
             
class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if not str:
            return 0
        if str[0] not in "+-0123456789":
            return 0
        if str[0] in "+-":
            if len(str) == 1:
                return 0
            elif str[1].isdigit() == False:
                return 0
        if str[0] == "-":
            sign = -1
        else :
            sign = 1
        
        str = str.strip("+")
        str = str.strip("-")
        i = 0
        res = ""
        
        while i < len(str) and str[i].isdigit():
            res += str[i]
            i += 1
        res_int = int(res)
        res_int = res_int*sign
        if res_int >2**31 - 1:
            return 2**31 - 1
        elif res_int < -2**31:
            return -2**31
        
        else:
            return res_int
          
          
          
          
          
