from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
        return True   
if __name__ == "__main__":
    nums = [3,2,2,0,4]
    sol = Solution()
    print(sol.canJump(nums))
        

        