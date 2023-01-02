"""
0003
[Longest Substring Without Repeating Characters - LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
"""

from pprint import pprint
from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        charTable: dict[str, int] = {}
        start: int = 0
        maxLength: int = 1

        for i in range(len(s)):
            if s[i] not in charTable:
                charTable.update({s[i]: i})
            else:
                start = max(start, charTable[s[i]] + 1)
                charTable[s[i]] = i
            length = i - start + 1
            print(f"{i:02} {s[i]} {start:02} {length} ", end="")
            pprint(charTable)
            maxLength = max(maxLength, length)

        return maxLength


sol = Solution()
print(f"Ans = {sol.lengthOfLongestSubstring(s='abcca')}")
