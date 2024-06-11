"""
21. Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/description/

    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

    Return the head of the merged linked list.

    Example 1:

        Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
        Output: [1, 1, 2, 3, 4, 4]

    Example 2:

        Input: list1 = [], list2 = []
        Output: []

    Example 3:

        Input: list1 = [], list2 = [0]
        Output: [0]


    Constraints:

        The number of nodes in both lists is in the range [0, 50].
        -100 <= Node.val <= 100
        Both list1 and list2 are sorted in non-decreasing order.

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkList:
    def __init__(self):
        self.head = None

    def append(self, val):
        nwNode = ListNode(val)

        if self.head is None:
            self.head = nwNode

        else:
            crNode = self.head

            while crNode:
                crNode = crNode.next

            crNode.next = nwNode


InputLst = [[[1, 2, 4], [1, 3,  4]],
            [[], []],
            [[], [0]]]

for csCnt, Lsts in enumerate(InputLst):

    lst1 = Lsts[0]
    lst2 = Lsts[1]

    print(f"{csCnt+1}. Case:\n")

    print(f"\t1.List:    {lst1}")
    print(f"\t2.List:    {lst2}")
    print()

    finLst = lst1 + lst2
    finLst.sort()

    print(f"\tFin. List: {finLst}")

    print("\n")
