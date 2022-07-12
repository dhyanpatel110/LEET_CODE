'''
Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
'''


#CODE:
  class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        start, ls = 0, len(nums)
        for i in range(ls):
            if i + 1 <  ls and nums[i + 1] == nums[i] + 1:
                continue
            if i == start:
                res.append(str(nums[start]))
            else:
                res.append("%d->%d" % (nums[start], nums[i]))
            start = i + 1
        return res
      
      
      
