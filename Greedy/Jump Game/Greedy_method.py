from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    s = Solution()
    print(s.canJump(nums))            