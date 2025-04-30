#Problem  Link : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# using tow pointer concept so time complexity reduce to O(n) and space complexity O(1)
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum < target:
                l += 1
            elif currSum > target:
                r -= 1
            else:
                return [l+1, r+1]
        return []  

if __name__ == "__main__":
    numbers = [2,7,11,15]
    target = 9
    sol = Solution()
    res = sol.twoSum(numbers, target)
    print(res)                       