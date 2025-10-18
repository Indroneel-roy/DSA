# Problem link : https://leetcode.com/problems/verifying-an-alien-dictionary/description/
from typing import List
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        OrderID = { c : i  for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                if w1[j] != w2[j]:
                    if OrderID[w2[j]] < OrderID[w1[j]]:
                        return False
                    break
        return True    
if __name__ == "__main__":
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    sol = Solution()
    print(sol.isAlienSorted(words, order))    