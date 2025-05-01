# Problem Link : https://leetcode.com/problems/sliding-window-maximum/description/
# Time and space complexity O(n) and O(n)
from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()
        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            if l > q[0]:
                q.popleft()
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output
if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    sol = Solution()
    res = sol.maxSlidingWindow(nums, k)
    print(res)                    
        