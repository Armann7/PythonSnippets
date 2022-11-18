from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

    def __str__(self):
        if self.next is not None:
            return f"{str(self.val)} {str(self.next)} "
        return f"{str(self.val)}"


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0:
            return None

        lists = [item for item in lists if item is not None]
        head = tail = None
        while len(lists) > 0:
            index_min = min(range(len(lists)), key=lambda i: lists[i].val)
            if index_min == -1:
                return None
            head = lists[index_min] if head is None else head
            if tail is None:
                tail = lists[index_min]
            else:
                tail.next, tail = lists[index_min], lists[index_min]

            lists[index_min] = lists[index_min].next
            if lists[index_min] is None:
                del lists[index_min]

        return head


if __name__ == "__main__":
    llist1 = ListNode(0, (ListNode(3, ListNode(8, ListNode(13, ListNode(14, ListNode(25)))))))
    llist2 = ListNode(4, (ListNode(7, ListNode(12, ListNode(31, ListNode(40, ListNode(51)))))))
    llist3 = ListNode(3, (ListNode(4, ListNode(8, ListNode(11, ListNode(12, ListNode(22)))))))

    final_list = Solution().mergeKLists([llist1, llist2, llist3])
    print(final_list)

    final_list = Solution().mergeKLists([])
    print(final_list)

    final_list = Solution().mergeKLists([None])
    print(final_list)
