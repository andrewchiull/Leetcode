"""
452. Minimum Number of Arrows to Burst Balloons
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

@Medium

@Array
@Greedy
@Sorting


There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array `points` where `points[i] = [x<sub>start</sub>, x<sub>end</sub>]` denotes a balloon whose **horizontal diameter** stretches between `x<sub>start</sub>` and `x<sub>end</sub>`. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up **directly vertically** (in the positive y-direction) from different points along the x-axis. A balloon with `x<sub>start</sub>` and `x<sub>end</sub>` is **burst** by an arrow shot at `x` if `x<sub>start</sub> <= x <= x<sub>end</sub>`. There is **no limit** to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array `points`, return _the **minimum** number of arrows that must be shot to burst all balloons_.

**Example 1:**

**Input:** points = [[10,16],[2,8],[1,6],[7,12]]
**Output:** 2
**Explanation:** The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
"""


from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        N = len(points)
        if N == 1:
            return 1
        points = sorted(points)
        ans = N
        rMin = points[0][1]
        for l, r in points[1:]:
            if l <= rMin:
                ans -= 1
                rMin = min(r, rMin)
            else:
                rMin = r
        return ans

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)
        rMin = float('inf')
        ans = 1
        for l, r in points:
            if l > rMin:
                ans += 1
                rMin = r
            rMin = min(r, rMin)
        return ans

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1]) # sort backwards
        rMax = -float('inf')
        ans = 0
        for l, r in points:
            if l > rMax:
                ans += 1
                rMax = r
        return ans

sol = Solution()
points = [[10,16],[2,8],[1,6],[7,12]] # 2
points = [[1,2],[3,4],[5,6],[7,8]] # 4
points = [[1,2],[2,3],[3,4],[4,5]] # 2


print(f"{sol.findMinArrowShots(points)}")
