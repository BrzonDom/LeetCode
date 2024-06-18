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


def Sol01_BackTrackGlob_Prt(csNum):

    def backtrack(prthCs, lftPrth, rgtPrth, prthNum):

        if len(prthCs) == 2 * prthNum:
            prnthComb.append(prthCs)

            return prnthComb

        if lftPrth < prthNum:
            backtrack(prthCs + '(', lftPrth + 1, rgtPrth, prthNum)

        if rgtPrth < lftPrth:
            backtrack(prthCs + ')', lftPrth, rgtPrth + 1, prthNum)


    print(f"{csNum}. Case\n")

    print(f"\tNum. of parentheses: {csNum}")

    parentExamp = ""

    for p in range(csNum):
        parentExamp += "()"

    print(f"\t\tParentheses: {parentExamp}")
    print()

    prnthComb = []
    backtrack("", 0, 0, csNum)

    print(f"\tNum. of valid combinations: {len(prnthComb)}")
    print("\tValid combinations:")

    print("\t\t", end="")
    for c, comb in enumerate(prnthComb):
        print(comb, end=", ")

        if (c + 1) % 5 == 0:
            print(f"\n\t\t", end="")

    print("\n")


def Sol01_BackTrackGlob(csNum):

    def backtrack(prthCs, lftPrth, rgtPrth, prthNum):

        if len(prthCs) == 2 * prthNum:
            prnthComb.append(prthCs)

            return prnthComb

        if lftPrth < prthNum:
            backtrack(prthCs + '(', lftPrth + 1, rgtPrth, prthNum)

        if rgtPrth < lftPrth:
            backtrack(prthCs + ')', lftPrth, rgtPrth + 1, prthNum)


    prnthComb = []
    backtrack("", 0, 0, csNum)


if __name__ == '__main__':

    InputLst = [3, 1]

    for csCnt in range(1, 9):

        Sol01_BackTrackGlob_Prt(csCnt)
