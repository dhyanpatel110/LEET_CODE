'''

-> Given a string s, reverse only all the vowels in the string and return it.

-> The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"

'''

#CODE:
  class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = list(s)
        i,j = 0, len(s)-1

        while i < j :
            if lst[i] not in 'aeiouAEIOU':
                i += 1
            elif lst[j] not in 'aeiouAEIOU':
                j -= 1
            else:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1
        return ''.join(lst)

      
      
