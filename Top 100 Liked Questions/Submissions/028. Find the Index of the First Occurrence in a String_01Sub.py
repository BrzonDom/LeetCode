"""
28. Find the Index of the First Occurrence in a String

https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

    Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1
    if needle is not part of haystack.


    Example 1:

        Input: haystack = "sadbutsad", needle = "sad"
        Output: 0

        Explanation: "sad" occurs at index 0 and 6.
            The first occurrence is at index 0, so we return 0.

    Example 2:

        Input: haystack = "leetcode", needle = "leeto"
        Output: -1

        Explanation: "leeto" did not occur in "leetcode", so we return -1.


    Constraints:

        1 <= haystack.length, needle.length <= 10^4
        haystack and needle consist of only lowercase English characters.

"""


def Sol01A_InIndx_Prt(InLst):

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}. Case\n")

        Str = case[0]
        Sub = case[1]

        print(f"\tString: {Str}")
        print(f"\tSub-string: {Sub}")
        print()

        if Sub in Str:
            print(f"\tSub-string Found")
            print(f"\tFound at index: {Str.index(Sub)}")

        else:
            print(f"\tSub-string Not Found")

        print("\n")


def Sol01_InIndx_Prt(case):

    Str = case[0]
    Sub = case[1]

    print(f"\tString: {Str}")
    print(f"\tSub-string: {Sub}")
    print()

    if Sub in Str:
        print(f"\tSub-string Found")
        print(f"\tFound at index: {Str.index(Sub)}")

        subIdx = Str.index(Sub)

    else:
        print(f"\tSub-string Not Found")

        subIdx = -1

    print("\n")

    return subIdx


if __name__ == '__main__':

    InputLst = [["sadbutsad", "sad"],
                ["leetcode", "leeto"]]

    Sol01A_InIndx_Prt(InputLst)

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}. Case\n")

        Sol01_InIndx_Prt(case)
