

class Solution:
    """Class to solve majority element problem."""

    def majorityElement(self, nums: list[int]) -> int:
        """
        Find the majority element in an array.

        Key Idea
        --------
        Approach 1 (Active): Use `collections.Counter` to count frequency
        of each element. Since the majority element always exists, return
        the one appearing more than n // 2 times.

        Approach 2 (Commented): Use Boyer–Moore Voting Algorithm to find
        the majority element in O(1) extra space.

        Parameters
        ----------
        nums : List[int]
            A list of integers.

        Returns
        -------
        int
            The majority element (appearing more than n/2 times).

        Time Complexity
        ---------------
        Best Case: O(n)
        Average Case: O(n)
        Worst Case: O(n)

        Space Complexity
        ----------------
        Counter Approach: O(k), where k = number of distinct elements
        Boyer–Moore Approach: O(1)
        """
        # # -------- Counter-based Solution (Active) --------
        # n: int = len(nums)
        # freq_map: Counter[int] = Counter(nums)

        # for element, count in freq_map.items():
        #     if count > n // 2:
        #         return element

        # -------- Boyer–Moore Solution (Optimized, O(1) space) --------
        candidate: int = nums[0]
        count: int = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate


if __name__ == "__main__":
    solution = Solution()
    nums_example: list[int] = [2, 2, 1, 1, 1, 2, 2]
    print(solution.majorityElement(nums_example))  # 1
