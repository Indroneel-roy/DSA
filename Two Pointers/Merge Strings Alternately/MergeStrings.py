# Problem Link : https://leetcode.com/problems/merge-strings-alternately/description/
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_1 = len(word1)
        len_2 = len(word2)
        i, j = 0, 0
        res = ""
        while i < len_1 and j < len_2:
            res += word1[i] + word2[j]
            i += 1
            j += 1
        res += word1[i:] + word2[j:] 
        return res   
if __name__ == "__main__":
    word1 = "ab"
    word2 = "pqrs"
    sol = Solution()
    print(sol.mergeAlternately(word1, word2))    