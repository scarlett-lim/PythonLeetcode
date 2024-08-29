from typing import List


class Solution:
    # Dictionary
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in dictionary:
                return [dictionary[complement], i]
            dictionary[num] = i



if __name__ == '__main__':
    solution = Solution()

    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    expected1 = [0, 1]
    result1 = solution.two_sum(nums1, target1)
    assert result1 == expected1, f"Test case 1 failed: expected {expected1}, got {result1}"

    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    expected2 = [1, 2]
    result2 = solution.two_sum(nums2, target2)
    assert result2 == expected2, f"Test case 2 failed: expected {expected2}, got {result2}"

    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    expected3 = [0, 1]
    result3 = solution.two_sum(nums3, target3)
    assert result3 == expected3, f"Test case 3 failed: expected {expected3}, got {result3}"

    print("All Q1 test cases passed!")