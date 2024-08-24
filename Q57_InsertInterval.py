from typing import List


class Solution:

    # Time O(n log n)
    # Space O(n)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda i: i[0])
        newList = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = newList[-1][1]
            if start <= lastEnd:
                newList[-1][1] = max(lastEnd,end)
            else:
                newList.append([start,end])

        return newList


    # Time O(n2)
    # Space O(n)
    # def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #     for i in range(len(intervals)):
    #         if intervals[i][0] < newInterval[0]:
    #             if i == len(intervals) - 1:
    #                 intervals.append(newInterval)
    #                 break
    #             continue
    #         else:
    #             intervals.insert(i, newInterval)
    #
    #     if not intervals:
    #         intervals.append(newInterval)
    #
    #     newList = [intervals[0]]
    #
    #     for start, end in intervals[1:]:
    #         lastEnd = newList[-1][1]
    #         if start <= lastEnd:
    #             newList[-1][1] = max(lastEnd, end)
    #         else:
    #             newList.append([start, end])
    #
    #     return newList


def run_tests():
    solution = Solution()

    # Test case 1
    args1 = ([[1, 3], [6, 9]], [2, 5])  # Replace with actual inputs
    expected1 = [[1, 5], [6, 9]]  # Replace with expected output
    result1 = solution.insert(*args1)
    assert result1 == expected1, f"Test case 1 failed: expected {expected1}, got {result1}"

    # Test case 2
    args2 = ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])  # Replace with actual inputs
    expected2 = [[1, 2], [3, 10], [12, 16]]  # Replace with expected output
    result2 = solution.insert(*args2)
    assert result2 == expected2, f"Test case 2 failed: expected {expected2}, got {result2}"

    # Test case 3
    args3 = ([[1,5]], [2,7])  # Replace with actual inputs
    expected3 = [[1,7]]  # Replace with expected output
    result3 = solution.insert(*args3)
    assert result3 == expected3, f"Test case 3 failed: expected {expected3}, got {result3}"

    # Test case 4
    args4 = ([], [2, 7])  # Replace with actual inputs
    expected4 = [[2, 7]]  # Replace with expected output
    result4 = solution.insert(*args4)
    assert result4 == expected4, f"Test case 4 failed: expected {expected4}, got {result4}"

    # Add more test cases as needed
    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
