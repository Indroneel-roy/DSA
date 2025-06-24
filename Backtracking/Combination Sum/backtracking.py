# problem link : https://leetcode.com/problems/combination-sum/
from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            print(f"dfs(i={i}, cur={cur}, total={total})")  # 👈 Step trace

            if total == target:
                print(f" Found: {cur}")
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                print(f" Stop: i={i}, total={total}")
                return

            # 👉 Include nums[i]
            cur.append(nums[i])
            print(f"Choose {nums[i]}, cur={cur}")
            dfs(i, cur, total + nums[i])
            cur.pop()
            print(f" Backtrack after choosing {nums[i]}, cur={cur}")

            # 👉 Skip nums[i]
            print(f" Skip {nums[i]}, move to index {i+1}")
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

# Run the example
sol = Solution()
output = sol.combinationSum(nums = [2,3,6,7], target = 7)
print("\n All Combinations:", output)
