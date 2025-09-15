# Problem Link : https://leetcode.com/problems/contains-duplicate-ii/description/
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        seen = set()
        for r in range(len(nums)):
            if r - l > k:
                seen.remove(nums[l])
                l += 1
            if nums[r] in seen:
                return True
            seen.add(nums[r])
        return False        

if __name__ == "__main__":
    nums = [1,2,3,1,2,3]
    k = 4
    sol = Solution()
    print(sol.containsNearbyDuplicate(nums, k))
