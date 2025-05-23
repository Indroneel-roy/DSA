from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False        

if __name__ == "__main__":
    nums = [1,2,3,1]    
    sol = Solution()
    print(sol.containsDuplicate(nums=nums))