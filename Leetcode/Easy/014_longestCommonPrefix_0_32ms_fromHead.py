from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        i = 0
        while(True):
            try:
                for j in range(len(strs)):
                    if strs[0][i] != strs[j][i]:
                        return prefix
                prefix += strs[0][i]
                i += 1
            except IndexError:
                break
        return prefix


sol = Solution()
# _input = ["dog", "racecar", "car"]
_input = ["flower", "flow", "flight"]
print(f"{_input} = {sol.longestCommonPrefix(_input)}")
