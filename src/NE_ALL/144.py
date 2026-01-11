"""
LeetCode #144 — Binary Tree Preorder Traversal

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
Given the root of a binary tree, return the preorder traversal
of its nodes' values.

Preorder traversal order:
    Root → Left → Right

Complexity
----------
Time  : O(n)
Space : O(n)   # recursion stack in the worst case

Key Idea
--------
Use Depth-First Search (DFS).

Recursively:
1. Visit current node
2. Traverse left subtree
3. Traverse right subtree


"""

from __future__ import annotations
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    """Binary tree node."""

    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Perform preorder traversal of a binary tree."""

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:  # noqa: N802
        """
        Return the preorder traversal of a binary tree.

        Parameters
        ----------
        root : Optional[TreeNode]
            Root of the binary tree.

        Returns
        -------
        List[int]
            Preorder traversal of node values.
        """
        result: List[int] = []

        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return

            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    solution = Solution()

    # Tree: [1, None, 2, 3]
    #     1
    #      \
    #       2
    #      /
    #     3
    root1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert solution.preorderTraversal(root1) == [1, 2, 3]

    # Tree: [1,2,3,4,5,None,8,None,None,6,7,9]
    root2 = TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(4),
            TreeNode(5, TreeNode(6), TreeNode(7)),
        ),
        TreeNode(
            3,
            None,
            TreeNode(8, TreeNode(9)),
        ),
    )
    assert solution.preorderTraversal(root2) == [1, 2, 4, 5, 6, 7, 3, 8, 9]

    print("✅ All tests passed successfully!")
