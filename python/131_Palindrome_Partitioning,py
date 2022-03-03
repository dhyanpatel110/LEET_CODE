'''
Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
'''

#CODE:
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        q, n = [[s[0]]], len(s)
        for i in range(1, n):
            new = []
            for arr in q:
                cur = arr[-1] + s[i]
                if i < n - 1 or cur == cur[::-1]:
                    new.append(arr[:-1] + [cur])
                if arr[-1] == arr[-1][::-1]:
                    new.append(arr + [s[i]])
            q = new
        return q
        
        
        
