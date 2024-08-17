from typing import List


class Solution:

    # Sorting
    # Time : O(n log n)
    # Space : O(1)
    # def missingNumber(self, nums: List[int]) -> int:
    #     nums.sort()
    #
    #     for value in range(len(nums)):
    #         if value != nums[value]:
    #             return value
    #
    #     return len(nums)


    # Set
    # O(n)
    # def missingNumber(self, nums: List[int]) -> int:
    #     numSet = set(nums)
    #
    #     for i in range(len(nums)+1):
    #         if i not in numSet:
    #             return i

    # Find the sum of range and nums then minus
    # Time O(n)
    # Space O(1)
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)

        for i in range(len(nums)):
            result += (i - nums[i])
        return result

def run_tests():
    solution = Solution()

    # Test case 1
    args1 = [3,0,1] # Replace with actual inputs
    expected1 = 2  # Replace with expected output
    result1 = solution.missingNumber(args1)
    assert result1 == expected1, f"Test case 1 failed: expected {expected1}, got {result1}"

    # Test case 2
    args2 = [0,1]  # Replace with actual inputs
    expected2 = 2  # Replace with expected output
    result2 = solution.missingNumber(args2)
    assert result2 == expected2, f"Test case 2 failed: expected {expected2}, got {result2}"

    # Test case 3
    args3 = [9,6,4,2,3,5,7,0,1]  # Replace with actual inputs
    expected3 = 8  # Replace with expected output
    result3 = solution.missingNumber(args3)
    assert result3 == expected3, f"Test case 3 failed: expected {expected3}, got {result3}"

    # Add more test cases as needed
    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
