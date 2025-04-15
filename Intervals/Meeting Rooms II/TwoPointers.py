# Problem Link : https://neetcode.io/problems/meeting-schedule-ii
from typing import List

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0
        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)
        return res                     
if __name__ == "__main__":
    intervals = [Interval(0,30), Interval(5,10), Interval(15,20)] 
    sol = Solution()
    result = sol.minMeetingRooms(intervals)
    print(result)  