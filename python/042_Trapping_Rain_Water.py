'''
Example 1:
  Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
  Output: 6
  Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
    
Example 2:
  Input: height = [4,2,0,3,2,5]
  Output: 9
'''

#CODE:
  class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
        	return 0
        
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        result = 0
        
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                result += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                result += rightMax - height[right]
        return result 
        
        
        
        
        
