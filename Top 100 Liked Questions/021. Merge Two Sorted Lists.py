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
        newNd = ListNode(val)

        if self.head is None:
            self.head = newNd

        else:
            curNd = self.head

            while curNd.next:
                curNd = curNd.next
            curNd.next = newNd


InputLst = [[[1, 2, 4], [1, 3,  4]],
            [[1, 3, 4, 7, 8], [2, 3, 5, 6]],
            # [[], []],
            [[], [0]]]

for csCnt, Lsts in enumerate(InputLst):

    lst1 = Lsts[0]
    lst2 = Lsts[1]

    print(f"{csCnt+1}. Case:\n")

    print(f"\t1. List: {lst1}")
    print(f"\t2. List: {lst2}")
    print()

    lnkLst1 = LinkList()
    lnkLst2 = LinkList()

    for num in lst1:
        lnkLst1.append(num)

    for num in lst2:
        lnkLst2.append(num)

    print(f"\t\t1. Linked list: ", end="")

    curNode = lnkLst1.head
    while curNode:
        print(f"{curNode.val}", end=" ")

        curNode = curNode.next
    print()

    print(f"\t\t2. Linked list: ", end="")

    curNode = lnkLst2.head
    while curNode:
        print(f"{curNode.val}", end=" ")

        curNode = curNode.next
    print("\n")

    hdLL1 = lnkLst1.head
    hdLL2 = lnkLst2.head

    hdFnLL = ListNode()

    curNd1 = hdLL1
    curNd2 = hdLL2

    curNdFn = hdFnLL

    print(f"\tFin. Linked list: ", end="")

    while curNd1 and curNd2:

        if curNd1.val < curNd2.val:
            curNdFn.next = curNd1

            curNd1 = curNd1.next

        else:
            curNdFn.next = curNd2

            curNd2 = curNd2.next

        curNdFn = curNdFn.next

        print(curNdFn.val, end=" ")

    if curNd1:
        while curNd1:
            curNdFn.next = curNd1.next

            curNd1 = curNd1.next
            curNdFn = curNdFn.next

    elif curNd2:
        while curNd2:
            curNdFn.next = curNd2.next

            curNd2 = curNd2.next
            curNdFn = curNdFn.next

    print("\n\n")
