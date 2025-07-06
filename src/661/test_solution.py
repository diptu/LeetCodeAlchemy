"""
Unit tests for the imageSmoother method in the Solution class.

This module uses pytest to validate the behavior of the image smoothing algorithm,
ensuring correct average pixel calculations across various edge cases and inputs.
"""

import pytest
from solution import Solution


@pytest.fixture
def solution_instance():
    """
    Fixture to initialize and return a Solution instance.

    Returns
    -------
    Solution
        A new instance of the Solution class.
    """
    return Solution()


def test_example_1(solution_instance):
    """
    Test imageSmoother with a 3x3 image with varying values.

    Ensures that smoothing is correctly averaged over the 3x3 grid.
    """
    input_img = [
        [100, 200, 100],
        [200, 50, 200],
        [100, 200, 100],
    ]
    expected = [
        [137, 141, 137],
        [141, 138, 141],
        [137, 141, 137],
    ]
    result = solution_instance.imageSmoother(input_img)
    assert result == expected


def test_example_2(solution_instance):
    """
    Test imageSmoother with a 3x3 image containing a zero value.

    Checks that the function handles zeros correctly.
    """
    input_img = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ]
    expected = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    result = solution_instance.imageSmoother(input_img)
    assert result == expected


def test_single_pixel(solution_instance):
    """
    Test imageSmoother with a single pixel image.

    The output should match the input because there are no neighbors.
    """
    input_img = [[255]]
    expected = [[255]]
    result = solution_instance.imageSmoother(input_img)
    assert result == expected


def test_non_square_image(solution_instance):
    """
    Test imageSmoother on a non-square (3x2) image.

    Ensures averaging is done correctly for non-square matrices.
    """
    input_img = [
        [10, 20],
        [30, 40],
        [50, 60],
    ]
    expected = [
        [25, 25],
        [35, 35],
        [45, 45],
    ]
    result = solution_instance.imageSmoother(input_img)
    assert result == expected
