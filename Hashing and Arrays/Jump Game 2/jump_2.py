from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:

        jump = 0
        farthest = 0
        current_end = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jump += 1
                current_end = farthest
        return jump        
# This greedy solution never deal with not reachablble like jump 1 game
if __name__ == "__main__":
    nums = [2,3,1,1,4]
    sol = Solution()
    print(sol.jump(nums))