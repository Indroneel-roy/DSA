#problem link : https://leetcode.com/problems/find-the-duplicate-number/description/
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        #Find a cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        #second iteration start from beginning and will joining point where solw == slow2
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow   
if __name__ == "__main__":
    nums = [3,1,3,4,2]
    sol = Solution()
    res = sol.findDuplicate(nums)
    print(res)            