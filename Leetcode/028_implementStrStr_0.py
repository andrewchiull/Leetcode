class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle == "":
        #     return 0
        # if needle not in haystack:
        #     return -1
        # for i in range(len(haystack)):
        #     if haystack[i:i+len(needle)] == needle:
        #         return i
        return haystack.find(needle)


sol = Solution()
print(f"Ans = {sol.strStr(haystack = 'hello', needle = 'll')}")
