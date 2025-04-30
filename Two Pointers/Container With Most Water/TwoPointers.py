#problem link : https://leetcode.com/problems/container-with-most-water/description/
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # brute force solution
        # maxArea = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         area = min(height[i], height[j]) * (j-i)
        #         maxArea = max(area, maxArea)
        # return maxArea      

        maxArea = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = min(height[l], height[r]) * (r-l)
            maxArea = max(maxArea, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea              
if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    sol = Solution()
    res = sol.maxArea(height)
    print(res)