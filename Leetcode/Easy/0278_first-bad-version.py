"""
278. First Bad Version
https://leetcode.com/problems/first-bad-version/

@Easy
@Algorithm
2022-03-24

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

1 500 1000
1 250 500
1 125 250
1 63 125
64 94 125
95 110 125
95 102 110
95 98 102
99 100 102
99 99 100
100 100
"""

# The isBadVersion API is already defined for you.


def isBadVersion(version: int) -> bool:
    return version >= 100

# v1 40.46%


class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n
        while low < high:
            mid = low + (high - low) // 2
            print(low, mid, high)
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        print(low, high)

        return high


sol = Solution()
print(f"{sol.firstBadVersion(1000) = }")
