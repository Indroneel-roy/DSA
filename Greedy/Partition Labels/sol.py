from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}  # storing the last index of each character

        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        start, end = 0, 0
        size = 0

        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0

        return res            

if __name__ == "__main__":
    s = "ababcbacadefegdehijhklij"
    sol = Solution()
    result = sol.partitionLabels(s=s)
    print(result)


            