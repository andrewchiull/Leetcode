/*
944. Delete Columns to Make Sorted
https://leetcode.com/problems/delete-columns-to-make-sorted/

@Easy
@Array
@String

2022-01-03

You are given an array of `n` strings `strs`, all of the same length.

The strings can be arranged such that there is one on each line, making a grid. For example, `strs = ["abc", "bce", "cae"]` can be arranged as:

abc
bce
cae

You want to **delete** the columns that are **not sorted lexicographically**. In the above example (0-indexed), columns 0 (`'a'`, `'b'`, `'c'`) and 2 (`'c'`, `'e'`, `'e'`) are sorted while column 1 (`'b'`, `'c'`, `'a'`) is not, so you would delete column 1.

Return _the number of columns that you will delete_.
*/

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
   public:
    int minDeletionSize(vector<string>& strs) {
        int count = 0;
        int rowLen = strs.size();
        int colLen = strs[0].size();

        for (int col = 0; col < colLen; col++) {
            for (int row = 0; row < rowLen - 1; row++) {
                if (strs[row][col] > strs[row + 1][col]) {
                    count++;
                    break;
                }
            }
        }
        return count;
    }
};

int main() {
    Solution sol;

    vector<string> input{"cba", "daf", "ghi"};
    cout << sol.minDeletionSize(input) << '\n';
}
