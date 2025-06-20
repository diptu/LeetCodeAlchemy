import timeit


class Solution1:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False


class Solution2:
    def isPalindrome(self, x: int) -> bool:
        # Find the divisor to extract the leading digit
        div = 1
        while x // div >= 10:
            div *= 10

        while x != 0:
            left = x // div  # Leading digit
            right = x % 10  # Trailing digit

            if left != right:
                return False

            # Remove leading and trailing digits
            x = (x % div) // 10
            div = div // 100  # Because we removed two digits

        return True


def benchmark():
    sol1 = Solution1()
    sol2 = Solution2()
    test_value = 123454321

    t1 = timeit.timeit(lambda: sol1.isPalindrome(test_value), number=1000000)
    t2 = timeit.timeit(lambda: sol2.isPalindrome(test_value), number=1000000)

    print(f"Solution1: {t1:.6f} seconds for 1,000,000 runs")
    print(f"Solution2: {t2:.6f} seconds for 1,000,000 runs")


if __name__ == "__main__":
    benchmark()
