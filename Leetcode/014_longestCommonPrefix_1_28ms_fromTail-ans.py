from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in strs[1:]:
            while i[:len(prefix)] != prefix and prefix:
                prefix = prefix[:len(prefix)-1]
        return prefix


sol = Solution()
# _input = ["dog", "racecar", "car"]
_input = ["flower", "flow", "flight"]
print(f"{_input} = {sol.longestCommonPrefix(_input)}")
