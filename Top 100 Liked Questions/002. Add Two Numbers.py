"""
2. Add Two Numbers

https://leetcode.com/problems/add-two-numbers/

    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
    order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.


    Example 1:

        Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
        Output: [7, 0, 8]

        Explanation: 342 + 465 = 807.

    Example 2:

        Input: l1 = [0], l2 = [0]
        Output: [0]

    Example 3:

        Input: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
        Output: [8, 9, 9, 9, 0, 0, 0, 1]


    Constraints:

        The number of nodes in each linked list is in the range [1, 100].
        0 <= Node.val <= 9
        It is guaranteed that the list represents a number that does not have leading zeros.

"""


class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.nxt = nxt

    def valLst(self):
        curNd = self
        valLst = []

        while curNd:
            valLst.append(curNd.val)
            curNd = curNd.nxt

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

            while curNd.nxt:
                curNd = curNd.nxt

            curNd.nxt = newNd

    def valLst(self, strtNd=None):

        if strtNd is None:
            strtNd = self.head

        valLst = []
        curNd = strtNd

        while curNd:
            valLst.append(curNd.val)
            curNd = curNd.nxt

        return valLst


def mkLnkLst(lst):

    lnkLst = LinkList()

    for num in lst:
        lnkLst.append(num)

    return lnkLst


def Sol01A_WhlIndv_Prt(InLst):

    for csCnt, case in enumerate(InLst):

        print(f"{csCnt + 1}. Case\n")

        lst1 = case[0]
        lst2 = case[1]

        lnkLst1 = mkLnkLst(lst1)
        lnkLst2 = mkLnkLst(lst2)

        print(f"\t1. Linked List: {lnkLst1.valLst()}")
        print(f"\t2. Linked List: {lnkLst2.valLst()}")
        print()

        curNd1 = lnkLst1.head
        curNd2 = lnkLst2.head

        outNdVal = curNd1.val + curNd2.val
        prvNdVal = 0

        if outNdVal >= 10:
            prvNdVal = 1
            outNdVal -= 10

        outHdNd = ListNode(outNdVal)
        curOutNd = outHdNd

        curNd1 = curNd1.nxt
        curNd2 = curNd2.nxt

        while curNd1 and curNd2:

            outNdVal = curNd1.val + curNd2.val + prvNdVal

            if outNdVal >= 10:
                outNdVal -= 10
                prvNdVal = 1

            else:
                prvNdVal = 0

            nxtOutNd = ListNode(outNdVal)
            curOutNd.nxt = nxtOutNd
            curOutNd = nxtOutNd

            curNd1 = curNd1.nxt
            curNd2 = curNd2.nxt

        while curNd1:

            outNdVal = curNd1.val + prvNdVal

            if outNdVal >= 10:
                outNdVal -= 10
                prvNdVal = 1

            else:
                prvNdVal = 0

            nxtOutNd = ListNode(outNdVal)
            curOutNd.nxt = nxtOutNd
            curOutNd = nxtOutNd

            curNd1 = curNd1.nxt

        while curNd2:

            outNdVal = curNd2.val + prvNdVal

            if outNdVal >= 10:
                outNdVal -= 10
                prvNdVal = 1

            else:
                prvNdVal = 0

            nxtOutNd = ListNode(outNdVal)
            curOutNd.nxt = nxtOutNd
            curOutNd = nxtOutNd

            curNd2 = curNd2.nxt

        if prvNdVal:
            nxtOutNd = ListNode(1)
            curOutNd.nxt = nxtOutNd

        outValLst = outHdNd.valLst()

        print(f"\tOut Linked List: {outValLst}")

        print("\n")


def Sol01_WhlIndv_Prt(lst1, lst2):

    lnkLst1 = mkLnkLst(lst1)
    lnkLst2 = mkLnkLst(lst2)

    curNd1 = lnkLst1.head
    curNd2 = lnkLst2.head

    print(f"\t1. Linked List: {curNd1.valLst()}")
    print(f"\t2. Linked List: {curNd2.valLst()}")
    print()

    outNdVal = curNd1.val + curNd2.val
    prvNdVal = 0

    if outNdVal >= 10:
        prvNdVal = 1
        outNdVal -= 10

    outHdNd = ListNode(outNdVal)
    curOutNd = outHdNd

    curNd1 = curNd1.nxt
    curNd2 = curNd2.nxt

    while curNd1 and curNd2:

        outNdVal = curNd1.val + curNd2.val + prvNdVal

        if outNdVal >= 10:
            outNdVal -= 10
            prvNdVal = 1

        else:
            prvNdVal = 0

        nxtOutNd = ListNode(outNdVal)
        curOutNd.nxt = nxtOutNd
        curOutNd = nxtOutNd

        curNd1 = curNd1.nxt
        curNd2 = curNd2.nxt

    while curNd1:

        outNdVal = curNd1.val + prvNdVal

        if outNdVal >= 10:
            outNdVal -= 10
            prvNdVal = 1

        else:
            prvNdVal = 0

        nxtOutNd = ListNode(outNdVal)
        curOutNd.nxt = nxtOutNd
        curOutNd = nxtOutNd

        curNd1 = curNd1.nxt

    while curNd2:

        outNdVal = curNd2.val + prvNdVal

        if outNdVal >= 10:
            outNdVal -= 10
            prvNdVal = 1

        else:
            prvNdVal = 0

        nxtOutNd = ListNode(outNdVal)
        curOutNd.nxt = nxtOutNd
        curOutNd = nxtOutNd

        curNd2 = curNd2.nxt

    if prvNdVal:
        nxtOutNd = ListNode(1)
        curOutNd.nxt = nxtOutNd

    outValLst = outHdNd.valLst()

    print(f"\tOut Linked List: {outValLst}")

    print("\n")


if __name__ == '__main__':

    InputLst = [[[2, 4, 3], [5, 6, 4]],
                [[0], [0]],
                [[9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]]]

    # Sol01A_WhlIndv_Prt(InputLst)

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}. Case\n")

        lst1 = case[0]
        lst2 = case[1]

        lnkLst1 = mkLnkLst(lst1)
        lnkLst2 = mkLnkLst(lst2)

        hdNd1 = lnkLst1.head
        hdNd2 = lnkLst2.head

        Sol01_WhlIndv_Prt(case[0], case[1])
