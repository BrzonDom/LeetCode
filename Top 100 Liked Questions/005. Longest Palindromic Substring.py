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

def findPalStr_Sol(s):
    maxLen = 1
    maxPal = s[0]
    palFnd = True

    for ind, char in enumerate(s):

        l = ind
        r = ind

        curLen = 1

        while True:

            if l - 1 >= 0 and r + 1 < len(s) and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
                curLen += 2
                continue

            if l == ind and r + 1 < len(s) and s[r + 1] == char:
                r += 1
                curLen += 1
                continue

            break

        if curLen > maxLen:
            maxLen = curLen
            maxPal = s[l:r + 1]

    return maxPal


def findPalStrV2_Prt(s):
    """
        Idea:
            Tries to build the longest palindrome one letter at a time
            with continuously widening the sub-string
    """


    print("\tString: ", s, "\n")

    maxLen = 1
    maxPal = s[0]
    palFnd = True

    for ind, char in enumerate(s):
        """     Every character is set as the center of the palindrome  """

        l = ind
        r = ind

        curLen = 1

        while True:

            if l-1 >= 0 and r+1 < len(s) and s[l-1] == s[r+1]:
                """     For a case where both left and right indexes can be moved
                            If both left-1 and right+1 indexes fit into the string
                                and 
                            if str[left-1] character == str[right+1] character
                            the sub-string str[l-1:r+2] is a palindrome
                """

                print("\t\t", s[l-1:r+2])

                l -= 1
                r += 1
                curLen += 2
                continue

            if r+1 < len(s) and s[r+1] == char:
                """     For a case where the left index can't be moved more
                            If right+1 index fits into the string
                                and
                            if str[right+1] character == current character
                            the sub-string str[l:r+2] is a palindrome 
                """

                print("\t\t", s[l:r+2])

                r += 1
                curLen += 1
                continue

            """     If neither of the previous cases are True
                        we can move to the next character
                        as the center of a palindrome
            """

            break


        if curLen > maxLen:
            maxLen = curLen
            maxPal = s[l:r + 1]

    print()
    print("\t\tMax Pal.str.: ", maxPal, "\n")

    return maxPal


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


print("2. Function solution:\n")

for str in Input_strLst:

    maxPal = findPalStrV2_Prt(str)
    print("\t\t\tMax Pal.str.:", maxPal)
    print("\n")

