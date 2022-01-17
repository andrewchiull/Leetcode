class Solution:
    def romanToInt(self, s: str) -> int:
        replacement = {
            'IV': 'a',
            'IX': 'b',
            'XL': 'c',
            'XC': 'd',
            'CD': 'e',
            'CM': 'f'
        }
        mapping = {
            'I': 1,
            'a': 5-1,
            'V': 5,
            'b': 10-1,
            'X': 10,
            'c': 50-10,
            'L': 50,
            'd': 100-10,
            'C': 100,
            'e': 500-100,
            'D': 500,
            'f': 1000-100,
            'M': 1000
        }
        for k, v in replacement.items():
            s = s.replace(k, v)
        print(s)
        res = 0
        for i in s:
            res += mapping[i]
        return res


sol = Solution()
_input = input("input: ")
print(f"{_input} = {sol.romanToInt(_input)}")
