Example 1:
  Input: nums1 = [1,3], nums2 = [2]
  Output: 2.00000
  Explanation: merged array = [1,2,3] and median is 2
    
Example 2:
  Input: nums1 = [1,2,3,4,5]
  Output: 3.00000
  Explanation: median(middle) is 3
    
Example 3:
  Input: nums1 = [1,2], nums2 = [3,4]
  Output: 2.50000
  Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5
    
Example 4:
  Input: nums1 = [1,2,4,7]
  Output: 2.50000
  Explanation: median(middle) is (2 + 4) / 2 = 3   

    
CODE:
  class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ls1 = len(nums1)
        ls2 = len(nums2)
        
        if ls1 < ls2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        l = 0
        r = ls2 * 2
        
        while l <= r:
            mid2 = (l + r) >> 1
            mid1 = ls1 + ls2 - mid2
            
            L1 = -sys.maxsize - 1 if mid1 == 0 else nums1[(mid1 - 1) >> 1]
            L2 = -sys.maxsize - 1 if mid2 == 0 else nums2[(mid2 - 1) >> 1]
            
            R1 = sys.maxsize if mid1 == 2 * ls1 else nums1[mid1 >> 1]
            R2 = sys.maxsize if mid2 == 2 * ls2 else nums2[mid2 >> 1]
            
            if L1 > R2:
                l = mid2 + 1
            elif L2 > R1:
                r = mid2 - 1
            else:
                return (max(L1, L2) + min(R1, R2)) / 2.0
              
              
              
              
              
