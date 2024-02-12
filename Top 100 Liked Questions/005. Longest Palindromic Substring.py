"""
5. Longest Palindromic Substring

https://leetcode.com/problems/longest-palindromic-substring/description/

    Given a string s, return the longest palindromic substring in s.

    Example 1:

        Input: s = "babad"
        Output: "bab"
        Explanation: "aba" is also a valid answer.

    Example 2:

        Input: s = "cbbd"
        Output: "bb

    Constraints:

        1 <= s.length <= 1000
        s consist of only digits and English letters.
"""

Input_strLst = ["babad", "cbbd"]

print("Driver solution:\n")

for str in Input_strLst:

    print("\tString: ", str)
    print()

    for c in range(len(str)):
        print("\t\t", str[c:])
        # print("\t\t", end="")
        for s in range(1, len(str[c:])):
            print("\t\t", str[c:-s])

            pal = str[c:-s]
            pal = pal[::-1]

            if str[c:-s] == pal:
                print("\t\t\tPalindromic string:", pal)
        print()

    print("\n")