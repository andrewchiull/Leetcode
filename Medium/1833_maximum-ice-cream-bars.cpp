/*
1833. Maximum Ice Cream Bars
https://leetcode.com/problems/maximum-ice-cream-bars/

@Medium
@Array
@Greedy
@Sorting

It is a sweltering summer day, and a boy wants to buy some ice cream bars.

At the store, there are `n` ice cream bars. You are given an array `costs` of length `n`, where `costs[i]` is the price of the `i<sup>th</sup>` ice cream bar in coins. The boy initially has `coins` coins to spend, and he wants to buy as many ice cream bars as possible.

Return _the **maximum** number of ice cream bars the boy can buy with_ `coins` _coins._

**Note:** The boy can buy the ice cream bars in any order.

**Example 1:**

**Input:** costs = [1,3,2,4,1], coins = 7
**Output:** 4
**Explanation:** The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.
*/
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        int ans = 0;
        sort(costs.begin(), costs.end());
        for (const auto cost : costs) {
            if (coins >= cost) {
                ans++;
                coins -= cost;
            } else {
                break;
            }
        }

        return ans;
    }
};

int main(int argc, char const *argv[])
{
    Solution sol;
    vector<int> costs = {1,3,2,4,1};
    int coins = 7;
    cout << sol.maxIceCream(costs, coins); // 4
    cout << '\n';
    return 0;
}
