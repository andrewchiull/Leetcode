"""
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
"""


# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.dfs(root) if root is not None else []
    
    def dfs(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        temp = [root.val]
        if root.left is not None:
            temp.extend(self.dfs(root.left))
        if root.right is not None:
            temp.extend(self.dfs(root.right))
        return temp


class Solution:
    ans = []
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        self.ans.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.ans
    
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [] if not root else ([root.val]
                                    + self.preorderTraversal(root.left)
                                    + self.preorderTraversal(root.right))


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return ans
    

