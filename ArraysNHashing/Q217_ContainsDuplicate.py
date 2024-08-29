from typing import List


class Solution:

    # Time Space O(N)
    def containsDuplicate(self, nums: List[int]) -> bool:
        numberSet = set()

        for i in nums:
            if i in numberSet:
                return True
            numberSet.add(i)
        return False



def run_tests():
    solution = Solution()

    # Test case 1
    args1 = [1,2,3,1] # Replace with actual inputs
    expected1 = True  # Replace with expected output
    result1 = solution.containsDuplicate(args1)
    assert result1 == expected1, f"Test case 1 failed: expected {expected1}, got {result1}"

    # Test case 2
    args2 = [1,2,3,4]  # Replace with actual inputs
    expected2 = False  # Replace with expected output
    result2 = solution.containsDuplicate(args2)
    assert result2 == expected2, f"Test case 2 failed: expected {expected2}, got {result2}"

    # Test case 3
    args3 = [1,1,1,3,3,4,3,2,4,2] # Replace with actual inputs
    expected3 = True  # Replace with expected output
    result3 = solution.containsDuplicate(args3)
    assert result3 == expected3, f"Test case 2 failed: expected {expected3}, got {result3}"

    # Add more test cases as needed
    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
