/*
2244. Minimum Rounds to Complete All Tasks
https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

Daily Challenge of 2022-01-04

@Medium

You are given a **0-indexed** integer array `tasks`, where `tasks[i]` represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the **same difficulty level**.

Return _the **minimum** rounds required to complete all the tasks, or_ `-1` _if it is not possible to complete all the tasks._

**Example 1:**

**Input:** tasks = [2,2,3,3,2,4,4,4,4,4]
**Output:** 4 (222,33,444,44)
*/

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int minimumRounds(vector<int>& tasks) {
        unordered_map<int,int> mp;
        for (auto task : tasks) {
            auto it = mp.find(task);
            if (it != mp.end()) {
                it->second++;
            }
            else {
                mp[task] = 1;
            }
        }
        
        int result = 0;

        for (auto it : mp) {
            if (it.second == 1) {
                return -1;
            }
            result += (it.second + 2) / 3; 
        }
        return result;
    }
};

int main() {

    Solution sol;
    vector<int> tasks = {2,2,3,3,2,4,4,4,4,4};
    cout << sol.minimumRounds(tasks);
    cout << '\n';
    return 0;
}

/*
[dictionary - How to find if a given key exists in a C++ std::map - Stack Overflow](https://stackoverflow.com/questions/1939953/how-to-find-if-a-given-key-exists-in-a-c-stdmap)

m.count(key) > 0
m.count(key) == 1
m.count(key) != 0

OR

auto it = m.find("key");
if (it != m.end()) {
    it->second; // The value
}
*/