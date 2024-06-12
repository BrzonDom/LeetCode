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


def Sol02_FstSlwAlg_Prt(hdLL, idxNd):
    print(f"\tIn Linked list: {hdLL.valLst_Nd()}")
    print()
    print(f"\t\tNode index: -{idxNd}")
    print(f"\t\tNode value: {lst[-idxNd]}")
    print()

    preHdLL = ListNode(0, hdLL)
    fstNd = slwNd = preHdLL

    for shft in range(idxNd):
        fstNd = fstNd.next

    print(f"\t\tFast shift:")
    print(f"\t\t\tFast link list: {fstNd.valLst_Nd()}")
    print(f"\t\t\tSlow link list: {slwNd.valLst_Nd()}")
    print()

    if fstNd.next:
        while fstNd.next:
            fstNd = fstNd.next
            slwNd = slwNd.next

        print(f"\t\tFast and slow shift:")
        print(f"\t\t\tFast link list: {fstNd.valLst_Nd()}")
        print(f"\t\t\tSlow link list: {slwNd.valLst_Nd()}")
        print()

    slwNd.next = slwNd.next.next
    preHdLL = preHdLL.next

    if preHdLL:
        print(f"\tOut Link list: {preHdLL.valLst_Nd()}")
    else:
        print(f"\tOut Link list: []")

    print("\n")


def Sol02_FstSlwAlg(hdLL, idxNd):

    preHdLL = ListNode(0, hdLL)
    fstNd = slwNd = preHdLL

    for shft in range(idxNd):
        fstNd = fstNd.next

    while fstNd.next:
        fstNd = fstNd.next
        slwNd = slwNd.next

    slwNd.next = slwNd.next.next
    preHdLL = preHdLL.next

    return preHdLL


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

        Sol02_FstSlwAlg_Prt(hdLLIn, idxNd)
