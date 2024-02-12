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

# def findPalStr_Prt(str):
#



Input_strLst = ["babad", "cbbd", "a", "bb"]

print("Driver print:\n")

for str in Input_strLst:

    print("\tString: ", str)
    print()

    for c in range(len(str)):
        print("\t\t", str[c:])
        # print("\t\t", end="")

        for d in range(1, len(str[c:])):
            print("\t\t", str[c:-d])

            pal = str[c:-d]
            pal = pal[::-1]

            if str[c:-d] == pal:
                print("\t\t\tPalindromic string:", pal)
        print()
    print()
print()


print("Driver solution:\n")

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
