class Solution:

    # Time space O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        lp = 0
        maxCount = 0
        longestSet = set()

        for rp in range(len(s)):
            while s[rp] in longestSet:
                longestSet.remove(s[lp])
                lp += 1
            longestSet.add(s[rp])
            maxCount = max(maxCount,len(longestSet))
        return maxCount


def run_tests():
    solution = Solution()

    # Test case 1
    args1 = "abcabcbb"  # Replace with actual inputs
    expected1 = 3  # Replace with expected output
    result1 = solution.lengthOfLongestSubstring(args1)
    assert result1 == expected1, f"Test case 1 failed: expected {expected1}, got {result1}"

    # Test case 2
    args2 = "bbbbb"  # Replace with actual inputs
    expected2 = 1  # Replace with expected output
    result2 = solution.lengthOfLongestSubstring(args2)
    assert result2 == expected2, f"Test case 2 failed: expected {expected2}, got {result2}"

    # Test case 3
    args3 = "pwwkew"  # Replace with actual inputs
    expected3 = 3  # Replace with expected output
    result3 = solution.lengthOfLongestSubstring(args3)
    assert result3 == expected3, f"Test case 3 failed: expected {expected3}, got {result3}"

    # Add more test cases as needed
    print("All Q3 test cases passed!")


if __name__ == "__main__":
    run_tests()
