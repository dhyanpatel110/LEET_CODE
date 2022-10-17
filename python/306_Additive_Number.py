'''
Problem:
An additive number is a string whose digits can form an additive sequence.
A valid additive sequence should contain at least three numbers. 
Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.
Given a string containing only digits, return true if it is an additive number or false otherwise.
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:
Input: "112358"
Output: true
Explanation: 
The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8 

Example 2:
Input: "199100199"
Output: true
Explanation: 
The additive sequence is: 1, 99, 100, 199. 
1 + 99 = 100, 99 + 100 = 199
'''

#CODE:
  class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        #1. find all num1 and num2 combinations
        for i in range(1, n):
            for j in range(i+1, n):
                num1 = num[:i]
                num2 = num[i:j]

                # check whether there leading 0
                # 02 X
                # o id Ok
                if (num1[0] == '0' and i > 1) or (num2[0] == '0' and j-i > 1):
                    continue
                
                #112358
                # 1 1
                # 1+1 = 2
                # "2"

                while j < n:
                    num3 = str(int(num1) + int(num2))
                    if not num.startswith(num3, j):
                        break
                    j += len(num3)
                    num1, num2 = num2, num3
                
                if j == n:
                    return True
        return False

                
        
