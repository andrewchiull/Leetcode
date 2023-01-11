/*
452. Minimum Number of Arrows to Burst Balloons
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

Daily Challenge of 2023-01-05

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
*/

#include <iostream>
#include <limits>
#include <vector>
using namespace std;

// class Solution {
// public:
//     static bool comp (const vector<int> &a, const vector<int> &b) {
//         return a[1] < b[1];
//     }
//     int findMinArrowShots(vector<vector<int>>& points) {
//         // int rMax = -(int)numeric_limits<double>::infinity(); // HOTFIX not working
//         // int rMax = -std::numeric_limits<int>::max();

//         sort(points.begin(), points.end(), comp);
//         int rMax = INT_MIN;
//         int ans = 0;

//         for (const auto point : points)
//         {
//             if (point[0] > rMax) {
//                 ans++;
//                 rMax = point[1];
//             }
//         }

//         return ans;
//     }
// };

class Solution {
   public:
    int findMinArrowShots(vector<vector<int>>& points) {
        vector<pair<int, int>> v;
        for (int i = 0; i < points.size(); i++) {
            v.push_back(make_pair(points[i][1], points[i][0])); // sort by right
        }
        sort(v.begin(), v.end());

        int ans = 1;
        int max = v[0].first;
        for (int i = 1; i < v.size(); i++) {
            if (v[i].second > max) {
                max = v[i].first;
                ans++;
            }
        }

        return ans;
    }
};

int main() {
    Solution sol;
    vector<vector<int>> points = {{1, 2}, {2, 3}, {3, 4}, {4, 5}};  // 2
    cout << sol.findMinArrowShots(points);
    return 0;
}