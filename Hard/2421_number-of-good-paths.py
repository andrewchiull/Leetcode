"""
2421. Number of Good Paths
https://leetcode.com/problems/number-of-good-paths/

Daily Challenge of 2023-01-15

@Hard

@Array
@Tree
@Union Find
@Graph


There is a tree (i.e. a connected, undirected graph with no cycles) consisting of `n` nodes numbered from `0` to `n - 1` and exactly `n - 1` edges.

You are given a **0-indexed** integer array `vals` of length `n` where `vals[i]` denotes the value of the `i<sup>th</sup>` node. You are also given a 2D integer array `edges` where `edges[i] = [a<sub>i</sub>, b<sub>i</sub>]` denotes that there exists an **undirected** edge connecting nodes `a<sub>i</sub>` and `b<sub>i</sub>`.

A **good path** is a simple path that satisfies the following conditions:

1. The starting node and the ending node have the **same** value.
2. All nodes between the starting node and the ending node have values **less than or equal to** the starting node (i.e. the starting node's value should be the maximum value along the path).

Return _the number of distinct good paths_.

Note that a path and its reverse are counted as the **same** path. For example, `0 -> 1` is considered to be the same as `1 -> 0`. A single node is also considered as a valid path.

**Example 1:**

![](https://assets.leetcode.com/uploads/2022/08/04/f9caaac15b383af9115c5586779dec5.png)

**Input:** vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]
**Output:** 6
**Explanation:** There are 5 good paths consisting of a single node.
There is 1 additional good path: 1 -> 0 -> 2 -> 4.
(The reverse path 4 -> 2 -> 0 -> 1 is treated as the same as 1 -> 0 -> 2 -> 4.)
Note that 0 -> 2 -> 3 is not a good path because vals[2] > vals[0].
"""

from collections import defaultdict
import math
from typing import List

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        uf = dict()

        def find(p):
            uf.setdefault(p, p)
            while p != uf[p]:
                uf[p] = uf[uf[p]]
                p = uf[p]
            return p
        
        def union(p, q):
            uf[find(q)] = find(p)

        adjacents = defaultdict(list)
        val2Nodes = defaultdict(set)
        for p, q in edges:
            adjacents[p].append(q)
            adjacents[q].append(p)
            val2Nodes[vals[p]].add(p)
            val2Nodes[vals[q]].add(q)

        
        ans = len(vals)

        # Process the nodes of the increasing same value
        for val in sorted(val2Nodes.keys()):
            sameVals = val2Nodes[val]
            # print(f"{val=}")

            # Connect the nodes to make "good paths"
            for node in sameVals:
                for adj in adjacents[node]:
                    if vals[adj] <= val:
                        union(adj, node)

            # Count connected nodes of the current val
            connectedCounter = defaultdict(int)
            for node in sameVals:
                connectedCounter[find(node)] += 1

            # Count combinations of the connected nodes
            for root in connectedCounter.keys():
                ans += math.comb(connectedCounter[root], 2) # v * (v-1) / 2

        return ans


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        N = len(vals)
        uf = list(range(N))
        rank = [1] * N

        def find(p):
            while p != uf[p]:
                uf[p] = uf[uf[p]]
                p = uf[p]
            return p
        
        ans = N

        # Sort by which edge has the largest val of p or q
        edges.sort(key=lambda x: max(vals[x[0]], vals[x[1]]))

        connectedCounter = defaultdict(int)

        # Process the nodes of the increasing same value
        for a, b in edges:
            rootA, rootB = find(a), find(b)
            valA, valB = vals[rootA], vals[rootB]

            if valA == valB:
                uf[rootB] = rootA
                
                # Add new combinations of the connected nodes
                ans += rank[rootA] * rank[rootB]

                rank[rootA] += rank[rootB]
            elif valA > valB:
                uf[rootB] = rootA
            else: # valA < valB
                uf[rootA] = rootB

        return ans