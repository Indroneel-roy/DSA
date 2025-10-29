# Problem link : https://leetcode.com/problems/word-ladder/description/
from typing import List
from collections import deque, defaultdict
import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1 : ]
                nei[pattern].append(word)
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1 : ] 
                    for newWord in nei[pattern]:
                        if newWord not in visit:
                            visit.add(newWord)
                            q.append(newWord)
            res += 1
        return 0                                  
if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    sol = Solution()
    print(sol.ladderLength(beginWord, endWord, wordList))