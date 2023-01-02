"""
0003
[Longest Substring Without Repeating Characters - LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
"""

from pprint import pprint
from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subStr = ""
        maxLen = 0

        for _s in s:
            if _s in subStr:
                subStr = subStr.split(_s)[1]
            subStr += _s
            maxLen = max(maxLen, len(subStr))
            print(subStr)
        return maxLen


sol = Solution()
print(f"Ans = {sol.lengthOfLongestSubstring(s='abcca')}")
