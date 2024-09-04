import typing


class Solution:

    # Time Space : O(n)
    # def isPalindrome(self, s: str) -> bool:
    #     filteredString = [item.lower() for item in s if item.isalnum()]
    #     return filteredString == filteredString[::-1]

    # Time : O(n)
    # Space O(1)
    def isPalindrome(self, s: str) -> bool:
        lp, rp = 0, len(s)-1

        while lp < rp:
            while not s[lp].isalnum() and lp<rp:
                lp += 1
            while not s[rp].isalnum() and rp>lp:
                rp -= 1
            if s[rp].lower() != s[lp].lower():
                return False
            lp, rp = lp+1, rp-1
        return True

        # lp,rp = 0,len(s)-1
        #
        # while lp < rp:
        #     # ensure lp and rp are alnum b4 make it lowecase
        #     while not self.isAlNum(s[lp]) and lp < rp:
        #         lp += 1
        #     while not self.isAlNum(s[rp]) and lp < rp:
        #         rp -= 1
        #     if s[lp].lower() != s[rp].lower():
        #         return False
        #     lp,rp = lp+1, rp-1
        # return True


    def isAlNum(self, char):
        return (('a' <= char <= 'z') or
                ('A' <= char <= 'Z') or
                ('0' <= char <= '9'))


def run_tests():
    solution = Solution()

    # Test case 1
    args1 = "A man, a plan, a canal: Panama"  # Replace with actual inputs
    expected1 = True  # Replace with expected output
    result1 = solution.isPalindrome(args1)
    assert result1 == expected1, f"Test case 1 failed: expected {expected1}, got {result1}"

    # Test case 2
    args2 = "race a car"  # Replace with actual inputs
    expected2 = False  # Replace with expected output
    result2 = solution.isPalindrome(args2)
    assert result2 == expected2, f"Test case 2 failed: expected {expected2}, got {result2}"

    # Test case 3
    args3 = " "  # Replace with actual inputs
    expected3 = True  # Replace with expected output
    result3 = solution.isPalindrome(args3)
    assert result3 == expected3, f"Test case 3 failed: expected {expected3}, got {result3}"

    # Add more test cases as needed
    print("All Q125 test cases passed!")


if __name__ == "__main__":
    run_tests()
