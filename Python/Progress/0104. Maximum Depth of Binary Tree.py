"""
104. Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

    Given the root of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


    Example 1:

        Input: root = [3, 9, 20, null, null, 15, 7]
        Output: 3

    Example 2:

        Input: root = [1, null, 2]
        Output: 2


    Constraints:

        The number of nodes in the tree is in the range [0, 10^4].
        -100 <= Node.val <= 100


    Topics:

        Tree
        Depth-First Search
        Breadth-First Search
        Binary Tree


    Courses:

        LeetCode 75

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


if __name__ == "__main__":

    Input_Lst = [[3, 9, 20, None, None, 15, 7],
                 [1, None, 2]]

    for cs_cnt, case in enumerate(Input_Lst, start=1):

        print(f"{cs_cnt}. Case\n")

        print(f"\t{case}")

        print("\n")
