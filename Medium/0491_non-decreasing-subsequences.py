"""
491. Non-decreasing Subsequences
https://leetcode.com/problems/non-decreasing-subsequences/
DC 2023-01-20

@Medium

@Array
@Hash Table
@Backtracking
@Bit Manipulation

Given an integer array `nums`, return _all the different possible non-decreasing subsequences of the given array with at least two elements_. You may return the answer in **any order**.

**Example 1:**

**Input:** nums = [4,6,7,7]
**Output:** [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

**Example 2:**

**Input:** nums = [4,4,3,2,1]
**Output:** [[4,4]]
"""

from typing import List
import math

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ans = list()
        for i in range(2**N):
            subSequence = list()
            binary = f"{i:0{N}b}"
            # print(binary)
            for j, digit in enumerate(binary):
                if digit == '1':
                    subSequence.append(nums[j])
            # print(subSequence)
            if (len(subSequence) > 1
                and subSequence == sorted(subSequence)
                and subSequence not in ans):
                ans.append(subSequence)
        return ans


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subs: set[tuple] = {()}
        for num in nums:
            subs |= {sub + (num,) # |= is union
                    for sub in subs
                    if not sub or sub[-1] <= num}
        return [sub for sub in subs if len(sub) >= 2]

sol = Solution()
print(sol.findSubsequences([4,6,7,7]))
