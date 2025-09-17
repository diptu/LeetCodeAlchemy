from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        """
        Assign relative ranks to athletes based on their scores.

        Key idea
        --------
        - Use counting sort–like strategy:
          * Find max score.
          * Build a direct mapping of score -> index.
          * Iterate scores from high to low to assign ranks.
        - This avoids sorting and heaps.

        Parameters
        ----------
        score : List[int]
            A list of unique scores for each athlete.

        Returns
        -------
        List[str]
            A list of ranks/medals in the same order as the input.

        Examples
        --------
        >>> sol = Solution()
        >>> sol.findRelativeRanks([10, 3, 8, 9, 4])
        ['Gold Medal', '5', 'Bronze Medal', 'Silver Medal', '4']

        Time Complexity
        ---------------
        O(n + m), where n = number of athletes and
        m = max(score). Usually O(n) if m ~ n.

        Space Complexity
        ----------------
        O(m), for the score-to-index array.
        """
        n: int = len(score)
        max_score: int = max(score)

        # Initialize with -1 (meaning no athlete with that score)
        score_to_idx: List[int] = [-1] * (max_score + 1)
        for idx, val in enumerate(score):
            score_to_idx[val] = idx

        print(score_to_idx)
        result: List[str] = [""] * n
        rank: int = 1

        # Iterate scores from high to low
        for val in range(max_score, -1, -1):
            idx: int = score_to_idx[val]
            if idx == -1:
                continue

            if rank == 1:
                result[idx] = "Gold Medal"
            elif rank == 2:
                result[idx] = "Silver Medal"
            elif rank == 3:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(rank)

            rank += 1

        return result


if __name__ == "__main__":
    solution = Solution()
    sample_scores = [10, 3, 8, 9, 4]
    print(solution.findRelativeRanks(sample_scores))
    # ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
