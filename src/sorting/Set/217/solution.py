class Solution:
    """Check if a list contains duplicates."""

    # ----------------------------
    # Active solution: one-liner
    # ----------------------------
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Return True if the list contains duplicates using a one-liner set check.

        Parameters
        ----------
        nums : List[int]
            Input list of integers.

        Returns
        -------
        bool
            True if duplicates exist, False otherwise.

        Complexity
        ----------
        Time: O(n) average
        Space: O(n)
        """
        return len(nums) != len(set(nums))

    # ----------------------------
    # Commented-out solution: loop + set
    # ----------------------------
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     """
    #     Return True if the list contains duplicates using a set and loop.
    #
    #     Parameters
    #     ----------
    #     nums : List[int]
    #         Input list of integers.
    #
    #     Returns
    #     -------
    #     bool
    #         True if duplicates exist, False otherwise.
    #
    #     Complexity
    #     ----------
    #     Time: O(n) average
    #     Space: O(n)
    #     """
    #     seen: set[int] = set()
    #     for num in nums:
    #         if num in seen:
    #             return True
    #         seen.add(num)
    #     return False


if __name__ == "__main__":
    solution = Solution()

    nums_example1: list[int] = [1, 2, 3, 4]
    nums_example2: list[int] = [1, 2, 3, 1]

    print(solution.containsDuplicate(nums_example1))
    print(solution.containsDuplicate(nums_example2))
