"""
725. Split Linked List in Parts

https://leetcode.com/problems/split-linked-list-in-parts/description/


    Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

    The length of each part should be as equal as possible: no two parts should have a size differing by more than one.
    This may lead to some parts being null.

    The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have
    a size greater than or equal to parts occurring later.

    Return an array of the k parts.


    Example 1:

        Input: head = [1, 2, 3], k = 5

        Output: [[1], [2], [3], [], []]

        Explanation:
            The first element output[0] has output[0].val = 1, output[0].next = null.
            The last element output[4] is null, but its string representation as a ListNode is [].

    Example 2:

        Input: head = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3

        Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]

        Explanation:
            The input has been split into consecutive parts with size difference at most 1, and earlier parts are a
            larger size than the later parts.


    Constraints:

        The number of nodes in the list is in the range [0, 1000].
        0 <= Node.val <= 1000
        1 <= k <= 50


    Topics:

        Linked List


    Courses:

        Daily: 2024/09/13

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.nxt = nxt


class LinkList:
    def __init__(self):
        self.head = None

    def add(self, val):
        nwNd = ListNode(val)

        if self.head is None:
            self.head = nwNd

        else:
            crNd = self.head

            while crNd.nxt:
                crNd = crNd.nxt

            crNd.nxt = nwNd


if __name__ == "__main__":

    InputLst = [[[1, 2, 3], 5],
                [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        Lnks = case[0]
        Prt = case[1]

        lnLnk = len(Lnks)

        print(f"\tLinked list values: {Lnks}")
        print(f"\t\tList length: {lnLnk}")
        print(f"\tParts: {Prt}")
        print()

        lnkLst = LinkList()

        for val in Lnks:
            lnkLst.add(val)

        crNd = lnkLst.head

        print("\t\tLinked list: ", end="")
        while crNd:
            print(crNd.val, end=" ")

            crNd = crNd.nxt

            if crNd:
                print(">", end=" ")
            else:
                print()
        print()

        dvds = [0 for _ in range(Prt)]

        prt = lnLnk // Prt
        dfr = lnLnk % Prt

        dvLnks = [[] for pr in range(Prt)]

        crNd = lnkLst.head

        for i in range(Prt):

            if i < dfr:
                crPrt = prt + 1
            else:
                crPrt = prt

            for pr in range(crPrt):

                if crNd:
                    crNd = crNd.nxt

            if crNd:
                crNd = crNd.nxt

        print(f"\t\tPart value: {prt}")
        print(f"\t\tDifferent parts: {dfr}")

        for i in range(Prt):
            dvds[i] = prt

        for i in range(dfr):
            dvds[i] += 1

        print(f"\t\tLinked list division: {dvds}")
        print()

        dvLnks = [[] for pr in range(Prt)]
        crLnks = Lnks

        for i, dv in enumerate(dvds):
            print(f"\t\t{dv}: {crLnks[:dv]}")

            dvLnks[i] = crLnks[:dv]
            crLnks = crLnks[dv:]
        print()

        print(f"\tDivided linked list: {dvLnks}")
        print()

        print(f"\tDivision parts:")
        for dv in dvLnks:
            print(f"\t\t{dv}")

        print("\n")
