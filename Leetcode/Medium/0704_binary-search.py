"""
633. Sum of Square Numbers
https://leetcode.com/problems/sum-of-square-numbers/

@Medium

Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

2022-04-23
"""
from math import sqrt


# v0
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a_max = int(sqrt(c/2))
        print(a_max)
        for a in range(a_max + 1):
            # print(a)
            if sqrt(c - a * a) % 1 == 0:
                return True
        return False


sol = Solution()
print(f"{sol.judgeSquareSum(c = 9) = }")
print(f"{sol.judgeSquareSum(c = 8) = }")
