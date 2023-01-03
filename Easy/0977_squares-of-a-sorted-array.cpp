/*
977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/

@Easy
@Algorithm

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution {
   public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> res(nums.size());
        int l = 0, r = nums.size() - 1;
        for (int i = nums.size() - 1; i >= 0; i--) {
            if (abs(nums[l]) > abs(nums[r])) {
                res[i] = nums[l] * nums[l];
                l++;
            } else {
                res[i] = nums[r] * nums[r];
                r--;
            }
        }
        return res;
    }
    void sortedSquares(int nums[], int size) {
        vector<int> res(size);
        int l = 0, r = size - 1;
        for (int i = size - 1; i >= 0; i--) {
            if (abs(nums[l]) > abs(nums[r])) {
                res[i] = nums[l] * nums[l];
                l++;
            } else {
                res[i] = nums[r] * nums[r];
                r--;
            }
        }
        copy(res.begin(), res.end(), nums);
    }
};

int main() {
    Solution sol;

    vector<int> nums{10, 2, 30};
    nums = sol.sortedSquares(nums);

    for (int x : nums) {
        cout << x << " ";
    }
    cout << "\n";

    int nums_array[] = {10, 2, 30};
    int size = (sizeof(nums_array) / sizeof(nums_array[0]));
    sol.sortedSquares(nums_array, size);

    for (int x : nums_array) {
        cout << x << " ";
    }
    cout << "\n";
    return 0;
}
