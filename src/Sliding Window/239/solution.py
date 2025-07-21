"""Module for solving sliding window maximum using a monotonic deque."""

from collections import deque
from typing import List


class Solution:
    """A class containing array-related sliding window solutions."""

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Return the maximum value in each sliding window of size `k`.

        This uses a deque (monotonic decreasing queue) to efficiently track
        the maximum values in each window as the window slides across the list.

        Parameters
        ----------
        nums : List[int]
            The input list of integers.
        k : int
            The size of the sliding window.

        Returns
        -------
        List[int]
            A list of the maximums for each window.

        Examples
        --------
        >>> sol = Solution()
        >>> sol.max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)
        [3, 3, 5, 5, 6, 7]
        Time Complexity
        ---------------
        O(n), where n is the length of `nums`. Each element is added and removed from
        the deque at most once.

        Space Complexity
        ----------------
        O(k), where k is the window size. This is the maximum size of the deque at any time.
        """
        result = []
        dq = deque()

        for i in range(len(nums)):
            # Remove indices outside the current window
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # Maintain decreasing order in deque
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Append max value to result once the window is full
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result


if __name__ == "__main__":
    SOLUTION = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    RESULT = SOLUTION.maxSlidingWindow(nums, k)
    print(RESULT)  # [3,3,5,5,6,7]
