# problem link : https://leetcode.com/problems/open-the-lock/description/
from collections import deque
from typing import List
class Solution:
    
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        def childern(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10) 
                res.append(lock[ : i] + digit + lock[i+1 : ])   
                digit = str((int(lock[i]) - 1 + 10) % 10) 
                res.append(lock[ : i] + digit + lock[i+1 : ])  
            return res

        q = deque()
        q.append(["0000", 0]) # lock, turns
        visit = set(deadends)
        while q:

            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in childern(lock):
                if child not in visit:
                    visit.add(child)
                    q.append([child, turns + 1])
        return -1           
if __name__ == "__main__":
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
    sol = Solution()
    print(sol.openLock(deadends, target)) 

