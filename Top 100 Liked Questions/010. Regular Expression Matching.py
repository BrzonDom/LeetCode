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

    p = 0
    match = True

    for c, char in enumerate(txt):

        if p >= len(pat):
            match = False
            break

        if char == pat[p]:
            p += 1
            continue

        elif pat[p] == '.':
            p += 1
            continue

        elif pat[p] == '*':

            if char == pat[p - 1]:
                continue

            elif pat[p - 1] == '.':
                continue

        match = False

    if match:
        print("\t\tStrings DO match")
    else:
        print("\t\tStrings DON'T match")

    print("\n")


Input_strsLst = [["aa", "a"],
                 ["aa", "a*"],
                 ["ab", ".*"],
                 ["aabbb", "aab*"]]

print("Driver print:\n")

for strPat in Input_strsLst:

    txt = strPat[0]
    pat = strPat[1]

    print("\tStr: ", txt)
    print("\tPat.:", pat)
    print("\n")

print("Driver solution:\n")

for strPat in Input_strsLst:

    txt = strPat[0]
    pat = strPat[1]

    print("\tStr: ", txt)
    print("\tPat.:", pat)
    print()

    p = 0

    match = True

    for c, char in enumerate(txt):

        if p >= len(pat):
            match = False
            break

        if char == pat[p]:
            p += 1
            continue

        elif pat[p] == '.':
            p += 1
            continue

        elif pat[p] == '*':

            if char == pat[p-1]:
                continue

            elif pat[p-1] == '.':
                continue

        match = False

    if match:
        print("\t\tStrings DO match")
    else:
        print("\t\tStrings DON'T match")

    print("\n")

print("Function solution:\n")

for strPat in Input_strsLst:

    txt = strPat[0]
    pat = strPat[1]

    regExpMatch_Prt(txt, pat)
