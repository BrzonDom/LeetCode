"""
10. Regular Expression Matching

https://leetcode.com/problems/regular-expression-matching/

    Given an input string s and a pattern p, implement
    regular expression matching with support for '.' and '*' where:

        '.' Matches any single character.
        '*' Matches zero or more of the preceding element.

        The matching should cover the entire input string (not partial).

    Example 1:

        Input: s = "aa", p = "a"
        Output: false

        Explanation:
            "a" does not match the entire string "aa".

    Example 2:

        Input: s = "aa", p = "a*"
        Output: true

        Explanation:
            '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

    Example 3:

        Input: s = "ab", p = ".*"
        Output: true

        Explanation:
            ".*" means "zero or more (*) of any character (.)".

    Constraints:

        1 <= s.length <= 20
        1 <= p.length <= 20
        s contains only lowercase English letters.
        p contains only lowercase English letters, '.', and '*'.
        It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

"""


def regExpMatch_Prt(txt, pat):

    print("\tStr: ", txt)
    print("\tPat.:", pat)
    print()

    match = False

    for pS in range(len(pat)):
        # print("\t", pat[pS:])
        if match:
            break

        patS = pat[pS:]
        p = 0
        match = True

        for char in txt:

            if p >= len(patS):
                match = False
                break

            if char == patS[p]:
                p += 1

            elif patS[p] == '.':
                p += 1

            elif patS[p] == '*':

                if p - 1 >= 0:

                    if char == patS[p - 1]:
                        p += 0

                    elif patS[p - 1] == '.':
                        p += 0

                    else:
                        p += 1

                else:
                    match = False
                    break

            else:
                match = False
                break

    if match:
        print("\t\tStrings DO match")
        print("\t\t\tUsing pattern:", patS)
        print()

    else:
        print("\t\tStrings DON'T match")
        print()


InputLst = [["aa", "a"],
            ["aa", "a*"],
            ["ab", ".*"],
            ["aab", "c*a*b"],
            ["mississippi", "mis*is*ip*."],
            ["aabbb", "aab*"]]

for csCnt, case in enumerate(InputLst):

    print(f"{csCnt + 1}. Case\n")

    txt = case[0]
    pat = case[1]

    print("\tStr: ", txt)
    print("\tPat.:", pat)
    print()

    # match = False
    #
    # for pS in range(len(pat)):
    #     # print("\t", pat[pS:])
    #     if match:
    #         break
    #
    #     patS = pat[pS:]
    #     p = 0
    #     pDif = 0
    #     match = True
    #
    #     for char in txt:
    #         # debug_pat = patS[p]
    #
    #         if p >= len(patS):
    #             match = False
    #             break
    #
    #         if char == patS[p]:
    #             p += 1
    #
    #         elif patS[p] == '.':
    #             p += 1
    #
    #         elif patS[p] == '*':
    #
    #             if p-1 >= 0:
    #
    #                 if char == patS[p-1]:
    #                     pDif += 1
    #
    #                 elif patS[p-1] == '.':
    #                     pDif += 1
    #
    #                 else:
    #                     p += pDif + 1
    #                     pDif = 0
    #
    #             else:
    #                 match = False
    #                 break
    #
    #         else:
    #             match = False
    #             break
    #
    # if match:
    #     print("\t\tStrings DO match")
    #     print("\t\t\tUsing pattern:", patS)
    #     print("\n")
    #
    # else:
    #     print("\t\tStrings DON'T match")
    #     print("\n")
