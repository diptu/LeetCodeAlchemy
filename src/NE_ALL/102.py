"""
LeetCode #102 — Binary Tree Level Order Traversal (Recursive)

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
Given the root of a binary tree, return the level order traversal
of its nodes' values (left to right, level by level).

Complexity
----------
Time  : O(n)
Space : O(n)   # recursion stack + result storage

Key Idea
--------
Use Depth-First Search (DFS) with level tracking.

- Pass the current depth (level) during recursion
- Create a new list in the result when visiting a level
  for the first time
- Append node values to their corresponding level list

Note
----
Although level-order traversal is naturally solved using BFS,
this DFS approach is equally correct and often asked as a
follow-up to test recursion depth handling.
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
    """Perform level-order traversal of a binary tree using recursion."""

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:  # noqa: N802
        """
        Return the level-order traversal of a binary tree.

        Parameters
        ----------
        root : Optional[TreeNode]
            Root of the binary tree.

        Returns
        -------
        List[List[int]]
            Node values grouped by depth level.
        """
        result: List[List[int]] = []

        def dfs(node: Optional[TreeNode], level: int) -> None:
            if node is None:
                return

            # Create a new level if it does not exist
            if level == len(result):
                result.append([])

            result[level].append(node.val)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
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
    assert solution.levelOrder(root1) == [[1], [2], [3]]

    # Tree: [1,2,3,4,5,6,7]
    root2 = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, TreeNode(6), TreeNode(7)),
    )
    assert solution.levelOrder(root2) == [[1], [2, 3], [4, 5, 6, 7]]

    print("✅ All tests passed successfully!")
