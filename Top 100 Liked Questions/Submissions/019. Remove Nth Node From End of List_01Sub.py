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


def Sol01_LstScan_Prt(hdLLIn, idxNd):
    print(f"\tIn Linked list: {hdLLIn.valLst_Nd()}")
    print()
    print(f"\t\tNode index: -{idxNd}")
    print(f"\t\tNode value: {lst[-idxNd]}")
    print()

    ndLst = []
    curNd = hdLLIn

    while curNd:
        ndLst.append(curNd)
        curNd = curNd.next

    if len(ndLst) == 1:
        hdLLOut = None

    elif idxNd == len(ndLst):
        hdLLOut = ndLst[1]

    elif idxNd == 1:
        ndLst[-2].next = None
        hdLLOut = ndLst[0]

    else:
        ndLst[-idxNd - 1].next = ndLst[-idxNd + 1]
        hdLLOut = ndLst[0]

    if hdLLOut:
        print(f"\tOut Linked list: {hdLLOut.valLst_Nd()}")
    else:
        print("\tOut Linked list: []")

    print("\n")


def Sol01_LstScan(hdLLIn, idxNd):

    ndLst = []
    curNd = hdLLIn

    while curNd:
        ndLst.append(curNd)
        curNd = curNd.next

    if len(ndLst) == 1:
        return None

    elif idxNd == len(ndLst):
        return ndLst[1]

    elif idxNd == 1:
        ndLst[-2].next = None
        return ndLst[0]

    else:
        ndLst[-idxNd - 1].next = ndLst[-idxNd + 1]
        return ndLst[0]


if __name__ == '__main__':

    InputLst = [[[1, 2, 3, 4, 5], 2],
                [[1], 1],
                [[1, 2], 1]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}. Case:\n")

        lst = case[0]
        idxNd = case[1]

        lnkLst = LinkList()
        for val in lst:
            lnkLst.append(val)

        hdLLIn = lnkLst.head

        Sol01_LstScan_Prt(hdLLIn, idxNd)
