from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1           

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9  
    sol = Solution()
    res = sol.search(nums, target)
    print(res)  