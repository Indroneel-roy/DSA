#Problem Link : https://neetcode.io/problems/meeting-schedule
from typing import List

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        preEnd = intervals[0].end
        for i in range(1, len(intervals)):
            if preEnd <= intervals[i].start:
                preEnd = intervals[i].end
            else:
                return False
        return True  

if __name__ == "__main__":
    intervals = [Interval(0,30), Interval(5,10), Interval(15,20)] 
    sol = Solution()
    result = sol.canAttendMeetings(intervals)
    print(result)    