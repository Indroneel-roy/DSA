# problem link : https://leetcode.com/problems/car-pooling/description/
import heapq
from typing import List
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t : t[1])
        minHeap = [] #[end, numPass]
        curPass = 0
        for t in trips:
            numPass, start, end = t
            while minHeap and minHeap[0][0] <= start:
                curPass -= minHeap[0][1]
                heapq.heappop(minHeap)
            curPass += numPass
            if curPass > capacity:
                return False
            heapq.heappush(minHeap, [end, numPass])
        return True     
if __name__ == "__main__":
    obj = Solution()
    # Example 1
    trips = [[2,1,5],[3,3,7]]
    capacity = 4
    print(obj.carPooling(trips, capacity)) # return False
    # Example 2
    trips = [[2,1,5],[3,3,7]]
    capacity = 5
    print(obj.carPooling(trips, capacity)) # return True
    # Example 3
    trips = [[2,1,5],[3,5,7]]
    capacity = 3
    print(obj.carPooling(trips, capacity)) # return True
    # Example 4
    trips = [[3,2,7],[3,7,9],[8,3,9]]
    capacity = 11
    print(obj.carPooling(trips, capacity)) # return True           
        