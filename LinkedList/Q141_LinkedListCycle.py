from typing import Optional

from Module.ListNodeClass import ListNode


# time O(n)
# space O(1)
# algorithm used: Floyd's Tortoise and Hare
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False











        # slow, fast = head, head
        #
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         return True
        #
        # return False


def create_linked_list_with_cycle(values, pos):
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    cycle_node = None

    for i in range(len(values)):
        current.next = ListNode(values[i])
        current = current.next
        if i == pos:
            cycle_node = current

    if pos != -1:
        current.next = cycle_node  # Point the last node to the cycle node

    return head




def run_tests():
    solution = Solution()

    # Test case 1
    args1 = create_linked_list_with_cycle([3, 2, 0, -4], 1)  # Replace with actual inputs
    expected1 = True  # Replace with expected output
    result1 = solution.hasCycle(args1)
    assert result1 == expected1, f"Test case 1 failed: expected {expected1}, got {result1}"

    # Test case 2
    args2 = create_linked_list_with_cycle([1, 2], 0)   # Replace with actual inputs
    expected2 = True  # Replace with expected output
    result2 = solution.hasCycle(args2)
    assert result2 == expected2, f"Test case 2 failed: expected {expected2}, got {result2}"

    # Test case 3
    args3 = create_linked_list_with_cycle([1], -1) # Replace with actual inputs
    expected3 = False  # Replace with expected output
    result3 = solution.hasCycle(args3)
    assert result3 == expected3, f"Test case 3 failed: expected {expected3}, got {result3}"

    # Add more test cases as needed
    print("All Q141 test cases passed!")


if __name__ == "__main__":
    run_tests()
