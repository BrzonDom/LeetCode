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


if __name__ == '__main__':

    InputLst = [[1, 2, 3, 4],
                [],
                [1]]

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
            curNd = curNd.next

        print(f"\tOrg Linked list: {valLst}")
        print()

        hdLLOrg = lnkLst.head

        #       Swap 1 and 2
        curLftNd = hdLLOrg
        nxtLftNd = hdLLOrg.next

        prvRgtNd = hdLLOrg
        curRgtNd = hdLLOrg.next
        nxtRgtNd = hdLLOrg.next.next

        lnkLst.head = curRgtNd
        curRgtNd.next = curLftNd
        curLftNd.next = nxtRgtNd

        # valLst = []
        # curNd = lnkLst.head
        #
        # while curNd:
        #     valLst.append(curNd.val)
        #     curNd = curNd.next
        #
        # print(f"\tOut Linked list: {valLst}")
        # print()


        #       Swap 2 and 3
        # prvLftNd = hdLLOrg
        # curLftNd = hdLLOrg.next
        # nxtLftNd = hdLLOrg.next.next
        #
        # prvRgtNd = hdLLOrg.next
        # curRgtNd = hdLLOrg.next.next
        # nxtRgtNd = hdLLOrg.next.next.next
        #
        # hdLLOrg.next = curRgtNd
        # curRgtNd.next = curLftNd
        # curLftNd.next = nxtRgtNd

        hdLLOrg = lnkLst.head

        #       Swap 3 and 4
        prvLftNd = hdLLOrg.next
        curLftNd = hdLLOrg.next.next
        nxtLftNd = hdLLOrg.next.next.next

        prvRgtNd = hdLLOrg.next.next
        curRgtNd = hdLLOrg.next.next.next

        prvLftNd.next = curRgtNd
        curRgtNd.next = curLftNd
        curLftNd.next = None

        valLst = []
        curNd = lnkLst.head

        while curNd:
            valLst.append(curNd.val)
            curNd = curNd.next

        print(f"\tOut Linked list: {valLst}")
        print()

        print("\n")
