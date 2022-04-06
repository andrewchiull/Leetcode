"""
https://leetcode.com/problems/contains-duplicate/
217. Contains Duplicate
@Easy
@DataStructure
2022-03-35

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

"""

# v1 74.80%

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        record = set()
        for num in nums:
            if num in record:
                return True
            record.add(num)
        return False


sol = Solution()
print(f"{sol.containsDuplicate(nums = [-1,0,3,5,9,12]) = }")
print(f"{sol.containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]) = }")


# v2 96.75%

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)


sol = Solution()
print(f"{sol.containsDuplicate(nums = [-1,0,3,5,9,12]) = }")
print(f"{sol.containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]) = }")
