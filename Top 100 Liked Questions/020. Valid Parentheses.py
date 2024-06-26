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


def Sol01A_IfTreeList_Prt(inLst):

    for cs, prnths in enumerate(inLst):

        print(f"{cs+1}. Case")
        print()

        print(f"\tParentheses: {prnths}")
        print()

        stckPrnth = []
        wrngPrnth = False

        for par in prnths:

            if par in "([{":
                print(f"\t\t\"{par}\"\tLeft parentheses")

                if par == '(':
                    stckPrnth = [')'] + stckPrnth

                elif par == '[':
                    stckPrnth = [']'] + stckPrnth

                elif par == '{':
                    stckPrnth = ['}'] + stckPrnth

                print("\t\t\t", stckPrnth)
                print()

            elif par in ")]}":
                print(f"\t\t\"{par}\"\tRight parentheses")

                if par == ')':
                    if ')' == stckPrnth[0]:
                        stckPrnth = stckPrnth[1:]
                    else:
                        wrngPrnth = True
                        break

                elif par == ']':
                    if ']' == stckPrnth[0]:
                        stckPrnth = stckPrnth[1:]
                    else:
                        wrngPrnth = True
                        break

                elif par == '}':
                    if '}' == stckPrnth[0]:
                        stckPrnth = stckPrnth[1:]
                    else:
                        wrngPrnth = True
                        break

                print("\t\t\t", stckPrnth)
                print()

            else:
                print("\t\tNo parentheses")
                break

        if wrngPrnth:
            print()
            print("\tInvalid - Wrong parentheses")

        elif stckPrnth:
            print("\tInvalid - Not enough parentheses")

        else:
            print("\tValid")

        print("\n")


def Sol01_IfTreeList_Prt(prnths):

    print(f"\tParentheses: {prnths}")
    print()

    stckPrnth = []
    wrngPrnth = False

    for par in prnths:

        if par in "([{":
            print(f"\t\t\"{par}\"\tLeft parentheses")

            if par == '(':
                stckPrnth = [')'] + stckPrnth

            elif par == '[':
                stckPrnth = [']'] + stckPrnth

            elif par == '{':
                stckPrnth = ['}'] + stckPrnth

            print("\t\t\t", stckPrnth)
            print()

        elif par in ")]}":
            print(f"\t\t\"{par}\"\tRight parentheses")

            if par == ')':
                if ')' == stckPrnth[0]:
                    stckPrnth = stckPrnth[1:]
                else:
                    print()
                    print("\tInvalid - Wrong parentheses")

                    return False

            elif par == ']':
                if ']' == stckPrnth[0]:
                    stckPrnth = stckPrnth[1:]
                else:
                    print()
                    print("\tInvalid - Wrong parentheses")

                    return False

            elif par == '}':
                if '}' == stckPrnth[0]:
                    stckPrnth = stckPrnth[1:]
                else:
                    print()
                    print("\tInvalid - Wrong parentheses")

                    return False

            print("\t\t\t", stckPrnth)
            print()

        else:
            print("\t\tNo parentheses")
            break

    # if wrngPrnth:
    #     print()
    #     print("\tInvalid - Wrong parentheses")

    if stckPrnth:
        print("\tInvalid - Not enough parentheses")

        return False

    else:
        print("\tValid")

        return True


def Sol02A_IterQue_Prt(inLst):

    for csCnt, prnths in enumerate(inLst):
        print(f"{csCnt + 1}. Case")
        print()

        print(f"\tParentheses: {prnths}")
        print()

        stckPrnth = []
        wrngPrnth = False
        lessPrnth = False

        for par in prnths:

            if par == '(':
                stckPrnth.append(')')

                print(f"\t\t\"{par}\"\tLeft parentheses")
                print("\t\t\t", stckPrnth)

            elif par == '[':
                stckPrnth.append(']')

                print(f"\t\t\"{par}\"\tLeft parentheses")
                print("\t\t\t", stckPrnth)

            elif par == '{':
                stckPrnth.append('}')

                print(f"\t\t\"{par}\"\tLeft parentheses")
                print("\t\t\t", stckPrnth)

            elif not stckPrnth:
                print(f"\t\t\"{par}\"\tRight parentheses")
                print("\t\t\t", stckPrnth)

                return False

                # lessPrnth = True
                # break

            elif stckPrnth.pop() != par:
                print(f"\t\t\"{par}\"\tRight parentheses")
                print("\t\t\t", stckPrnth)

                return False

                # wrngPrnth = True
                # break

            else:
                print(f"\t\t\"{par}\"\tRight parentheses")
                print("\t\t\t", stckPrnth)

            print()

        print()

        if wrngPrnth:
            print("\tInvalid - Wrong parentheses")

            return False

        elif stckPrnth or lessPrnth:
            print("\tInvalid - Not enough parentheses")

            return False

        else:
            print("\tValid")

            return True

        # print("\n")


def Sol02_IterQue_Prt(prnths):

    # for csCnt, prnths in enumerate(inLst):
    #     print(f"{csCnt + 1}. Case")
    #     print()

    print(f"\tParentheses: {prnths}")
    print()

    stckPrnth = []
    wrngPrnth = False
    lessPrnth = False

    for par in prnths:

        if par == '(':
            stckPrnth.append(')')

            print(f"\t\t\"{par}\"\tLeft parentheses")
            print("\t\t\t", stckPrnth)

        elif par == '[':
            stckPrnth.append(']')

            print(f"\t\t\"{par}\"\tLeft parentheses")
            print("\t\t\t", stckPrnth)

        elif par == '{':
            stckPrnth.append('}')

            print(f"\t\t\"{par}\"\tLeft parentheses")
            print("\t\t\t", stckPrnth)

        elif not stckPrnth:
            print(f"\t\t\"{par}\"\tRight parentheses")
            print("\t\t\t", stckPrnth)

            lessPrnth = True
            break

        elif stckPrnth.pop() != par:
            print(f"\t\t\"{par}\"\tRight parentheses")
            print("\t\t\t", stckPrnth)

            wrngPrnth = True
            break

        else:
            print(f"\t\t\"{par}\"\tRight parentheses")
            print("\t\t\t", stckPrnth)

        print()

    print()

    if wrngPrnth:
        print("\tInvalid - Wrong parentheses")

    elif stckPrnth or lessPrnth:
        print("\tInvalid - Not enough parentheses")

    else:
        print("\tValid")

    print("\n")


if __name__ == '__main__':

    InputLst = ["()",
                "()[]{}",
                "(]",
                "(([]{}))",
                "([]{(}))"]

    # Sol01A_IfTreeList_Prt(InputLst)

    # for csCnt, case in enumerate(InputLst):
    #
    #     print(f"{csCnt+1}. Case")
    #     print()
    #
    #     Sol01_IfTreeList_Prt(case)
    #
    #     print("\n")


    # Sol02A_IterQue_Prt(InputLst)

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt+1}. Case")
        print()

        Sol02_IterQue_Prt(case)

        print("\n")
