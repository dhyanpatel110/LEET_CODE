'''
Example 1:
Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"

Example 2:
Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
'''

#CODE:
  class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        bucket = [0] * 10
        
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                bucket[int(s)] +=1
                bucket[int(g)] -=1
        return f'{bulls}A{len(secret) - bulls-sum(x for x in bucket if x>0)}B'
        
        
        
