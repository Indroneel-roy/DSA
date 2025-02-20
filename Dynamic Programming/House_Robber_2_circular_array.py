class Solution:
    def rob(self, nums: List[int]) -> int:

        return max(nums[0], self.helper_fun(nums[1:]), self.helper_fun(nums[:-1]))


    def helper_fun(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            tem = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = tem
        return rob2  