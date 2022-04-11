"""
189. Rotate Array
https://leetcode.com/problems/rotate-array/

@Medium
@Algorithm

Given an array, rotate the array to the right by k steps, where k is non-negative.
"""
from typing import List


# v1 63.86%, 79.96%
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        shift = (len(nums) - k) % len(nums)
        nums[:] = nums[shift:] + nums[:shift]
        print(nums)


sol = Solution()
sol.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=10)


# v2 Time Limit Exceeded
# O(n * k) in time, O(1) in space
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for _ in range(k % len(nums)):
            for i in range(len(nums)):
                nums[i], nums[-1] = nums[-1], nums[i]
        print(nums)


sol = Solution()
sol.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=10)


# v3 87.96%, 79.96%
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = [None] * len(nums)
        for i in range(len(nums)):
            temp[(i+k) % len(nums)] = nums[i]
        nums[:] = temp
        print(nums)


sol = Solution()
sol.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=10)


# v4 Using Cyclic Replacements
# Time complexity : O(n). Only one pass is used.
# Space complexity : O(1). Constant extra space is used.
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        count = 0
        start_idx = 0
        while count < len(nums):
            current_idx = start_idx
            temp = nums[current_idx]
            while True:
                # print(temp)
                next_idx = (current_idx + k) % len(nums)
                temp, nums[next_idx] = nums[next_idx], temp
                current_idx = next_idx
                count += 1
                if next_idx == start_idx:
                    start_idx += 1
                    break
        print(nums)


sol = Solution()
sol.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=10)


# v5 Using Reverse
# Time complexity : O(n). n elements are reversed a total of three times.
# Space complexity : O(1). No extra space is used.
# Original List                   : 1 2 3 4 5 6 7
# After reversing all numbers     : 7 6 5 4 3 2 1
# After reversing first k numbers : 5 6 7 4 3 2 1
# After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums.reverse()
        nums[:] = list(reversed(nums[:k])) + list(reversed(nums[k:]))
        # self.reverse(nums, 0, k-1)
        # self.reverse(nums, k, len(nums)-1)
        print(nums)

    def reverse(self, nums: List[int], start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


sol = Solution()
sol.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=10)
