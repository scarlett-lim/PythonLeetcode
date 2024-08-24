from typing import List


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # lambda arguments: expression
        # arguments = The input parameters to the function, similar to parameters in a regular function.
        # expression = A single expression that is evaluated and returned.
        # i = arguments = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
        # i.start mean the start time for each pair in i
        intervals.sort(key = lambda i:i.start)

        for item in range(1,len(intervals)):
            if intervals[item].start < intervals[item-1].end:
                return False
        return True


def run_tests():
    solution = Solution()

    # # Test case 1: Overlapping intervals
    # args1 = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
    # expected1 = False
    # result1 = solution.can_attend_meetings(args1)
    # assert result1 == expected1, f"Test case 1 failed: expected {expected1}, got {result1}"

    # Test case 2
    args2 = [Interval(5, 8), Interval(9, 15)]  # Replace with actual inputs
    expected2 = True  # Replace with expected output
    result2 = solution.can_attend_meetings(args2)
    assert result2 == expected2, f"Test case 2 failed: expected {expected2}, got {result2}"

    # Test case 3: Single interval
    args3 = [Interval(5, 10)]
    expected3 = True
    result3 = solution.can_attend_meetings(args3)
    assert result3 == expected3, f"Test case 3 failed: expected {expected3}, got {result3}"

    # Test case 4: Empty list of intervals
    args4 = []
    expected4 = True
    result4 = solution.can_attend_meetings(args4)
    assert result4 == expected4, f"Test case 4 failed: expected {expected4}, got {result4}"

    # Add more test cases as needed
    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
