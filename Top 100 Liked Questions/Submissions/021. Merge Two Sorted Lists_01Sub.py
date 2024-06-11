"""
21. Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/description/

    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two
    lists.

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

    def valLst_Nd(self):

        curNd = self
        valLst = []

        while curNd:
            valLst.append(curNd.val)
            curNd = curNd.next

        return valLst


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

    def valLst_Lnk(self, strtNd=None):

        if strtNd is None:
            strtNd = self.head

        curNd = strtNd
        valLst = []

        while curNd:
            valLst.append(curNd.val)
            curNd = curNd.next

        return valLst


def Sol01_While_Prt(hdLL1, hdLL2):

    # if hdLL1:
    #     print(f"\t\t1. Linked list: {hdLL1.valLst_Nd()}")
    # else:
    #     print(f"\t\t1. Linked list: ")
    #
    # if hdLL2:
    #     print(f"\t\t2. Linked list: {hdLL2.valLst_Nd()}")
    # else:
    #     print(f"\t\t2. Linked list: ")
    # print()

    preHdFnLL = ListNode()
    lnkLstFn = LinkList()

    curNd1 = hdLL1
    curNd2 = hdLL2

    curNdFn = preHdFnLL

    while curNd1 and curNd2:

        if curNd1.val < curNd2.val:
            curNdFn.next = curNd1
            curNd1 = curNd1.next

        else:
            curNdFn.next = curNd2
            curNd2 = curNd2.next

        curNdFn = curNdFn.next

        # print(curNdFn.val, end=" ")
        lnkLstFn.append(curNdFn.val)

    while curNd1:
        # print(curNd1.val, end=" ")
        lnkLstFn.append(curNd1.val)
        curNdFn.next = curNd1

        curNd1 = curNd1.next
        curNdFn = curNdFn.next

    while curNd2:
        # print(curNd2.val, end=" ")
        lnkLstFn.append(curNd2.val)
        curNdFn.next = curNd2

        curNd2 = curNd2.next
        curNdFn = curNdFn.next

    # print(f"\tFin. Linked list: {lnkLstFn.valLst_Lnk()}")

    hdFnLL = preHdFnLL.next
    # if hdFnLL:
    #     print(f"\tFin. Linked list: {hdFnLL.valLst_Nd()}")
    # else:
    #     print(f"\tFin. Linked list: ")
    #
    # print("\n")

    return hdFnLL


if __name__ == '__main__':

    InputLst = [[[1, 2, 4], [1, 3,  4]],
                [[1, 3, 4, 7, 8], [2, 3, 5, 6]],
                [[], []],
                [[], [0]]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt+1}. Case:\n")

        lst1 = case[0]
        lst2 = case[1]

        lnkLst1 = LinkList()
        lnkLst2 = LinkList()

        for num in lst1:
            lnkLst1.append(num)

        for num in lst2:
            lnkLst2.append(num)

        hdLL1 = lnkLst1.head
        hdLL2 = lnkLst2.head

        # print(f"\t1. Linked list: {lnkLst1.valLst_Lnk()}")
        # print(f"\t2. Linked list: {lnkLst2.valLst_Lnk()}")

        Sol01_While_Prt(hdLL1, hdLL2)
