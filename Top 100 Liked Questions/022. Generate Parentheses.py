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


def Sol01_BackTrackGlob_Prt(csCnt):

    def backtrack(prthCs, lftPrth, rgtPrth, prthNum):

        if len(prthCs) == 2 * prthNum:
            prnthComb.append(prthCs)

            return prnthComb

        if lftPrth < prthNum:
            backtrack(prthCs + '(', lftPrth + 1, rgtPrth, prthNum)

        if rgtPrth < lftPrth:
            backtrack(prthCs + ')', lftPrth, rgtPrth + 1, prthNum)


    print(f"{csCnt}. Case\n")

    print(f"\tNum. of parentheses: {csCnt}")

    parentExamp = ""

    for p in range(csCnt):
        parentExamp += "()"

    print(f"\t\tParentheses: {parentExamp}")
    print()

    prnthComb = []
    backtrack("", 0, 0, csCnt)

    print(f"\tNum. of valid combinations: {len(prnthComb)}")
    print("\tValid combinations:")

    print("\t\t", end="")
    for c, comb in enumerate(prnthComb):
        print(comb, end=", ")

        if (c + 1) % 5 == 0:
            print(f"\n\t\t", end="")

    print("\n")


def Sol01A_BackTrackGlob_Prt():

    def backtrack(prthCs, lftPrth, rgtPrth, prthNum):

        if len(prthCs) == 2 * prthNum:
            prnthComb.append(prthCs)

            return prnthComb

        if lftPrth < prthNum:
            backtrack(prthCs + '(', lftPrth + 1, rgtPrth, prthNum)

        if rgtPrth < lftPrth:
            backtrack(prthCs + ')', lftPrth, rgtPrth + 1, prthNum)

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

        print(f"\tNum. of valid combinations: {len(prnthComb)}")
        print("\tValid combinations:")

        print("\t\t", end="")
        for c, comb in enumerate(prnthComb):
            print(comb, end=", ")

            if (c + 1) % 5 == 0:
                print(f"\n\t\t", end="")

        print("\n")


if __name__ == '__main__':
    InputLst = [3, 1]

    Sol01A_BackTrackGlob_Prt()
