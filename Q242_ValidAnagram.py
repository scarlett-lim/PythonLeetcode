from collections import defaultdict


class Solution:

    # time : o(n log n)
    # space : o(n)
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
    #
    #     sorted_s = ''.join(sorted(s))
    #     sorted_t = ''.join(sorted(t))
    #
    #     for item in range(len(sorted_s)):
    #         if sorted_s[item] != sorted_t[item]:
    #             return False
    #     return True

    # Time & Space : O(n)
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
    #
    #     dictionary = {}
    #
    #     for i in range(len(s)):
    #         if s[i] in dictionary:
    #             dictionary[s[i]] += 1
    #
    #     for j in range(len(t)):
    #         if t[j] in dictionary:
    #             dictionary[t[j]] -= 1
    #             if dictionary[t[j]] == 0:
    #                 dictionary.pop(t[j])
    #         else:
    #             dictionary[t[j]] = j
    #
    #     if dictionary == {}:
    #         return True
    #     else:
    #         return False

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = defaultdict(int)

        for char in s:
            count[char] += 1

        for char in t:
            count[char] -= 1
            if count[char] == 0:
                del count[char]

        return not count


def run_tests():
    solution = Solution()

    # Test case 1
    s1, t1 = "anagram", "nagaram"
    expected1 = True  # Replace with expected output
    result1 = solution.isAnagram(s1, t1)
    assert result1 == expected1, f"Test case 1 failed: expected {expected1}, got {result1}"

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
    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
