"""
5. Longest Palindromic Substring

https://leetcode.com/problems/longest-palindromic-substring/description/

    Given a string d, return the longest palindromic substring in d.

    Example 1:

        Input: d = "babad"
        Output: "bab"
        Explanation: "aba" is also a valid answer.

    Example 2:

        Input: d = "cbbd"
        Output: "bb

    Constraints:

        1 <= d.length <= 1000
        d consist of only digits and English letters.
"""

# def findPalStrV2_Prt(str):


def findPalStrV1_Prt(str):

    print("\tString: ", str)
    print()

    palLen = 0

    for c in range(len(str)):
        if len(str[c:]) > palLen:

            pal = str[c:]
            pal = pal[::-1]

            if str[c:] == pal:
                print("\t\t", pal)
                maxPal = pal
                palLen = len(pal)

            else:

                for d in range(1, len(str[c:])):
                    if len(str[c:-d]) > palLen:

                        pal = str[c:-d]
                        pal = pal[::-1]

                        if str[c:-d] == pal:
                            print("\t\t", pal)
                            maxPal = pal
                            palLen = len(pal)

    print()
    print("\t\tMax Pal.str.:", maxPal)

    return maxPal


Input_strLst = ["babad", "cbbd", "a", "bb"]

print("Driver combinations print:\n")

for str in Input_strLst:

    print("\tString: ", str)
    print()

    for c in range(len(str)):
        print("\t\t", str[c:], end="")
        # print("\t\t", end="")
        pal = str[c:]
        pal = pal[::-1]

        if str[c:] == pal:
            print("\t\tPalindromic string")
        else:
            print()

        for d in range(1, len(str[c:])):
            print("\t\t", str[c:-d], end="")

            pal = str[c:-d]
            pal = pal[::-1]

            if str[c:-d] == pal:
                print("\t\tPalindromic string")
            else:
                print()
        print()
    print()
print("\n")


print("1.Driver solution:\n")

for str in Input_strLst:

    print("\tString: ", str)
    print()

    palLen = 0

    for c in range(len(str)):
        if len(str[c:]) > palLen:

            pal = str[c:]
            pal = pal[::-1]

            if str[c:] == pal:
                print("\t\t", pal)
                maxPal = pal
                palLen = len(pal)

            else:

                for d in range(1, len(str[c:])):
                    if len(str[c:-d]) > palLen:

                        pal = str[c:-d]
                        pal = pal[::-1]

                        if str[c:-d] == pal:
                            print("\t\t", pal)
                            maxPal = pal
                            palLen = len(pal)

    print()
    print("\t\tMax Pal.str.:", maxPal)
    print("\n")


print("2. Driver solution:\n")

for s in Input_strLst:

    print("\tString: ", s, "\n")

    maxLen = 1
    maxPal = s[0]
    palFnd = True

    for ind, char in enumerate(s):

        l = ind
        r = ind

        curLen = 1

        while True:

            if l-1 >= 0 and r+1 < len(s) and s[l-1] == s[r+1]:

                print("\t\t", s[l-1:r+2])
                l -= 1
                r += 1
                curLen += 2
                continue

            if l == ind and r+1 < len(s) and s[r+1] == char:

                print("\t\t", s[l:r+2])
                r += 1
                curLen += 1
                continue

            break

        if curLen > maxLen:
            maxLen = curLen
            maxPal = s[l:r + 1]

    print()
    print("\t\tMax Pal.str.: ", maxPal, "\n")


print()
print("1. Function solution:\n")

for str in Input_strLst:

    maxPal = findPalStrV1_Prt(str)
    print()
    print("\t\t\tMax Pal.str.:", maxPal)
    print("\n")

