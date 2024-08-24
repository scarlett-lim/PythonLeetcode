from typing import List


class Solution:

    # time o(n log n)
    # space o(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i : i[0])
        newList = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = newList[-1][1]
            if start <= lastEnd:
                newList[-1][1] = max(end,lastEnd)
            else:
                newList.append([start,end])

        return newList



def run_tests():
    solution = Solution()

    # Test case 1
    args1 = [[1, 3], [2, 6], [8, 10], [15, 18]]  # Replace with actual inputs
    expected1 = [[1, 6], [8, 10], [15, 18]]  # Replace with expected output
    result1 = solution.merge(args1)
    assert result1 == expected1, f"Test case 1 failed: expected {expected1}, got {result1}"

    # Test case 2
    args2 = [[1, 4], [4, 5]]  # Replace with actual inputs
    expected2 = [[1, 5]]  # Replace with expected output
    result2 = solution.merge(args2)
    assert result2 == expected2, f"Test case 2 failed: expected {expected2}, got {result2}"

    # Add more test cases as needed
    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
