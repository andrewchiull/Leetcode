/*
144. Binary Tree Preorder Traversal
https://leetcode.com/problems/binary-tree-preorder-traversal/

Daily Challenge of 2023-01-09

@Easy

@Stack
@Tree
@Depth-First Search
@Binary Tree

Given the `root` of a binary tree, return _the preorder traversal of its nodes' values_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)

**Input:** root = [1,null,2,3]
**Output:** [1,2,3]
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

#include <iostream>
#include <vector>
#include <stack>
#include <string>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
 
class Solution {
public:
    vector<int> ans;
    vector<int> preorderTraversal(TreeNode* root) {
        if (!root) return ans;
        ans.push_back(root->val);
        preorderTraversal(root->left);
        preorderTraversal(root->right);
        return ans;
    }
};

class Solution {
public:
    vector<int> ans;
    vector<int> preorderTraversal(TreeNode* root) {
        if (!root) return ans;
        stack<TreeNode*> st;
        st.push(root);
        while (!st.empty()) {
            TreeNode* node = st.top();
            st.pop();
            ans.push_back(node->val);
            if (node->right) {
                st.push(node->right);
            }
            if (node->left) {
                st.push(node->left);
            }
        }
        return ans;
    }
};


// Morris Traversal
// [✅[C++] EASY|| Beats100% || 3 Approach With explaination✅ - Binary Tree Preorder Traversal - LeetCode](https://leetcode.com/problems/binary-tree-preorder-traversal/solutions/3022021/c-easy-beats100-3-approach-with-explaination/)
// [Morris Traversal方法遍历二叉树（非递归，不用栈，O(1)空间](https://blog.csdn.net/u013007900/article/details/77663733)

class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ans;
        if (!root) return ans;
        while (root) {
            if (!root->left) { // if root.left IS null
                ans.push_back(root->val); // Record root.val
                root = root->right; // Let root.right be the new root
            } else { // if root.left is NOT null

                // Let predecessor be the right-most children in the left tree of current root
                TreeNode* pre = root->left;
                while (pre->right && (pre->right != root)) {
                    // (When pre->right == root, we need to restore the tree as the "else" below)
                    pre = pre->right;
                }

                if (!pre->right) { // if pre.right IS null
                    ans.push_back(root->val); // Record root.val

                    pre->right = root; // Point pre.right to the root
                    root = root->left; // Let root.left be the new root
                } else { // if pre.right is NOT null <=> pre.right == root
                    root = root->right; // Let root.right be the new root
                    pre->right = nullptr; // Restore the tree
                }
            }
        }
        return ans;
    }
};