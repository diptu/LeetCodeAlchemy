"""
LeetCode #543 — Diameter of Binary Tree

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
Given the root of a binary tree, return the length of the diameter
of the tree.

The diameter of a binary tree is the length of the longest path
between any two nodes in a tree. This path may or may not pass
through the root.

The length of a path is measured by the number of edges between nodes.

Complexity
----------
Time  : O(n)
Space : O(h)   (recursive call stack, h = tree height)

Key Idea
--------
Use DFS to compute the height of each subtree.

At each node:
- Diameter passing through that node = left_height + right_height
- Keep track of the maximum diameter globally

The height of a node:
- 1 + max(left_height, right_height)

Note
----
Diameter is measured in number of edges, not nodes.
"""

from __future__ import annotations
from typing import Optional


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
    """Compute the diameter of a binary tree."""

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:  # noqa: N802
        """
        Return the diameter of the binary tree.

        Parameters
        ----------
        root : Optional[TreeNode]
            Root of the binary tree.

        Returns
        -------
        int
            Diameter of the tree (number of edges).
        """
        self.max_diameter = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # Update diameter at this node
            self.max_diameter = max(self.max_diameter, left_height + right_height)

            # Return height
            return 1 + max(left_height, right_height)

        dfs(root)
        return self.max_diameter


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    solution = Solution()

    # Tree: [1,2,3,4,5]
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    root1 = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3),
    )
    assert solution.diameterOfBinaryTree(root1) == 3

    # Tree: [1,2]
    #     1
    #    /
    #   2
    root2 = TreeNode(1, TreeNode(2))
    assert solution.diameterOfBinaryTree(root2) == 1

    # Single node
    root3 = TreeNode(1)
    assert solution.diameterOfBinaryTree(root3) == 0

    print("✅ All tests passed successfully!")
