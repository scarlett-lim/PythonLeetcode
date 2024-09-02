class Solution:

    # Time Space : O(n)
    def isValid(self, s: str) -> bool:
        pair = {'}': '{', ']': '[', ')': '('}
        stack = []

        if not s:
            return False

        for item in s:
            if item in pair:
                if stack and stack[-1] == pair[item]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)

        return not stack


def run_tests():
    solution = Solution()

    # Test case 1
    args1 = "()"  # Replace with actual inputs
    expected1 = True  # Replace with expected output
    result1 = solution.isValid(args1)
    assert result1 == expected1, f"Test case 1 failed: expected {expected1}, got {result1}"

    # Test case 2
    args2 = "()[]{}"  # Replace with actual inputs
    expected2 = True  # Replace with expected output
    result2 = solution.isValid(args2)
    assert result2 == expected2, f"Test case 2 failed: expected {expected2}, got {result2}"

    # Test case 3
    args3 = "(]"  # Replace with actual inputs
    expected3 = False  # Replace with expected output
    result3 = solution.isValid(args3)
    assert result3 == expected3, f"Test case 3 failed: expected {expected3}, got {result3}"

    # Test case 4
    args4 = "(])"  # Replace with actual inputs
    expected4 = False  # Replace with expected output
    result4 = solution.isValid(args4)
    assert result4 == expected4, f"Test case 3 failed: expected {expected4}, got {result4}"

    # Add more test cases as needed
    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
