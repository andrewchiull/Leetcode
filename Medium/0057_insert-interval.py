"""
57. Insert Interval
https://leetcode.com/problems/insert-interval/

DC of 2023-01-16

@Medium

@Array


You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]` represent the start and the end of the `i<sup>th</sup>` interval and `intervals` is sorted in ascending order by `start<sub>i</sub>`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `start<sub>i</sub>` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` _after the insertion_.

**Example 1:**

**Input:** intervals = [[1,3],[6,9]], newInterval = [2,5]
**Output:** [[1,5],[6,9]]

**Example 2:**

**Input:** intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
**Output:** [[1,2],[3,10],[12,16]]
**Explanation:** Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        N = len(intervals)
        for i in range(N):
            if intervals[i][1] < p:
                continue
            elif intervals[i][1] == p:
                pass
            
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        p, q = newInterval

        ans: List[List[int]] = list()
        END = 1 + max(intervals[-1][1], q) # newInterval might be longer
        flags = [0] * END

        # Convert the intervals to the flags
        for interval in intervals:
            a, b = interval
            flags[a:b] = [1] * (b-a)

            # Edge cases: zero length interval
            if a == b and (a not in range(p, q)):
                ans.append(interval)

        # Convert the newInterval to the flags
        flags[p:q] = [1] * (q-p)


        # Edge cases
        if p == q:
            # newInterval IS in one of the intervals
            if flags[p] or (flags[p-1] and not flags[p]):
                return intervals
            else: # newInterval is NOT in one of the intervals
                intervals.append(newInterval)
                return sorted(intervals)

        # Convert reversely from the flags to the intervals
        a, b = 0, 0
        for i in range(END):
            if flags[i-1] == 0 and flags[i] == 1: 
                # flags[-1] must == flage[END] == 0
                a = i
            elif flags[i-1] == 1 and flags[i] == 0:
                b = i
                ans.append([a, b])
                a, b = 0, 0

        return sorted(ans)


# [7+ lines, 3 easy solutions - Insert Interval - LeetCode](https://leetcode.com/problems/insert-interval/solutions/21622/7-lines-3-easy-solutions/?orderBy=most_votes)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval[0], newInterval[1]
        left, right = [], []
        for i in intervals:
            if i[1] < s:
                left += i,
            elif i[0] > e:
                right += i,
            else:
                s = min(s, i[0])
                e = max(e, i[1])
        return left + [[s, e]] + right

sol = Solution()
# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# newInterval = [4,8]
intervals = [[1,5]]
newInterval = [0,0]
print(sol.insert(intervals, newInterval))