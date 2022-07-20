'''
Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 
Example 2:
Input: nums = [1], k = 1
Output: [1]
''''

#CODE:
  class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque() #index
        left = 0
        right = 0
        
        while right < len(nums):
            #pop smaller value from q
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)
            
            #remove left value from window
            if left > q[0]:
                q.popleft()
                
            if (right + 1) >= k:
                output.append(nums[q[0]])
                left += 1
            right += 1
        return output

        
        
