from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        node_prev = None
        while node is not None:
            node.next, node, node_prev = node_prev, node.next, node

        return node_prev


if __name__ == "__main__":
    llist = ListNode(0, (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))

    llist = Solution().reverseList(llist)

    while llist is not None:
        print(llist.val)
        llist = llist.next
