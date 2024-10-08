"""
2807. Insert Greatest Common Divisors in Linked List

https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/

        Daily: 2024/09/10


    Given the head of a linked list head, in which each node contains an integer value.

    Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

    Return the linked list after insertion.

    The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.


    Example 1:

        Input: head = [18, 6, 10, 3]

        Output: [18, 6, 6, 2, 10, 1, 3]

        Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after
            inserting the new nodes (nodes in blue are the inserted nodes).
            - We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
            - We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
            - We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
            There are no more adjacent nodes, so we return the linked list.

    Example 2:

        Input: head = [7]

        Output: [7]

        Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after
            inserting the new nodes.
            There are no pairs of adjacent nodes, so we return the initial linked list.


    Constraints:

        The number of nodes in the list is in the range [1, 5000].
        1 <= Node.val <= 1000


    Tags:

        Linked List
        Math
        Number Theory

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


def Hlp01_EclGCDItr_Prt(A, B):

    aNm = max(A, B)
    bNm = min(A, B)

    while bNm:
        rNm = aNm % bNm

        print(f"\t\t{aNm:2} % {bNm} = {rNm}")

        aNm = bNm
        bNm = rNm

    print(f"\t\t\tGCD({A:3}, {B:2}) = {aNm:2}")

    return aNm


def Hlp01_EclGCDItr(A, B):

    aNm = max(A, B)
    bNm = min(A, B)

    while bNm:
        rNm = aNm % bNm

        print(f"\t\t{aNm:2} % {bNm} = {rNm}")

        aNm = bNm
        bNm = rNm

    return aNm


if __name__ == "__main__":

    InputLst = [[18, 6, 10, 3],
                [7]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        Lnks = case
        lnLn = len(Lnks)

        print(f"\tLinked list values: {Lnks}")
        print(f"\t\tLength: {lnLn}")
        print()

        lnkLst = LinkList()

        for val in Lnks:
            lnkLst.add(val)

        crNd = lnkLst.head

        print("\t\tLinked list: ", end="[")
        while crNd:
            print(f"{crNd.val}", end="")

            crNd = crNd.nxt

            if crNd:
                print(", ", end="")
            else:
                print("]")
        print()

        if lnLn > 1:

            print("\tEuclidean algorithm:")
            for idx in range(lnLn - 1):

                Hlp01_EclGCDItr_Prt(Lnks[idx], Lnks[idx+1])
                print()

        print("\n")
