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


def backtrack(prthCs, lftPrth, rgtPrth, csCnt):

    if len(prthCs) == 2 * csCnt:
        prnthComb.append(prthCs)

        return prnthComb

    if lftPrth < csCnt:
        backtrack(prthCs + '(', lftPrth + 1, rgtPrth, csCnt)

    if rgtPrth < lftPrth:
        backtrack(prthCs + ')', lftPrth, rgtPrth + 1, csCnt)


InputLst = [3, 1]

for csCnt in range(1, 9):

    print(f"{csCnt}. Case\n")

    print(f"\tNum. of parentheses: {csCnt}")

    parentExamp = ""

    for p in range(csCnt):
        parentExamp += "()"

    print(f"\t\tParentheses: {parentExamp}")
    print()

    prnthComb = []
    backtrack("", 0, 0, csCnt)

    print("\t\tValid combinations:")

    print("\t\t\t", end="")
    for c, comb in enumerate(prnthComb):
        if (c + 1) % 5 == 0:
            print(comb)
            print(f"\t\t\t", end="")

        else:
            print(comb, end=", ")

    print("\n")