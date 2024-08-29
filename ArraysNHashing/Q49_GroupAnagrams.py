from collections import defaultdict
from typing import List


class Solution:
    # Time Spcae O(m*n)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
            dictionary[tuple(count)].append(word)

        return dictionary.values()









        # res = defaultdict(list) # handle edge case to make the default dict to list
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c)-ord("a")] +=1
        #     # put tuple bcuz list cnt be key in dictionary
        #     res[tuple(count)].append(s)
        #
        # return res.values()



def run_tests():
    solution = Solution()

    # Test case 1
    args1 = ["eat","tea","tan","ate","nat","bat"]  # Replace with actual inputs
    expected1 = [["bat"],["nat","tan"],["ate","eat","tea"]]  # Replace with expected output
    result1 = solution.groupAnagrams(args1)
    assert result1 == expected1, f"Test case 1 failed: expected {expected1}, got {result1}"

    # Test case 2
    args2 = [""]  # Replace with actual inputs
    expected2 = [[""]]  # Replace with expected output
    result2 = solution.groupAnagrams(args2)
    assert result2 == expected2, f"Test case 2 failed: expected {expected2}, got {result2}"

    # Test case 3
    args3 = ["a"]  # Replace with actual inputs
    expected3 = [["a"]]  # Replace with expected output
    result3 = solution.groupAnagrams(args3)
    assert result3 == expected3, f"Test case 3 failed: expected {expected3}, got {result3}"

    # Add more test cases as needed
    print("All Q49 test cases passed!")


if __name__ == "__main__":
    run_tests()
