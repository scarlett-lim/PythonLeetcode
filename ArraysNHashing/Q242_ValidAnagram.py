from collections import defaultdict


class Solution:

    # Time Space: O(m + n)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = defaultdict(int)

        for item in s:
            count[item] += 1

        for item in t:
            count[item] -= 1

        for item in count.values():
            if item != 0:
                return False
        return True




def run_tests():
    solution = Solution()

    # Test case 1
    # s1, t1 = "anagram", "nagaram"
    # expected1 = True  # Replace with expected output
    # result1 = solution.isAnagram(s1, t1)
    # assert result1 == expected1, f"Test case 1 failed: expected {expected1}, got {result1}"

    s2, t2 = "rat", "cat"
    expected2 = False
    result2 = solution.isAnagram(s2, t2)
    assert result2 == expected2, f"Test case 2 failed: expected {expected2}, got {result2}"

    # Test case 3
    s3, t3 = "aacc", "ccac"
    expected3 = False
    result3 = solution.isAnagram(s3, t3)
    assert result3 == expected3, f"Test case 3 failed: expected {expected3}, got {result3}"

    # Add more test cases as needed
    print("All Q242 test cases passed!")


if __name__ == "__main__":
    run_tests()
