from typing import Optional

from Module.ListNodeClass import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Implement the solution for the specific LeetCode problem here.
        Adjust the method name and parameters as needed based on the problem statement.
        """
        pass

def createLinkList(List[int]):


def run_tests():
    solution = Solution()

    # Test case 1
    args1 = [1,2,3,4,5]  # Replace with actual inputs
    expected1 = [5,4,3,2,1]  # Replace with expected output
    result1 = solution.reverseList(args1)
    assert result1 == expected1, f"Test case 1 failed: expected {expected1}, got {result1}"

    # Test case 2
    args2 = [1,2]  # Replace with actual inputs
    expected2 = [2,1]  # Replace with expected output
    result2 = solution.reverseList(args2)
    assert result2 == expected2, f"Test case 2 failed: expected {expected2}, got {result2}"

    # Test case 3
    args3 = []  # Replace with actual inputs
    expected3 = []  # Replace with expected output
    result3 = solution.solve(args3)
    assert result3 == expected3, f"Test case 3 failed: expected {expected3}, got {result3}"

    # Add more test cases as needed
    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
