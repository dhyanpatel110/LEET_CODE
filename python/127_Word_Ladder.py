'''
Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
'''

#CODE:
  class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words, layer = set(wordList), {beginWord: [[beginWord]]}
        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord: 
                    return len(layer[w][0])
                else:
                    for i in range(len(w)):
                        for c in string.ascii_lowercase:
                            neww = w[:i] + c + w[i + 1:]
                            if neww in words:
                                newlayer[neww] += [j + [neww] for j in layer[w]]
            words -= set(newlayer.keys())
            layer = newlayer
        return 0
      
      
      
