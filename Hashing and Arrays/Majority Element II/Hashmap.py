# Problem Link : https://leetcode.com/problems/majority-element-ii/description/
from typing import List
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            if len(count) <= 2:
                continue
            new_count = defaultdict(int)
            for n, c in count.items():
                if c > 1:
                    new_count[n] = c -1
            count = new_count
        res = []
        for n in count:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        return res    
    
if __name__ == "__main__":
    nums = [3,2,3]
    sol = Solution()
    print(sol.majorityElement(nums))
                      
