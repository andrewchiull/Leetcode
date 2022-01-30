class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0
        for i in range(len(s)-1):
            thisChar = mapping[s[i]]
            if thisChar < mapping[s[i+1]]:
                res -= thisChar
            else:
                res += thisChar
        res += mapping[s[-1]]
        return res


sol = Solution()
_input = input("input: ")
print(f"{_input} = {sol.romanToInt(_input)}")
