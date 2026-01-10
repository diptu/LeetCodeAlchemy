"""
LeetCode #94 — Binary Tree Inorder Traversal

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
Given the root of a binary tree, return the inorder traversal
of its nodes' values.

Inorder traversal order:
    Left → Root → Right

Complexity
----------
Time  : O(n)
Space : O(h)   # recursion stack in the worst case-height/depth of the tree

Key Idea
--------
Use Depth-First Search (DFS).

Recursively:
1. Traverse left subtree
2. Visit current node
3. Traverse right subtree

Note
----
An iterative stack-based solution is also possible, but the
recursive approach is simpler and equally valid.
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
    """Perform inorder traversal of a binary tree."""

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:  # noqa: N802
        """
        Return the inorder traversal of a binary tree.

        Parameters
        ----------
        root : Optional[TreeNode]
            Root of the binary tree.

        Returns
        -------
        List[int]
            Inorder traversal of node values.
        """
        result: List[int] = []

        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return

            dfs(node.left)
            result.append(node.val)
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
    assert solution.inorderTraversal(root1) == [1, 3, 2]

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
    assert solution.inorderTraversal(root2) == [4, 2, 6, 5, 7, 1, 3, 9, 8]

    print("✅ All tests passed successfully!")
