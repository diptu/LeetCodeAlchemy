"""
LeetCode #412 — Fizz Buzz

Author: Nazmul Alam Diptu
--------------------------------------------------------

Implementation
--------------
**String** → O(log N) Time, O(1) Space
"""

from __future__ import annotations


class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer


if __name__ == "__main__":
    sol = Solution()
    # Basic test cases
    assert sol.fizzBuzz(n=3) == ["1", "2", "Fizz"]
    assert sol.fizzBuzz(n=5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert sol.fizzBuzz(n=15) == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
    ]

    print("✅ All tests passed successfully!")
