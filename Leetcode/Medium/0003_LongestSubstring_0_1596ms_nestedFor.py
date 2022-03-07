"""
0003
[Longest Substring Without Repeating Characters - LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
"""

from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        charTables: List[dict] = []
        charLengths: List[int] = []

        for i in range(len(s)):
            charTables.append({})
            charLengths.append(0)
            for j in range(i, len(s)):
                if s[j] not in charTables[i]:
                    charTables[i].update({s[j]: None})
                    charLengths[i] += 1
                else:
                    break
            print(f"{i:02} {s[i]}")
            print(charTables[i])
            print(charLengths[i])

        res = max(charLengths)
        return res


sol = Solution()
print(f"Ans = {sol.lengthOfLongestSubstring(s='abcabcbb')}")
