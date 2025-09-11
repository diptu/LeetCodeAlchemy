from __future__ import annotations


class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        """
        Split array into k subarrays to minimize the largest subarray sum.

        Uses binary search over the range [max(nums), sum(nums)] to find the
        minimal largest subarray sum such that the array can be split into at
        most k subarrays.

        Parameters
        ----------
        nums : list[int]
            The input array of positive integers.
        k : int
            The number of subarrays to split into.

        Returns
        -------
        int
            The minimized largest subarray sum.

        Notes
        -----
        Key Idea
        --------
        The answer lies between the maximum element (lower bound) and the
        total sum of the array (upper bound). Binary search is applied to
        test feasible largest sums via a greedy partitioning check.

        Time Complexity
        ---------------
        O(n log(sum(nums))), where n is the length of nums.

        Space Complexity
        ----------------
        O(1).

        Examples
        --------
        >>> sol = Solution()
        >>> sol.splitArray([7,2,5,10,8], 2)
        18
        >>> sol.splitArray([1,2,3,4,5], 2)
        9
        """

        def can_split(max_sum: int) -> bool:
            subarrays, current_sum = 1, 0
            for num in nums:
                if current_sum + num > max_sum:
                    subarrays += 1
                    current_sum = 0
                current_sum += num
                if subarrays > k:
                    return False
            return True

        low, high = max(nums), sum(nums)
        result = high

        while low <= high:
            mid = (low + high) // 2
            if can_split(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 5]
    k = 2
    print(sol.splitArray(nums, k))  # 9
