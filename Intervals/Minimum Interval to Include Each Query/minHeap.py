#problem link : https://leetcode.com/problems/minimum-interval-to-include-each-query/description/
#time complexity is O(nlogn + qlogq)
#space complexity is O(n+m)
from typing import List
import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []
        res = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]            
        

if __name__ == "__main__":
    intervals = [[1,4],[2,4],[3,6],[4,4]]
    queries = [2,3,4,5]
    sol = Solution()
    print(sol.minInterval(intervals, queries))    