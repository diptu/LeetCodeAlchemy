

class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        """
        Find all unique triplets in the array that sum up to zero.

        Parameters
        ----------
        nums : List[int]
            A list of integers.

        Returns
        -------
        List[List[int]]
            A list of unique triplets such that the sum of the
            elements in each triplet is zero.

        Examples
        --------
        >>> Solution().three_sum([-1, 0, 1, 2, -1, -4])
        [[-1, -1, 2], [-1, 0, 1]]

        Notes
        -----
        Time Complexity: O(n^2)
        Space Complexity: O(1) extra space (not counting output)
        """
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate `i`

            left, right = i + 1, len(nums) - 1

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result


if __name__ == "__main__":
    solution = Solution()
    nums_input = [-1, 0, 1, 2, -1, -4]
    print(solution.three_sum(nums_input))  # Output: [[-1, -1, 2], [-1, 0, 1]]
