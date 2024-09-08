from typing import Optional

from Module.ListNodeClass import ListNode
from Module.ListNodeClass import listToLinkList
from Module.ListNodeClass import linkedListToList


class Solution:

    # time o(n+m)
    # space o(1)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newListNode = ListNode()
        currentNode = newListNode

        while list1 and list2:
            if list1.val < list2.val:
                currentNode.next = list1
                list1 = list1.next
            else:
                currentNode.next = list2
                list2 = list2.next
            currentNode = currentNode.next

        if list1:
            currentNode.next = list1
        else:
            currentNode.next = list2

        return newListNode.next



def run_tests():
    solution = Solution()

    # Test case 1
    args1 = (listToLinkList([1,2,4]), listToLinkList([1,3,4])) # Replace with actual inputs
    expected1 = [1,1,2,3,4,4]  # Replace with expected output
    result1 = solution.mergeTwoLists(*args1)
    assert linkedListToList(result1) == expected1, f"Test case 1 failed: expected {expected1}, got {result1}"

    # Test case 2
    args2 = (listToLinkList([]), listToLinkList([]))  # Replace with actual inputs
    expected2 = []  # Replace with expected output
    result2 = solution.mergeTwoLists(*args2)
    assert linkedListToList(result2) == expected2, f"Test case 2 failed: expected {expected2}, got {result2}"

    # Test case 3
    args3 = (listToLinkList([]), listToLinkList([0]))  # Replace with actual inputs
    expected3 = [0]  # Replace with expected output
    result3 = solution.mergeTwoLists(*args3)
    assert linkedListToList(result3) == expected3, f"Test case 3 failed: expected {expected3}, got {result3}"

    # Add more test cases as needed
    print("All Q21 test cases passed!")


if __name__ == "__main__":
    run_tests()
