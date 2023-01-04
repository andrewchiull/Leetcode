"""
2244. Minimum Rounds to Complete All Tasks
https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

Daily Challenge of 2022-01-04

@Medium

You are given a **0-indexed** integer array `tasks`, where `tasks[i]` represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the **same difficulty level**.

Return _the **minimum** rounds required to complete all the tasks, or_ `-1` _if it is not possible to complete all the tasks._

**Example 1:**

**Input:** tasks = [2,2,3,3,2,4,4,4,4,4]
**Output:** 4 (222,33,444,44)

"""

from typing import List
import collections

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        taskTable = collections.Counter(tasks)

        result = 0
        for count in taskTable.values():
            if count == 1:
                return -1
            result += (count+2) // 3
        return result

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = collections.Counter(tasks).values() 
        return -1 if (1 in freq) else sum((n+2) // 3 for n in freq)




sol = Solution()
tasks = [2,2,3,3,2,4,4,4,4,4]


print(f"{sol.minimumRounds(tasks)}")
