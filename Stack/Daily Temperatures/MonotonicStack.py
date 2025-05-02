# Problem Link : https://leetcode.com/problems/daily-temperatures/description/
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = [] #[val : index]
        for i, val in enumerate(temperatures):
            while stack and stack[-1][0] < val :
                stackVal, stackIndex = stack.pop()
                output[stackIndex] = (i - stackIndex)
            stack.append([val, i])
        return output
if __name__ == "__main__":
    temperatures = [73,74,75,71,69,72,76,73]
    sol = Solution()
    res = sol.dailyTemperatures(temperatures)
    print(res)            