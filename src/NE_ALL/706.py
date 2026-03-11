from __future__ import annotations


class MyHashMap:
    def __init__(self):
        # Constraints: 0 <= key, value <= 10^6
        # We need size 1,000,001 to accommodate the key 1,000,000
        self.data = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        """Sets the value for the given key."""
        self.data[key] = value

    def get(self, key: int) -> int:
        """Returns the value to which the specified key is mapped, or -1 if no mapping exists."""
        return self.data[key]

    def remove(self, key: int) -> None:
        """Removes the mapping for the specific key if it exists."""
        self.data[key] = -1


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    myHashMap = MyHashMap()

    # Basic Operations
    myHashMap.put(1, 1)
    myHashMap.put(2, 2)
    assert myHashMap.get(1) == 1
    assert myHashMap.get(3) == -1  # Not found

    # Update Existing Key
    myHashMap.put(2, 1)
    assert myHashMap.get(2) == 1

    # Removal
    myHashMap.remove(2)
    assert myHashMap.get(2) == -1

    # Edge Case: Max Constraint
    myHashMap.put(1000000, 50)
    assert myHashMap.get(1000000) == 50

    print("✅ All tests passed successfully!")
