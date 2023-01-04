"""
290. Word Pattern
https://leetcode.com/problems/word-pattern/submissions/870887306/

Daily Challenge of 2022-01-01 (done on 2022-01-03)

@Easy
@Hash Table
@String

Given a `pattern` and a string `s`, find if `s` follows the same pattern.

Here **follow** means a full match, such that there is a bijection between a letter in `pattern` and a **non-empty** word in `s`.

**Example 1:**

**Input:** pattern = "abba", s = "dog cat cat dog"
**Output:** true
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        if len(pattern) != len(words):
            return False

        seenChars = dict()
        seenWords = dict()
        
        for char, word in zip(pattern, words):
            if char in seenChars and seenChars[char] != word:
                return False
            seenChars[char] = word

            if word in seenWords and seenWords[word] != char:
                return False
            seenWords[word] = char
        return True

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        if len(pattern) != len(words) or len(set(pattern)) != len(set(words)):
            return False

        seenChars = dict()
        for char, word in zip(pattern, words):
            if char in seenChars and seenChars[char] != word:
                return False
            seenChars[char] = word

        return True


from itertools import zip_longest

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        return (len(set(pattern)) 
                == len(set(s.split())) 
                == len(set(zip_longest(pattern, s.split())))
                )

# zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-

sol = Solution()
pattern = "abba"
s = "dog dog dog dog"

print(f"{sol.wordPattern(pattern, s)}")
