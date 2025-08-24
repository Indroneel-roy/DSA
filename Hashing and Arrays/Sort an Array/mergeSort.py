# Problem Link : https://leetcode.com/problems/sort-an-array/description/
from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(a, b):
            len_a = len(a)
            len_b = len(b)
            index_a, index_b = 0, 0
            merge_list = []
            while index_a < len_a and index_b < len_b:
                if a[index_a] < b[index_b]:
                    merge_list.append(a[index_a])
                    index_a += 1
                else:
                    merge_list.append(b[index_b]) 
                    index_b += 1
            if index_a < len_a:
                merge_list.extend(a[index_a :])
            elif index_b < len_b:
                merge_list.extend(b[index_b : ])  
            return merge_list      
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid : ])   
            return merge(left, right)                    
        return merge_sort(nums) 
if __name__ == "__main__":
    nums = [5,1,1,2,0,0]
    sol = Solution()
    print(sol.sortArray(nums))        