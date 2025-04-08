from typing import List
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        minHip = list(count.keys())
        heapq.heapify(minHip)
        while minHip:
            first = minHip[0]
            for i in range(first, first+groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minHip[0]:
                        return False
                    heapq.heappop(minHip)
        return True
if __name__ == "__main__":
    hand = [1,2,3,6,2,3,4,7,8]
    groupSize = 3
    s = Solution()
    print(s.isNStraightHand(hand, groupSize))
                        