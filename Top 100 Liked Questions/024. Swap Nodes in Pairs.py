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
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.nxt = nxt

    def valLst_Nd(self):
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

    def valLst_Lnk(self, strNd=None):

        if strNd is None:
            strNd = self.head

        curNd = strNd
        valLst = []

        while curNd:
            valLst.append(curNd.val)
            curNd = curNd.nxt

        return valLst


def Hlp01_Swp_PrvCur_Prt(swpVal, lnkLst):

    HdNd = lnkLst.head
    preHdNd = ListNode(0, HdNd)

    valLft = swpVal
    valRgt = swpVal + 1

    idxLft = valLft - 1
    idxRgt = valRgt - 1

    cntLft = 0
    cntRgt = 0

    print(f"\t\tSwitch: {idxLft}.Node and {idxRgt}.Node")

    prvLftNd = preHdNd
    curLftNd = HdNd

    while curLftNd is not None and cntLft != idxLft:
        cntLft += 1

        prvLftNd = curLftNd
        curLftNd = curLftNd.nxt

    prvRgtNd = preHdNd
    curRgtNd = HdNd

    while curRgtNd is not None and cntRgt != idxRgt:
        cntRgt += 1

        prvRgtNd = curRgtNd
        curRgtNd = curRgtNd.nxt

    if curLftNd:
        print(f"\t\t\t{idxLft}.Node: {curLftNd.val}")
    else:
        print(f"\t\t\t{idxLft}.Node: None")

    if curRgtNd:
        print(f"\t\t\t{idxRgt}.Node: {curRgtNd.val}")
    else:
        print(f"\t\t\t{idxRgt}.Node: None")
    print()

    if valLft == valRgt:
        return lnkLst

    elif curLftNd is None or curRgtNd is None:
        return lnkLst

    elif curLftNd == HdNd:
        curLftNd.nxt = curRgtNd.nxt
        lnkLst.head = curRgtNd
        curRgtNd.nxt = curLftNd

    elif curRgtNd.nxt is None:
        prvLftNd.nxt = curRgtNd
        curRgtNd.nxt = curLftNd
        curLftNd.nxt = None

    else:
        prvLftNd.nxt = curRgtNd
        curLftNd.nxt = curRgtNd.nxt
        curRgtNd.nxt = curLftNd

    return lnkLst


if __name__ == '__main__':

    # InputLst = [[1, 2, 3, 4],
    #             [],
    #             [1]]

    InputLst = [[1, 2, 3, 4, 5]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt+1}. Case\n")

        print(f"\tList: {case}")
        print()

        lnkLst = LinkList()

        for num in case:
            lnkLst.append(num)

        valLst = lnkLst.valLst_Lnk()

        print(f"\tOrg Linked list: {valLst}")
        print()

        HdNd = lnkLst.head
        prHdNd = ListNode(0, HdNd)

        # swpVal = 2
        # lnkLst = Hlp01_Swp_PrvCur_Prt(swpVal, lnkLst)

        valLst = lnkLst.valLst_Lnk()

        print(f"\tOut Linked list: {valLst}")

        print("\n")
