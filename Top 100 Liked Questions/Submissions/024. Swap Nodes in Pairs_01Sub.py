"""
24. Swap Nodes in Pairs

https://leetcode.com/problems/swap-nodes-in-pairs/description/

    Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without
    modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

    Example 1:

        Input: head = [1, 2, 3, 4]
        Output: [2, 1, 4, 3]

    Example 2:

        Input: head = []
        Output: []

    Example 3:

        Input: head = [1]
        Output: [1]


    Constraints:

        The number of nodes in the list is in the range [0, 100].
        0 <= Node.val <= 100

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

    def valLst_Lnk(self, strNd=None):

        if strNd is None:
            strNd = self.head

        curNd = strNd
        valLst = []

        while curNd:
            valLst.append(curNd.val)
            curNd = curNd.next

        return valLst


def Sol01_SwpWhlLftRgt_Prt(case):

    lnkLst = LinkList()

    for num in case:
        lnkLst.append(num)

    valLst = lnkLst.valLst_Lnk()

    print(f"\tOrg Linked list: {valLst}")
    print()

    HdNd = lnkLst.head
    prHdNd = ListNode(0, HdNd)

    curNd = prHdNd

    while curNd.next and curNd.next.next:

        lftNd = curNd.next
        rgtNd = curNd.next.next

        lftNd.next = rgtNd.next

        curNd.next = rgtNd
        curNd.next.next = lftNd

        curNd = curNd.next.next

    lnkLst.head = prHdNd.next

    valLst = lnkLst.valLst_Lnk()

    print(f"\tOut Linked list: {valLst}")

    print("\n")


def Sol01_SwpWhlLftRgt(HdNd):

    prHdNd = ListNode(0, HdNd)

    curNd = prHdNd

    while curNd.next and curNd.next.next:

        lftNd = curNd.next
        rgtNd = curNd.next.next

        lftNd.next = rgtNd.next

        curNd.next = rgtNd
        curNd.next.next = lftNd

        curNd = curNd.next.next

    lnkLst.head = prHdNd.next

    return lnkLst.head


if __name__ == '__main__':

    InputLst = [[1, 2, 3, 4],
                [],
                [1]]

    for csCnt, case in enumerate(InputLst):

        # print(f"{csCnt+1}. Case\n")

        lnkLst = LinkList()

        for num in case:
            lnkLst.append(num)

        csHdLL = lnkLst.head

        Sol01_SwpWhlLftRgt(csHdLL)

