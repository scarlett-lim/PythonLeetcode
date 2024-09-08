from typing import Optional

from Module.ListNodeClass import ListNode
from Module.ListNodeClass import listToLinkList
from Module.ListNodeClass import linkedListToList


class Solution:

    # time o(n)
    # space o(1)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next



def run_tests():
    solution = Solution()

    # Test case 1
    args1 = (listToLinkList([1,2,3,4,5]), 2) # Replace with actual inputs
    expected1 = [1,2,3,5]  # Replace with expected output
    result1 = solution.removeNthFromEnd(*args1)
    assert linkedListToList(result1) == expected1, f"Test case 1 failed: expected {expected1}, got {result1}"

    # Test case 2
    args2 = (listToLinkList([1]), 1)  # Replace with actual inputs
    expected2 = []  # Replace with expected output
    result2 = solution.removeNthFromEnd(*args2)
    assert linkedListToList(result2) == expected2, f"Test case 2 failed: expected {expected2}, got {result2}"

    # Test case 3
    args3 = (listToLinkList([1,2]), 1)  # Replace with actual inputs
    expected3 = [1]  # Replace with expected output
    result3 = solution.removeNthFromEnd(*args3)
    assert linkedListToList(result3) == expected3, f"Test case 3 failed: expected {expected3}, got {result3}"

    # Add more test cases as needed
    print("All Q21 test cases passed!")


if __name__ == "__main__":
    run_tests()
