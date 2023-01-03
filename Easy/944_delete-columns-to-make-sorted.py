"""
944. Delete Columns to Make Sorted
https://leetcode.com/problems/delete-columns-to-make-sorted/

@Easy
@Array
@String

2022-01-03

You are given an array of `n` strings `strs`, all of the same length.

The strings can be arranged such that there is one on each line, making a grid. For example, `strs = ["abc", "bce", "cae"]` can be arranged as:

abc
bce
cae

You want to **delete** the columns that are **not sorted lexicographically**. In the above example (0-indexed), columns 0 (`'a'`, `'b'`, `'c'`) and 2 (`'c'`, `'e'`, `'e'`) are sorted while column 1 (`'b'`, `'c'`, `'a'`) is not, so you would delete column 1.

Return _the number of columns that you will delete_.
"""


from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for col in range(len(strs[0])):
            for row in range(len(strs) - 1):
                if strs[row][col] > strs[row+1][col]:
                    count += 1
                    print
                    break
        return count


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum((list(col) != sorted(col)) for col in zip(*strs))

sol = Solution()

_input = ["cba","daf","ghi"]
print(f"{_input} -> {sol.minDeletionSize(_input)}")