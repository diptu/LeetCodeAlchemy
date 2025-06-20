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
        x = str(x)

        if x == x[::-1]:
            return True
        else:
            return False


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
