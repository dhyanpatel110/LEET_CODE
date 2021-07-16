Example 1:
  Input: nums = [1,0,-1,0,-2,2], target = 0
  Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    
Example 2:
  Input: nums = [2,2,2,2,2], target = 8
  Output: [[2,2,2,2]]

CODE:
  class Solution(object):
    def fourSum(self, nums, target):
        sort_nums = sorted(nums)
        ls = len(nums)
        res = {}
        pairs = {}
        for i in range(ls - 3):
            for j in range(i + 1, ls - 2):
                res_2 = sort_nums[i] + sort_nums[j]
                try:
                    pairs[target - res_2].append([i, j])
                except KeyError:
                    pairs[target - res_2] = [[i, j]]
        for key, temp in pairs.items():
            for pair in temp:
                j = pair[1] + 1
                k = ls - 1
                while j < k:
                    current = sort_nums[j] + sort_nums[k]
                    if current == key:
                        result = (sort_nums[pair[0]], sort_nums[pair[1]], sort_nums[j], sort_nums[k])
                        res[result] = True
                        j += 1
                    elif current < key:
                        j += 1
                    else:
                        k -= 1
        return res.keys()

      
      
      
      
      
