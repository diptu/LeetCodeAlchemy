"""
Benchmark different implementations.
"""

import random
import timeit


def product_except_self_original(nums: list[int]) -> list[int]:
    """
    Compute the product of all elements except self using
    left and right prefix arrays.

    Parameters
    ----------
    nums : List[int]
        Input list of integers.

    Returns
    -------
    List[int]
        Product array except self.
    """
    length = len(nums)
    left_to_right = [1] * length
    prefix_sum = 1
    for i in range(1, length):
        prefix_sum *= nums[i - 1]
        left_to_right[i] = prefix_sum

    right_to_left = [1] * length
    prefix_sum = 1
    for i in range(length - 2, -1, -1):
        prefix_sum *= nums[i + 1]
        right_to_left[i] = prefix_sum

    result = [1] * length
    for i in range(length):
        result[i] = left_to_right[i] * right_to_left[i]

    return result


def product_except_self_optimized(nums: list[int]) -> list[int]:
    """
    Optimized version that computes product except self using only one result array.

    Parameters
    ----------
    nums : List[int]
        Input list of integers.

    Returns
    -------
    List[int]
        Product array except self.
    """
    length = len(nums)
    result = [1] * length

    prefix = 1
    for i in range(length):
        result[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(length - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result


def benchmark():
    """
    Run time benchmarks for both implementations and print the results.
    """
    test_input = [random.randint(1, 10) for _ in range(1000)]

    original_time = timeit.timeit(
        lambda: product_except_self_original(test_input), number=100
    )
    optimized_time = timeit.timeit(
        lambda: product_except_self_optimized(test_input), number=100
    )

    print(f"Original solution time:  {original_time:.4f} seconds")
    print(f"Optimized solution time: {optimized_time:.4f} seconds")


if __name__ == "__main__":
    benchmark()
