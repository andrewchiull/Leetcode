"""
374. Guess Number Higher or Lower
https://leetcode.com/problems/guess-number-higher-or-lower/

@Easy
@Algorithm
2022-03-24

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
"""

# v1 85.18%

pick = 10


def guess(num: int) -> int:
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:

        low, high = 1, n
        while low <= high:
            mid = low + (high - low) // 2
            guess_ans = guess(mid)
            print(low, mid, high, guess_ans)
            if guess_ans == 0:
                return mid
            elif guess_ans == -1:
                high = mid - 1
            elif guess_ans == 1:
                low = mid + 1


sol = Solution()
print(f"{sol.guessNumber(100) = }")
