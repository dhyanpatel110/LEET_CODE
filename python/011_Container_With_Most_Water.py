Example 1:
  https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg
  Input: height = [1,8,6,2,5,4,8,3,7]
  Output: 49
  Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
'''
#CODE:
  class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        largest = 0
        
        while start != end:
            next_are = min(height[start],height[end]) * (end-start)
            if next_are > largest:
                largest = next_are
                
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return(largest)
      
      
      
      
      
