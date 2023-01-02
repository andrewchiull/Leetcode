"""
35. Search Insert Position
https://leetcode.com/problems/search-insert-position/

@Easy
@Algorithm
2022-03-24

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.


"""

# v1 66.95%

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high - low)//2
            print(low, mid, high)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        print(low, ' ', high)
        return low


sol = Solution()
print(f"{sol.searchInsert(nums = [-1,0,3,5,9,12], target = -13) = }")
print(f"{sol.searchInsert(nums = [-1,0,3,5,9,12], target = 13) = }")
print(f"{sol.searchInsert(nums = [-1], target = -13) = }")
print(f"{sol.searchInsert(nums = [-1], target = 13) = }")
