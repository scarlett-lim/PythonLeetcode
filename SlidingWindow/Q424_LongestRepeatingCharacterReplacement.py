class Solution:

    # # Time O(n)
    # # Space O(1)
    # def characterReplacement(self, s: str, k: int) -> int:
    #     count = {}
    #     res = 0
    #
    #     lp = 0
    #     for rp in range(len(s)):
    #         count[s[rp]] = 1 + count.get(s[rp], 0)
    #         if (rp-lp+1) - max(count.values()) > k:
    #             count[s[lp]] -= 1
    #             lp += 1
    #         res = max(res,rp-lp+1)
    #     return res


    # Time O(n)
    # Space O(1)
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        lp = 0
        maxFrequency = 0
        for rp in range(len(s)):
            count[s[rp]] = 1 + count.get(s[rp], 0)
            maxFrequency = max(maxFrequency, count[s[rp]])

            if (rp - lp + 1) - maxFrequency > k:
                count[s[lp]] -= 1
                lp += 1
            res = max(res, rp - lp + 1)
        return res



def run_tests():
    solution = Solution()

    # Test case 1
    args1 = ("ABAB", 2)  # Replace with actual inputs
    expected1 = 4  # Replace with expected output
    result1 = solution.characterReplacement(*args1)
    assert result1 == expected1, f"Test case 1 failed: expected {expected1}, got {result1}"

    # Test case 2
    args2 = ("AABABBA", 1)  # Replace with actual inputs
    expected2 = 4  # Replace with expected output
    result2 = solution.characterReplacement(*args2)
    assert result2 == expected2, f"Test case 2 failed: expected {expected2}, got {result2}"

    # # Test case 3
    # args3 = (input1, input2, ...)  # Replace with actual inputs
    # expected3 = expected_output2  # Replace with expected output
    # result3 = solution.solve(args3)
    # assert result3 == expected3, f"Test case 3 failed: expected {expected3}, got {result3}"

    # Add more test cases as needed
    print("All Q424 test cases passed!")


if __name__ == "__main__":
    run_tests()
