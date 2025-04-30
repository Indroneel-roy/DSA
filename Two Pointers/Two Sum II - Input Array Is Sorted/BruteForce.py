#Problem  Link : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# using nested loop so time complexity O(n^2) and space complexity O(1)
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
        return []   

if __name__ == "__main__":
    numbers = [2,7,11,15]
    target = 9
    sol = Solution()
    res = sol.twoSum(numbers, target)
    print(res)         