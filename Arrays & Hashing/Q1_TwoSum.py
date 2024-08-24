from typing import List


class Solution:
    # Brute force/nested for loop
    # def two_sum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i]+nums[j] == target:
    #                 return [i,j]
    #     return []


    # Dictionary
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        # dictionary = {}
        # index = 0
        # for item in range(len(nums)):
        #     complement = target - nums[item]
        #     if dictionary.__contains__(complement):
        #         return[dictionary[complement], item]
        #     else:
        #         dictionary[nums[item]] = index
        #         index += 1
        # return []
        # Create a dictionary to store the complement and its index
        num_to_index = {}

        # Iterate over the list
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num

            # If the complement is in the dictionary, return the indices
            if complement in num_to_index:
                return [num_to_index[complement], i]

            # Otherwise, store the index of the current number
            num_to_index[num] = i
        return []



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

    # Test case 4
    nums3 = [3, 2]
    target3 = 6
    expected3 = []
    result3 = solution.two_sum(nums3, target3)
    assert result3 == expected3, f"Test case 3 failed: expected {expected3}, got {result3}"
    print("All test cases passed!")