from typing import List


class Solution:

    # Time : O(n2)
    # Space : O(n)
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     for i in range(len(numbers)-1):
    #         for j in range(i+1,len(numbers)):
    #             if numbers[i] + numbers[j] == target:
    #                 return [i+1,j+1]
    #
    #     return []

    # Time : On
    # Space : O1
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp, rp = 0, len(numbers)-1

        while lp<rp:
            if numbers[lp]+numbers[rp] == target:
                return [lp+1, rp+1]
            elif numbers[lp]+numbers[rp] > target:
                rp -= 1
            else:
                lp += 1

        return []


def run_tests():
    solution = Solution()

    # Test case 1
    args1 = [2, 7, 11, 15], 9  # Replace with actual inputs
    expected1 = [1, 2]  # Replace with expected output
    result1 = solution.twoSum(*args1)
    assert result1 == expected1, f"Test case 1 failed: expected {expected1}, got {result1}"

    # Test case 2
    args2 = [2, 3, 4], 6  # Replace with actual inputs
    expected2 = [1, 3]  # Replace with expected output
    result2 = solution.twoSum(*args2)
    assert result2 == expected2, f"Test case 2 failed: expected {expected2}, got {result2}"

    # Test case 3
    args3 = [-1, 0], -1  # Replace with actual inputs
    expected3 = [1, 2]  # Replace with expected output
    result3 = solution.twoSum(*args3)
    assert result3 == expected3, f"Test case 3 failed: expected {expected3}, got {result3}"

    # Add more test cases as needed
    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
