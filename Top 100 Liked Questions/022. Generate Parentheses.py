"""
22. Generate Parentheses

https://leetcode.com/problems/generate-parentheses/description/

    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    Example 1:

        Input: n = 3
        Output: ["((()))","(()())","(())()","()(())","()()()"]

    Example 2:

        Input: n = 1
        Output: ["()"]


    Constraints:

        1 <= n <= 8

"""


def checkValPrth(prthStr):

    return


def backtrack(prthStr, prnthLst, lftPrth, rgtPrth, csCnt):

    return


InputLst = [3, 1]

for csCnt in range(1, 9):

    print(f"{csCnt}. Case\n")

    print(f"\tNum. of parentheses: {csCnt}")

    parentLst = ""

    for p in range(csCnt):
        parentLst += "()"

    print(f"\t\tParentheses: {parentLst}")

    print("\n")