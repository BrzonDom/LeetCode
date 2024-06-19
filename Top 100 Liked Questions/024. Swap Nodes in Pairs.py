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


if __name__ == '__main__':

    # InputLst = [[1, 2, 3, 4],
    #             [],
    #             [1]]

    InputLst = [[1, 2, 3, 4]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt+1}. Case\n")

        print(f"\tList: {case}")
        print()

        lnkLst = LinkList()

        for num in case:
            lnkLst.append(num)

        valLst = []
        curNd = lnkLst.head

        while curNd:
            valLst.append(curNd.val)
            curNd = curNd.nxt

        print(f"\tOrg Linked list: {valLst}")
        print()

        HdNd = lnkLst.head
        preHdNd = ListNode()
        preHdNd.nxt = HdNd

        # prvNd = HdNd
        # curNd = HdNd.nxt
        # nxtNd = HdNd.nxt.nxt

        swtIdx = [0, 1]
        swtIdx.sort()

        idxLft = 0
        idxRgt = 0

        print(f"\t\tSwitch: {swtIdx[0]}.Node and {swtIdx[1]}.Node")

        prvLftNd = preHdNd
        curLftNd = HdNd

        while curLftNd is not None and idxLft != swtIdx[0]:
            idxLft += 1

            prvLftNd = curLftNd
            curLftNd = curLftNd.nxt

        prvRgtNd = preHdNd
        curRgtNd = HdNd

        while curRgtNd is not None and idxRgt != swtIdx[1]:
            idxRgt += 1

            prvRgtNd = curRgtNd
            curRgtNd = curRgtNd.nxt

        if curLftNd:
            print(f"\t\t\t{swtIdx[0]}.Node: {curLftNd.val}")
        else:
            print(f"\t\t\t{swtIdx[0]}.Node: None")

        if curRgtNd:
            print(f"\t\t\t{swtIdx[1]}.Node: {curRgtNd.val}")
        else:
            print(f"\t\t\t{swtIdx[1]}.Node: None")
        print()

        if swtIdx[0] == swtIdx[1]:
            continue

        elif curLftNd is None or curRgtNd is None:
            continue

        elif curLftNd == HdNd:
            curLftNd.nxt = curRgtNd.nxt
            lnkLst.head = curRgtNd
            curRgtNd.nxt = curLftNd

        """
              Left Node  =  Head
              Right Node != Tail
        """
        # HdNd = lnkLst.head
        # preHdNd = ListNode()
        # preHdNd.nxt = HdNd
        #
        # prvLftNd = preHdNd
        # curLftNd = HdNd
        # prvRgtNd = HdNd
        # curRgtNd = HdNd.nxt
        #
        # curLftNd.nxt = curRgtNd.nxt
        # lnkLst.head = curRgtNd
        # curRgtNd.nxt = curLftNd

        """
              Left Node  != Head
              Right Node != Tail
        """
        # HdNd = lnkLst.head
        # preHdNd = ListNode()
        # preHdNd.nxt = HdNd
        #
        # prvLftNd = HdNd
        # curLftNd = HdNd.nxt
        # prvRgtNd = HdNd.nxt
        # curRgtNd = HdNd.nxt.nxt
        #
        # prvLftNd.nxt = curRgtNd
        # curLftNd.nxt = curRgtNd.nxt
        # curRgtNd.nxt = curLftNd

        """
              Left Node  != Head
              Right Node  = Tail
        """
        # HdNd = lnkLst.head
        # preHdNd = ListNode()
        # preHdNd.nxt = HdNd
        #
        # prvLftNd = HdNd.nxt
        # curLftNd = HdNd.nxt.nxt
        # prvRgtNd = HdNd.nxt.nxt
        # curRgtNd = HdNd.nxt.nxt.nxt
        #
        # prvLftNd.nxt = curRgtNd
        # curRgtNd.nxt = curLftNd
        # curLftNd.nxt = None


        valLst = []
        curNd = lnkLst.head

        while curNd:
            valLst.append(curNd.val)
            curNd = curNd.nxt

        print(f"\tOut Linked list: {valLst}")

        print("\n")
