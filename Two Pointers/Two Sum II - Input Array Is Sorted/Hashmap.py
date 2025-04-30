#Problem  Link : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# using hash map concept so time complexity reduce to O(n) and space complexity O(n) because a hash map is call to store index of each value
from typing import List
from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash = defaultdict(int)
        for i in range(len(numbers)):
            tem = target - numbers[i]
            if hash[tem]:
                return [hash[tem], i + 1]
            hash[numbers[i]] = i + 1
        return []    

if __name__ == "__main__":
    numbers = [2,7,11,15]
    target = 9
    sol = Solution()
    res = sol.twoSum(numbers, target)
    print(res)             