"""
145. Binary Tree Postorder Traversal

https://leetcode.com/problems/binary-tree-postorder-traversal/description/?envType=daily-question&envId=2024-08-25

        Day: 2024/08/25

    Given the root of a binary tree, return the postorder traversal of its nodes' values.


        Example 1:

            Input: root = [1, null, 2, 3]
            Output: [3, 2, 1]

        Example 2:

            Input: root = []
            Output: []

        Example 3:

            Input: root = [1]
            Output: [1]


        Constraints:

            The number of the nodes in the tree is in the range [0, 100].
            -100 <= Node.val <= 100

"""


InputLst = [[1, 0, 2, 3],
            [],
            [1]]

for csCnt, case in enumerate(InputLst):

    print(f"{csCnt + 1}.Case\n")

    BnTr = case

    print(f"\t{BnTr}")

    print("\n")
