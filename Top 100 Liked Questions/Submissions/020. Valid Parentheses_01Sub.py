"""
20. Valid Parentheses

https://leetcode.com/problems/valid-parentheses/description/

    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

    Example 1:

        Input: s = "()"
        Output: true

    Example 2:

        Input: s = "()[]{}"
        Output: true

    Example 3:

        Input: s = "(]"
        Output: false


    Constraints:

        1 <= s.length <= 104
        s consists of parentheses only '()[]{}'.

"""


def Sol01_IfTreeList_Prt(prnths):

    # print(f"\tParentheses: {prnths}")
    # print()

    stckPrnth = []
    wrngPrnth = False

    for par in prnths:

        if par in "([{":
            # print(f"\t\t\"{par}\"\tLeft parentheses")

            if par == '(':
                stckPrnth = [')'] + stckPrnth

            elif par == '[':
                stckPrnth = [']'] + stckPrnth

            elif par == '{':
                stckPrnth = ['}'] + stckPrnth

            # print("\t\t\t", stckPrnth)
            # print()

        elif par in ")]}":
            # print(f"\t\t\"{par}\"\tRight parentheses")

            if not stckPrnth:
                return False

            if par == ')':
                if ')' == stckPrnth[0]:
                    stckPrnth = stckPrnth[1:]
                else:
                    # print()
                    # print("\tInvalid - Wrong parentheses")

                    return False

            elif par == ']':
                if ']' == stckPrnth[0]:
                    stckPrnth = stckPrnth[1:]
                else:
                    # print()
                    # print("\tInvalid - Wrong parentheses")

                    return False

            elif par == '}':
                if '}' == stckPrnth[0]:
                    stckPrnth = stckPrnth[1:]
                else:
                    # print()
                    # print("\tInvalid - Wrong parentheses")

                    return False

            # print("\t\t\t", stckPrnth)
            # print()

        else:
            # print("\t\tNo parentheses")
            break

    # if wrngPrnth:
    #     print()
    #     print("\tInvalid - Wrong parentheses")

    if stckPrnth:
        # print("\tInvalid - Not enough parentheses")

        return False

    else:
        # print("\tValid")

        return True


if __name__ == '__main__':

    InputLst = ["()",
                "()[]{}",
                "(]",
                "(([]{}))",
                "([]{(}))"]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt+1}. Case")
        print()

        print(Sol01_IfTreeList_Prt(case))

        print("\n")
