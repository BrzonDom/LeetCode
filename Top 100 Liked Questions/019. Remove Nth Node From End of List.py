"""
19. Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

    Given the head of a linked list, remove the nth node from the end of the list and return its head.

    Example 1:

        Input: head = [1, 2, 3, 4, 5], n = 2
        Output: [1, 2, 3, 5]

    Example 2:

        Input: head = [1], n = 1
        Output: []

    Example 3:

        Input: head = [1, 2], n = 1
        Output: [1]


    Constraints:

        The number of nodes in the list is sz.
        1 <= sz <= 30
        0 <= Node.val <= 100
        1 <= n <= sz

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkList:
    def __init__(self):
        self.head = None

    def append(self, val):
        newNd = ListNode(val)

        if self.head is None:
            self.head = newNd

        else:
            curNd = self.head

            while curNd.next:
                curNd = curNd.next
            curNd.next = newNd


InputLst = [[[1, 2, 3, 4, 5], 2],
            [[1], 1],
            [[1, 2], 1]]

for csCnt, case in enumerate(InputLst):

    print(f"{csCnt + 1}. Case:\n")

    lnkLst = case[0]
    rmvNd = case[1]

    print(f"\tLinked list: {lnkLst}")
    print()
    print(f"\t\tNode index: -{rmvNd}")
    print(f"\t\tNode value: {lnkLst[-rmvNd]}")

    print("\n")
