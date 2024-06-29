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
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkList:
    def __init__(self):
        self.head = None

    def append(self, val):
        nwNode = ListNode(val)

        if self.head is None:
            self.head = nwNode

        else:
            crNode = self.head

            while crNode:
                crNode = crNode.next

            crNode.next = nwNode


InputLst = [[[2, 4, 3], [5, 6, 4]],
            [[0], [0]],
            [[9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]]]

for csCnt, case in enumerate(InputLst):

    print(f"{csCnt + 1}. Case\n")

    print(f"\t1.List: {case[0]}")
    print(f"\t2.List: {case[1]}")

    print("\n")
