

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        N = len(nums)
        left, right = 0, N - 1
        result = [0] * N
        pos = right

        while left <= right:
            left_element = nums[left] * nums[left]
            right_element = nums[right] * nums[right]
            if left_element < right_element:
                result[pos] = right_element
                pos -= 1
        return result


if __name__ == "__main__":
    solution = Solution()
    nums = [-4, -1, 0, 3, 10]
    print(solution.sortedSquares(nums))  # [0,1,9,16,100]
