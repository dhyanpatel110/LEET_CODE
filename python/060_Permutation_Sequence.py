'''
Example 1:
  Input: n = 3, k = 3
  Output: "213"
  
Example 2:
  Input: n = 4, k = 9
  Output: "2314"
  
Example 3:
  Input: n = 3, k = 1
  Output: "123"
'''

#CODE:
  class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i)for i in range(1, n+1)]
        output = []
        factorial = math.factorial(n)
        index = k-1
        
        while (nums):
            factorial = factorial //len(nums)
            pos = index //factorial
            number = nums.pop(pos)
            output.append(number)
            index = index % factorial
        
        return "".join(output)
        
        
        
        
        
