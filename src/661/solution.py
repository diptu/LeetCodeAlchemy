

class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        """
        Smooths an image represented as a 2D grid by averaging each pixel
        with its neighboring pixels in a 3x3 window.

        Parameters
        ----------
        img : List[List[int]]
            A 2D list of integers where each integer represents the grayscale
            value of a pixel (0 to 255).

        Returns
        -------
        List[List[int]]
            A new 2D list representing the smoothed image. Each pixel is
            replaced with the average of its neighbors (including itself),
            rounded down to the nearest integer.

        Notes
        -----
        - Edge and corner pixels are smoothed using only the available neighbors.
        - The input image is not modified; a new image is returned.

        Complexity
        ----------
        Time complexity : O(m * n)
            Each pixel is visited once, and for each pixel, at most 9 neighbors
            are inspected in constant time.

        Space complexity : O(m * n)
            A new matrix of the same size as the input is created to store results.
        Examples
        --------
        >>> solution = Solution()
        >>> solution.imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        >>> solution.imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]])
        [[133, 133, 133], [133, 133, 133], [133, 133, 133]]
        """
        rows, cols = len(img), len(img[0])
        res = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                pixel_sum = 0
                pixel_count = 0

                # Iterate through the 3x3 neighborhood
                for i in range(max(0, r - 1), min(rows, r + 2)):
                    for j in range(max(0, c - 1), min(cols, c + 2)):
                        pixel_sum += img[i][j]
                        pixel_count += 1

                res[r][c] = pixel_sum // pixel_count

        return res


if __name__ == "__main__":
    solution = Solution()
    # Example 1
    result1 = solution.imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]])
    print(f"Result for example 1:\n{result1}")
    # Expected: [[137, 141, 137], [141, 138, 141], [137, 141, 137]]

    # Example 2
    result2 = solution.imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    print(f"Result for example 2:\n{result2}")
    # Expected: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
