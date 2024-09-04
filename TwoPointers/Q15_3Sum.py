from typing import List


class Solution:

    # time O(N2)
    # space O(1)/O(N)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, value in enumerate(nums):
            # prevent using same value for 1st number
            if i > 0 and value == nums[i-1]:
                continue
            lp, rp = i+1, len(nums)-1
            while lp < rp:
                if nums[lp]+nums[rp]+value == 0:
                    result.append([value,nums[lp],nums[rp]])
                    # prevent using duplicate value for left pointer
                    lp += 1
                    while nums[lp] == nums[lp-1] and lp<rp:
                        lp += 1
                elif nums[lp]+nums[rp]+value < 0:
                    lp += 1
                else:
                    rp -= 1
        return result


def run_tests():
    solution = Solution()

    # Test case 1
    args1 = [-1,0,1,2,-1,-4]  # Replace with actual inputs
    expected1 = [[-1,-1,2],[-1,0,1]]  # Replace with expected output
    result1 = solution.threeSum(args1)
    assert result1 == expected1, f"Test case 1 failed: expected {expected1}, got {result1}"

    # Test case 2
    args2 = [0,1,1] # Replace with actual inputs
    expected2 = []  # Replace with expected output
    result2 = solution.threeSum(args2)
    assert result2 == expected2, f"Test case 2 failed: expected {expected2}, got {result2}"

    # Test case 3
    args3 = [0,0,0]  # Replace with actual inputs
    expected3 = [[0,0,0]]  # Replace with expected output
    result3 = solution.threeSum(args3)
    assert result3 == expected3, f"Test case 3 failed: expected {expected3}, got {result3}"

    # Add more test cases as needed
    print("All Q15 test cases passed!")


if __name__ == "__main__":
    run_tests()
