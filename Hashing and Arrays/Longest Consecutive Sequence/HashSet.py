# Problem Link : https://leetcode.com/problems/longest-consecutive-sequence/description/
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in numSet:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length) 
        return longest 
if __name__ == "__main__":
    nums = [0,3,7,2,5,8,4,6,0,1]
    sol = Solution()
    print(sol.longestConsecutive(nums))    