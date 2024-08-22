from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def linkedListToList(head : Optional[ListNode]) -> List[int]:
    list = []
    if head is None:
        return list
    currentNode = head
    while currentNode:
        list.append(currentNode.val)
        currentNode = currentNode.next
    return list


def listToLinkList(numbers: List[int]) -> Optional[ListNode]:
    if not numbers:
        return None

    head = ListNode(numbers[0])
    currentNode = head
    for values in numbers[1:]:
        currentNode.next = ListNode(values)
        currentNode = currentNode.next
    return head