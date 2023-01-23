"""24. Swap Nodes in Pairs"""
from typing import Iterable, Optional


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

    def __repr__(self):
        return f"{self.val}"


def make_linked_list(data: Iterable) -> ListNode:
    zero_node = ListNode(-1)
    node = zero_node
    for value in data:
        node.next = ListNode(value)
        node = node.next
    return zero_node.next


def print_linked_list(node: ListNode):
    while node is not None:
        print(node.val, end=" ")
        node = node.next
    print("")

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        new_head = None
        last = ListNode(0)
        while node is not None and node.next is not None:
            first, second = node, node.next
            second.next, first.next = first, second.next
            last.next = second
            last = first
            node = first.next
            new_head = new_head or second
        return new_head or head


if __name__ == "__main__":
    print_linked_list(Solution().swapPairs(make_linked_list([1,2,3,4])))
    print_linked_list(Solution().swapPairs(make_linked_list([1])))
