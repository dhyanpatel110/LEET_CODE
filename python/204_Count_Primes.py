'''
Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0
'''

CODE:
  class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [True] * n
        i = 2
        while i * i < n:
            if is_prime[i]:
                j = i * i
                while j < n:
                    is_prime[j] = False
                    j += i
            i += 1
        return sum(is_prime[2:])
      
      
