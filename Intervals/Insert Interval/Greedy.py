# Problem Link : https://leetcode.com/problems/insert-interval/description/
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(intervals[i][0], newInterval[0]),
                    max(intervals[i][1], newInterval[1])
                ]
                
        res.append(newInterval) 
        return res               
        
if __name__ == "__main__":
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]        
    sol = Solution()
    result = sol.insert(intervals, newInterval)
    print(result)