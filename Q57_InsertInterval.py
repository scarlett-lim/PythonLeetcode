from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Implement the solution for the specific LeetCode problem here.
        Adjust the method name and parameters as needed based on the problem statement.
        """
        pass


def run_tests():
    solution = Solution()

    # Test case 1
    args1 = ([[1,3],[6,9]],[2,5])  # Replace with actual inputs
    expected1 = [[1,5],[6,9]]  # Replace with expected output
    result1 = solution.insert(*args1)
    assert result1 == expected1, f"Test case 1 failed: expected {expected1}, got {result1}"

    # Test case 2
    args2 = ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])  # Replace with actual inputs
    expected2 = [[1,2],[3,10],[12,16]]  # Replace with expected output
    result2 = solution.insert(*args2)
    assert result2 == expected2, f"Test case 2 failed: expected {expected2}, got {result2}"

    # Add more test cases as needed
    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
