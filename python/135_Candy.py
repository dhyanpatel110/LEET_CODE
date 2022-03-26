'''
Example 1:
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
'''

#CODE:
  class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        o = [1 for _ in range(N)]
        
        for i in range(1,N):
            if ratings[i] > ratings[i-1]:
                o[i] = max(o[i-1] + 1, o[i])
        
        for i in range(N-2, -1, -1):
            if  ratings[i]>ratings[i+1]:
                o[i] = max(o[i+1]+1, o[i])
        
        return sum(o)
     
    
    
