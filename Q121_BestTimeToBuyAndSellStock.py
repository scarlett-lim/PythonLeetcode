from typing import List


class Solution:

    # Two pointers
    # Time ON
    # Space O1
    def maxProfit(self, prices: List[int]) -> int:
        # lp to find minimum value, rp to find maximum
        lp,rp=0,1

        maxProfit = 0

        while rp < len(prices):
            if prices[rp] < prices[lp]:
                lp = rp
            else:
                maxProfit = max(maxProfit,prices[rp]-prices[lp])
            rp+=1
        return maxProfit











def run_tests():
    solution = Solution()

    # Test case 1
    args1 = [7,1,5,3,6,4]  # Replace with actual inputs
    expected1 = 5  # Replace with expected output
    result1 = solution.maxProfit(args1)
    assert result1 == expected1, f"Test case 1 failed: expected {expected1}, got {result1}"

    # Test case 2
    args2 = [7,6,4,3,1]  # Replace with actual inputs
    expected2 = 0  # Replace with expected output
    result2 = solution.maxProfit(args2)
    assert result2 == expected2, f"Test case 2 failed: expected {expected2}, got {result2}"

    # Add more test cases as needed
    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
