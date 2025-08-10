# test_max_product.py
"""
Pytest unit tests for the Solution class in max_product module.

Covers:
- Positive numbers
- Negative numbers
- Mixed positives and negatives
- Arrays containing zeros
- Single-element arrays
"""

import pytest
from solution import Solution


@pytest.fixture
def solver():
    """Fixture providing a Solution instance."""
    return Solution()


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 3, -2, 4], 6),  # Simple case: product from [2,3]
        ([-2, 0, -1], 0),  # Contains zero, max is 0
        ([-2, 3, -4], 24),  # Negative product becomes positive
        ([0, 0, 0], 0),  # All zeros
        ([5], 5),  # Single positive
        ([-5], -5),  # Single negative
        ([2, -5, -2, -4, 3], 24),  # Multiple negatives
        ([1, 2, 3, 4], 24),  # All positive
        ([2, -3, 0, -2, -40], 80),  # Reset after zero
    ],
)
def test_max_product(solver, nums, expected):
    """Test max_product with various input arrays."""
    assert solver.max_product(nums) == expected
