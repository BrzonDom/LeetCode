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

InputLst = ["()",
            "()[]{}",
            "(]",
            "(([]{}))"]

for cs, prnths in enumerate(InputLst):

    print(f"{cs+1}. Case")
    print()

    print(f"\tParentheses: {prnths}")
    print()

    stckPrnth = []

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

            elif par == ']':
                if ']' == stckPrnth[0]:
                    stckPrnth = stckPrnth[1:]

            elif par == '}':
                if '}' == stckPrnth[0]:
                    stckPrnth = stckPrnth[1:]

            print("\t\t\t", stckPrnth)
            print()

        else:
            print("\t\tNo parentheses")
            break

    print("\n")