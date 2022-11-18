from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[list]) -> Optional[list]:
        if lists is None or len(lists) == 0:
            return []

        result = []
        while len(lists) > 0:
            index_min = min(range(len(lists)), key=lambda i: lists[i][0] if len(lists[i]) > 0 else None)
            if len(lists[index_min]) > 0:
                result.append(lists[index_min].pop(0))
            if len(lists[index_min]) == 0:
                del lists[index_min]

        return result


if __name__ == "__main__":
    final_list = Solution().mergeKLists([[1, 4, 5, 9], [1, 3, 4, 6], [2, 6]])
    print(final_list)

    final_list = Solution().mergeKLists([])
    print(final_list)

    final_list = Solution().mergeKLists([[]])
    print(final_list)
