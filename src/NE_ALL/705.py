"""
LeetCode #705. Design HashSet

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
Design a HashSet without using built-in hash table libraries.

Implement:
- add(key)
- remove(key)
- contains(key)

Complexity
----------
Time  : O(1) average
Space : O(n)

Key Idea
--------
Use **hashing with buckets**.

- Compute bucket index using: key % bucket_size
- Each bucket stores keys in a list
- Handle collisions by storing multiple values in the same bucket
"""

from __future__ import annotations


class MyHashSet:
    """Simple HashSet using bucket lists."""

    def __init__(self) -> None:
        self.arr = [[] for _ in range(1000)]

    def add(self, key: int) -> None:
        index = key % len(self.arr)
        if not self.contains(key):
            self.arr[index].append(key)

    def remove(self, key: int) -> None:
        index = key % len(self.arr)
        if self.contains(key):
            self.arr[index].remove(key)

    def contains(self, key: int) -> bool:
        index = key % len(self.arr)
        return key in self.arr[index]


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    myHashSet = MyHashSet()

    myHashSet.add(1)
    myHashSet.add(2)

    assert myHashSet.contains(1) is True
    assert myHashSet.contains(3) is False

    myHashSet.add(2)
    assert myHashSet.contains(2) is True

    myHashSet.remove(2)
    assert myHashSet.contains(2) is False

    print("✅ All tests passed successfully!")
