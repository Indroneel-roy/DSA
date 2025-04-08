from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0
        while r < len(nums) - 1:
            largest_step = 0
            for i in range(l, r+1):
                largest_step = max(largest_step, i + nums[i])
            l = r + 1
            r = largest_step
            res += 1
        return res        
        
if __name__ == "__main__":
    nums = [2,3,1,1,4]
    s = Solution()
    print(s.jump(nums))            