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


def backtrack(prthCs, prnthLst, lftPrth, rgtPrth, csCnt):

    if len(prthCs) == 2 * csCnt:
        prnthLst.append(prthCs)

        return prnthLst

    if lftPrth < csCnt:
        prthCs += '('
        lftPrth += 1

        backtrack(prthCs, prnthLst, lftPrth, rgtPrth, csCnt)

    if rgtPrth < lftPrth:
        prthCs += ')'
        rgtPrth += 1

        backtrack(prthCs, prnthLst, lftPrth, rgtPrth, csCnt)


InputLst = [3, 1]

for csCnt in range(1, 9):

    print(f"{csCnt}. Case\n")

    print(f"\tNum. of parentheses: {csCnt}")

    parentLst = ""

    for p in range(csCnt):
        parentLst += "()"

    print(f"\t\tParentheses: {parentLst}")

    print("\n")