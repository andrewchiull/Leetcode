"""
1. Two Sum
https://leetcode.com/problems/two-sum/
@Easy
@HashSet_HashMap

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


# In[1]:


from typing import List


# # 1: Too slow

# In[2]:


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index in range(len(nums)):
            for interval in range(1, len(nums) - index):
                if nums[index] + nums[index + interval] == target:
                    return [index, index + interval]

# # 2: Wrong
#

# In[3]:


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = []
        for num in nums:
            if num in diffs and diffs.index(num) < num.index(num):
                # if there are repeated values, ls.index(elem) will return the index of the first elem
                return [diffs.index(num), num.index(num)]
            diffs.append(target - num)

# # 3: OK
#

# In[4]:


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = []
        for index, num in enumerate(nums):
            if num in diffs and diffs.index(num) < index:
                return [diffs.index(num), index]
            diffs.append(target - num)

# # Sol: Use HashMap
#
# - Runtime: 60 ms, faster than 76.38% of Python3 online submissions for Two Sum.
# - Memory Usage: 15.4 MB, less than 20.38% of Python3 online submissions for Two Sum.
#

# In[5]:


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], index]
            seen[num] = index
