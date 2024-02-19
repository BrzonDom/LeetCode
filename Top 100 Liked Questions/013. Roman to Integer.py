"""
13. Roman to Integer

https://leetcode.com/problems/roman-to-integer/description/

    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

        Symbol       Value
            I             1
            V             5
            X             10
            L             50
            C             100
            D             500
            M             1000

    For example, 2 is written as II in Roman numeral, just two one's added together.
    12 is written as XII, which is simply X + II.
    The number 27 is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right.
    However, the numeral for four is not IIII. Instead, the number four is
    written as IV. Because the one is before the five we subtract it making four.
    The same principle applies to the number nine, which is written as IX.
    There are six instances where subtraction is used:

        I can be placed before V (5) and X (10) to make 4 and 9.
        X can be placed before L (50) and C (100) to make 40 and 90.
        C can be placed before D (500) and M (1000) to make 400 and 900.

    Given a roman numeral, convert it to an integer.

    Example 1:

        Input: s = "III"
        Output: 3

        Explanation: III = 3.

    Example 2:

        Input: s = "LVIII"
        Output: 58

        Explanation: L = 50, V= 5, III = 3.

    Example 3:

        Input: s = "MCMXCIV"
        Output: 1994

        Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

    Constraints:

        1 <= s.length <= 15
        s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
        It is guaranteed that s is a valid roman numeral in the range [1, 3999].

"""

Input_romNum = ["III", "LVIII", "MCMXCIV"]

"""
    3    = III
    58   = LVIII
    1994 = MCMXCIV
"""

print("Driver print solution:\n")

for romNum in Input_romNum:
    print("\tRom. num.:", romNum)

    num = 0

    while True:

        while romNum[0] == 'M':
            romNum = romNum[1:]
            num += 1000

            if not len(romNum):
                break
        if not len(romNum):
            break

        if romNum[:2] == "CM":
            romNum = romNum[2:]
            num += 900

        if not len(romNum):
            break

        if romNum[:2] == "CD":
            romNum = romNum[2:]
            num += 400

        if not len(romNum):
            break

        if romNum[0] == 'D':
            romNum = romNum[1:]
            num += 500

        if not len(romNum):
            break

        while romNum[0] == 'C':
            romNum = romNum[1:]
            num += 100

            if not len(romNum):
                break
        if not len(romNum):
            break

        if romNum[:2] == "XC":
            romNum = romNum[2:]
            num += 90

        if not len(romNum):
            break

        if romNum[:2] == "XL":
            romNum = romNum[2:]
            num += 40

        if not len(romNum):
            break

        if romNum[0] == 'L':
            romNum = romNum[1:]
            num += 50

        if not len(romNum):
            break

        while romNum[0] == 'X':
            romNum = romNum[1:]
            num += 10

            if not len(romNum):
                break
        if not len(romNum):
            break

        if romNum[:2] == "IX":
            romNum = romNum[2:]
            num += 9

        if not len(romNum):
            break

        if romNum[:2] == "IV":
            romNum = romNum[2:]
            num += 4

        if not len(romNum):
            break

        if romNum[0] == 'V':
            romNum = romNum[1:]
            num += 5

        if not len(romNum):
            break

        while romNum[0] == 'I':
            romNum = romNum[1:]
            num += 1

            if not len(romNum):
                break
        if not len(romNum):
            break

    print("\tNum.:     ", num)
    print("\n")

