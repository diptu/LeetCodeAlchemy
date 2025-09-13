import heapq


class Solution:
    """Find the k-th largest element in a list using a heap."""

    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        Return the k-th largest element from the list using a MinHeap
        of size k for efficiency.

        Key Idea
        --------
        Maintain a MinHeap of size k containing the k largest elements.
        Iterate through the numbers:
        - If the heap has fewer than k elements, push the number.
        - Otherwise, if the current number is larger than the heap root,
          replace the root with the current number.
        The root of the heap after processing all numbers is the k-th
        largest element.

        Parameters
        ----------
        nums : List[int]
            Input list of integers.
        k : int
            The rank of the largest element to find (1-based).

        Returns
        -------
        int
            The k-th largest element.

        Raises
        ------
        ValueError
            If k <= 0 or k > len(nums).

        Complexity
        ----------
        Time:
            - Best/Average/Worst: O(n log k)
        Space:
            - O(k) for the heap

        Examples
        --------
        >>> solution = Solution()
        >>> solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
        4
        >>> solution.findKthLargest([1, 2, 2, 3], 2)
        2
        """
        min_heap: list[int] = []

        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            elif num > min_heap[0]:
                heapq.heapreplace(min_heap, num)

        return min_heap[0]


if __name__ == "__main__":
    solution = Solution()
    nums: list[int] = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k: int = 4
    result = solution.findKthLargest(nums, k)
    print(f"nums={nums} -> {k}_th_largest={result}")
