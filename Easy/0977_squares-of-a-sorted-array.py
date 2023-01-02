"""
977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/

@Easy
@Algorithm

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""
from typing import List


# v1 58.01%


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([n**2 for n in nums])


# v2


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = list()
        left, right = 0, len(nums) - 1
        for _ in range(len(nums)):
            if abs(nums[left]) <= abs(nums[right]):
                index = right
                right -= 1
            else:
                index = left
                left += 1
            res.insert(0, nums[index]**2)
        return res


sol = Solution()
print(f"{sol.sortedSquares(nums = [-4,-1,0,3,10]) = }")
print(f"{sol.sortedSquares(nums = [-4, -2, 0]) = }")
