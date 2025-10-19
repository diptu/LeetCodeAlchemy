from typing import List


class Solution:
    """
    Optimal greedy solution for LeetCode 853 — Car Fleet.

    Intuition
    ---------
    Sort cars by position in descending order and compute the time
    each car needs to reach the target. Iterate from the car closest
    to the target to the farthest:
      - If a car’s arrival time is greater than the current fleet time,
        it starts a new fleet.
      - Otherwise, it joins the fleet ahead.

    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """

    def car_fleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """Return the number of fleets that reach the target."""
        if not position:
            return 0

        # Sort cars by position descending (closer cars first)
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        current_time = 0.0

        for pos, spd in cars:
            time = (target - pos) / spd
            # A new fleet forms only if this car arrives later
            if time > current_time:
                fleets += 1
                current_time = time

        return fleets


if __name__ == "__main__":
    sol = Solution()

    # ✅ Example test cases
    assert sol.car_fleet(10, [3], [3]) == 1
    assert sol.car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
    assert sol.car_fleet(10, [6, 8], [3, 2]) == 2
    assert sol.car_fleet(100, [0, 2, 4], [4, 2, 1]) == 1

    print("All tests passed ✅")
