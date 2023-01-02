"""
704. Binary Search
https://leetcode.com/problems/binary-search/

@Easy
@Algorithm
2022-03-24

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

nums = [-1,0,3,5,9,12], target = 9

l h m
0 6 3 5>0
0 3 5 9=9

"""
from typing import List


# v0 27.58% recursive
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def _search(low: int, high: int) -> int:
            mid = (low + high) // 2
            print(low, mid, high)
            if low == high and nums[mid] != target:
                return -1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return _search(mid+1, high)
            elif nums[mid] > target:
                return _search(low, mid)

        return _search(0, len(nums)-1)


sol = Solution()
# print(f"{sol.search(nums = [-1,0,3,5,9,12], target = 9) = }")
# print(f"{sol.search(nums = [-1,0,3,5,9,12], target = 2) = }")
print(f"{sol.search(nums = [-1,0,3,5,9,12], target = 13) = }")


# v1 76.98% while
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (high - low) // 2 + low
            print(low, mid, high)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        print(low, high)
        return -1


sol = Solution()
print(f"{sol.search(nums = [-1,0,3,5,9,12], target = 9) = }")
print(f"{sol.search(nums = [-1,0,3,5,9,12], target = 2) = }")
print(f"{sol.search(nums = [-13], target = -13) = }")
