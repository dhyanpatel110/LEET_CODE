'''
Example 1:
  Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
  Output:
  [
     "This    is    an",
     "example  of text",
     "justification.  "
  ]
  
Example 2:
  Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
  Output:
  [
    "What   must   be",
    "acknowledgment  ",
    "shall be        "
  ]
  Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
  Note that the second line is also left-justified becase it contains only one word.
  
Example 3:
  Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
  Output:
  [
    "Science  is  what we",
    "understand      well",
    "enough to explain to",
    "a  computer.  Art is",
    "everything  else  we",
    "do                  "
  ]
'''

#CODE:
  class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lst = []
        res = []
        n = 0
        
        for w in words:
            
            while len(w) + n + len(lst) > maxWidth:
                gaps = (len(lst) - 1) or 1
                q, rem = divmod(maxWidth - n, gaps)
                for i in range (gaps):
                    lst[i] += " " * q + (" " if i < rem else "")
                res.append("".join(lst))
                n, lst = 0, []
            
            lst.append(w)
            n += len(w)
             
        return res + [" ".join(lst).ljust(maxWidth)] if lst else []
      
      
      
      
      
