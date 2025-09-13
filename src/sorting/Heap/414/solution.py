import heapq


class Solution:
    """Find the third maximum distinct number in a list using a heap."""

    def third_max(self, nums: list[int]) -> int:
        """
        Return the third distinct maximum number. If it does not exist,
        return the maximum number.

        Key Idea
        --------
        Use a min-heap of size at most 3. Iterate through distinct
        numbers, pushing each into the heap. If the heap exceeds size 3,
        pop the smallest element. At the end:
        - If heap size == 3, the smallest element is the third maximum.
        - Otherwise, return the maximum element in the heap.

        Parameters
        ----------
        nums : List[int]
            Input list of integers.

        Returns
        -------
        int
            The third maximum distinct number if it exists, otherwise
            the maximum.

        Complexity
        ----------
        Time:
            - Best: O(n) (iterate and push/pop limited elements)
            - Average: O(n)
            - Worst: O(n)
        Space:
            - Best/Average/Worst: O(1) (heap of at most 3 elements)

        Examples
        --------
        >>> solution = Solution()
        >>> solution.third_max([2, 2, 3, 1])
        1
        >>> solution.third_max([1, 2])
        2
        >>> solution.third_max([3, 2, 1])
        1
        >>> solution.third_max([5, 2, 2])
        5
        """
        min_heap: list[int] = []

        for num in set(nums):  # remove duplicates
            heapq.heappush(min_heap, num)
            if len(min_heap) > 3:
                heapq.heappop(min_heap)

        if len(min_heap) == 3:
            return min_heap[0]  # third maximum
        return max(min_heap)  # less than 3 unique numbers


if __name__ == "__main__":
    solution = Solution()
    nums: list[int] = [2, 2, 3, 1]

    print(f"nums={nums} -> third_max={solution.third_max(nums)}")
