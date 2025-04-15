# Problem Link : https://leetcode.com/problems/non-overlapping-intervals/description/
from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        preEnd = intervals[0][1]
        for start, end in intervals[1 : ]:
            if preEnd <= start:
                preEnd = end
            else:
                res += 1
                preEnd = min(end, preEnd)
        return res    

if __name__ == "__main__":
    intervals = [[1,2],[1,2],[1,2]]
    sol = Solution()
    result = sol.eraseOverlapIntervals(intervals)
    print(result)    