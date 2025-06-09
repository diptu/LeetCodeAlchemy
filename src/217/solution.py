

class Solution:
    """
    Solution class to check if a list contains any duplicates.

    Methods
    -------
    contains_duplicate(nums: List[int]) -> bool
        Returns True if the input list contains any duplicate elements,
        otherwise returns False.
    """

    @staticmethod
    def contains_duplicate(nums: list[int]) -> bool:
        """
        Check if the input list contains any duplicates.

        Parameters
        ----------
        nums : List[int]
            A list of integers to check for duplicates.

        Returns
        -------
        bool
            True if duplicates exist in the list, False otherwise.

        Examples
        --------
        >>> Solution.contains_duplicate([1, 2, 3, 1])
        True
        >>> Solution.contains_duplicate([1, 2, 3, 4])
        False
        """
        return len(nums) != len(set(nums))
