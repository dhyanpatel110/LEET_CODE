'''
Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
'''
#CODE:
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = collections.Counter(list(s))

        for i in range(len(s)):
            if counter.get(s[i])  == 1:
                return i
        return -1
      
      
      
