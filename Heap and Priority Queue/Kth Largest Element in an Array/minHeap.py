# Problem Link : https://leetcode.com/problems/kth-largest-element-in-an-array/
import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

if __name__ == "__main__":
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    sol = Solution()
    print(sol.findKthLargest(nums, k))    
        