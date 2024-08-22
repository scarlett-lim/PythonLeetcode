from typing import Optional, List
from Module.ListNodeClass import ListNode
from Module.ListNodeClass import listToLinkList
from Module.ListNodeClass import linkedListToList


class Solution:

    # time space : o(n)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if head is None or head is the last node
        if not head:
            return None

        # Recursively reverse the rest of the list
        newhead = head
        if head.next:
            newhead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newhead

        # Make the next node point to the current node (reverse the link)
        head.next.next = head

        # Set the current node's next to None
        head.next = None

        return newhead


    # Two Pointers
    # Space O1
    # Time ON
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     prev, current = None, head
    #
    #     while current:
    #         next = current.next
    #         current.next = prev
    #
    #         prev = current
    #         current = next
    #
    #     return prev


def run_tests():
    solution = Solution()

    # Test case 1
    args1 = listToLinkList([1,2,3,4,5])  # Replace with actual inputs
    expected1 = [5,4,3,2,1]  # Replace with expected output
    result1 = linkedListToList(solution.reverseList(args1))
    assert result1 == expected1, f"Test case 1 failed: expected {expected1}, got {result1}"

    # Test case 2
    args2 = listToLinkList([1,2])  # Replace with actual inputs
    expected2 = [2,1]  # Replace with expected output
    result2 = linkedListToList(solution.reverseList(args2))
    assert result2 == expected2, f"Test case 2 failed: expected {expected2}, got {result2}"

    # Test case 3
    args3 = listToLinkList([])  # Replace with actual inputs
    expected3 = []  # Replace with expected output
    result3 = linkedListToList(solution.reverseList(args3))
    assert result3 == expected3, f"Test case 3 failed: expected {expected3}, got {result3}"

    # Add more test cases as needed
    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()
