from typing import List
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        count = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    count.add(i)
        return True if len(count) == 3 else False 

if __name__ == "__main__":
    triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]
    target = [5,5,5] 
    s = Solution()
    print(s.mergeTriplets(triplets, target))   