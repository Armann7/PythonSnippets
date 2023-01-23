"""2. Add Two Numbers"""
from typing import Iterable, Optional

class ListIter:
    def __init__(self, node: "ListNode"):
        self.first_node = node
        self.current_node = None

    def __next__(self):
        if self.current_node is None:
            self.current_node = self.first_node
        else:
            self.current_node = self.current_node.next
            if self.current_node is None:
                raise StopIteration
        return self.current_node

class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

    def __iter__(self):
        return ListIter(self)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        zero_node = ListNode(-1)
        node = zero_node
        add_one = 0
        while l1 is not None or l2 is not None:
            l1 = l1 if l1 is not None else ListNode(0)
            l2 = l2 if l2 is not None else ListNode(0)
            items_sum = l1.val + l2.val + add_one
            node.next = ListNode(items_sum % 10)
            l1, l2, node = l1.next, l2.next, node.next
            add_one = 0 if items_sum < 10 else 1
        if add_one == 1:
            node.next = ListNode(1)
        return zero_node.next

def make_linked_list(data: Iterable) -> ListNode:
    zero_node = ListNode(-1)
    node = zero_node
    for value in data:
        node.next = ListNode(value)
        node = node.next
    return zero_node.next


def print_linked_list(list_: ListNode):
    for node in list_:
        print(node.val, end=" ")
    print("")


if __name__ == "__main__":
    print_linked_list(Solution().addTwoNumbers(make_linked_list([2,4,3]), make_linked_list([5,6,4])))
    print_linked_list(Solution().addTwoNumbers(make_linked_list([9,9,9,9,9,9,9]), make_linked_list([9,9,9,9])))

