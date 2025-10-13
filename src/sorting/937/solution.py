from typing import List, Tuple


class Solution:
    """
    Provides a beginner-friendly, step-by-step implementation to reorder log files
    according to LeetCode 937.

    Key Idea
    --------
    1. Split each log into `identifier` and `content`.
    2. Determine if the log is a letter-log or digit-log.
    3. Sort letter-logs by content first, then by identifier.
    4. Digit-logs remain in original order and appear after all letter-logs.

    Time Complexity
    ---------------
    O(n log n) — sorting letter-logs.

    Space Complexity
    ----------------
    O(n) — temporary storage for letter-logs and digit-logs.

    Example
    -------
    >>> sol = Solution()
    >>> sol.reorder_log_files([
    ...     "dig1 8 1 5 1",
    ...     "let1 art can",
    ...     "dig2 3 6",
    ...     "let2 own kit dig",
    ...     "let3 art zero"
    ... ])
    ['let1 art can', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6']
    """

    def reorder_log_files(self, logs: List[str]) -> List[str]:
        """Beginner-friendly step-by-step reorder of logs."""

        # Step 1: Separate letter-logs and digit-logs
        letter_logs: List[str] = []
        digit_logs: List[str] = []

        for log in logs:
            identifier, content = log.split(" ", 1)  # split into two parts
            if content[0].isdigit():
                # It's a digit-log → keep original order
                digit_logs.append(log)
            else:
                # It's a letter-log → will sort later
                letter_logs.append(log)

        # Step 2: Define sort key for letter-logs
        def sort_key(log: str) -> Tuple[str, str]:
            identifier, content = log.split(" ", 1)
            return (content, identifier)  # sort by content, then identifier

        # Step 3: Sort the letter-logs
        letter_logs.sort(key=sort_key)

        # Step 4: Combine letter-logs and digit-logs
        return letter_logs + digit_logs


if __name__ == "__main__":
    sol = Solution()

    # ✅ Example test
    logs_input = [
        "dig1 8 1 5 1",
        "let1 art can",
        "dig2 3 6",
        "let2 own kit dig",
        "let3 art zero",
    ]
    print(sol.reorder_log_files(logs_input))
    # Output: ['let1 art can', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6']

    # ✅ Additional test cases
    assert sol.reorder_log_files(["d1 2 3", "d2 4 5"]) == ["d1 2 3", "d2 4 5"]
    assert sol.reorder_log_files(["a1 act car", "b2 act zoo", "a2 act car"]) == [
        "a1 act car",
        "a2 act car",
        "b2 act zoo",
    ]
    assert sol.reorder_log_files(["a1 abc def", "b1 abc def", "c1 1 2"]) == [
        "a1 abc def",
        "b1 abc def",
        "c1 1 2",
    ]

    print("All tests passed ✅")
