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
    print()

    romNumOrg = romNum

    num = 0
    cnt = 0

    while True:

        while romNum[0] == 'M':
            romNum = romNum[1:]
            num += 1000
            cnt += 1

            if not len(romNum):
                print(f"\t\tM  = 1000 : {cnt} => num + {cnt * 1000} = {num}")
                cnt = 0
                break

            elif romNum[0] != 'M':
                print(f"\t\tM  = 1000 : {cnt} => num + {cnt*1000} = {num}")
                cnt = 0
                break

        if not len(romNum):
            break

        if romNum[:2] == "CM":
            romNum = romNum[2:]
            num += 900

            print(f"\t\tCM =  900 : 1 => num +  900 = {num}")

        if not len(romNum):
            break

        if romNum[:2] == "CD":
            romNum = romNum[2:]
            num += 400

            print(f"\t\tCD =  400 : 1 => num +  400 = {num}")

        if not len(romNum):
            break

        if romNum[0] == 'D':
            romNum = romNum[1:]
            num += 500

            print(f"\t\tD  =  500 : 1 => num +  500 = {num}")

        if not len(romNum):
            break

        while romNum[0] == 'C':
            romNum = romNum[1:]
            num += 100
            cnt += 1

            if not len(romNum):
                print(f"\t\tC  =  100 : {cnt} => num +  {cnt*100} = {num}")
                cnt = 0
                break

            elif romNum[0] != 'C':
                print(f"\t\tC  =  100 : {cnt} => num +  {cnt*100} = {num}")
                cnt = 0
                break

        if not len(romNum):
            break

        if romNum[:2] == "XC":
            romNum = romNum[2:]
            num += 90

            print(f"\t\tXC =   90 : 1 => num +   90 = {num}")

        if not len(romNum):
            break

        if romNum[:2] == "XL":
            romNum = romNum[2:]
            num += 40

            print(f"\t\tXL =   40 : 1 => num +   40 = {num}")

        if not len(romNum):
            break

        if romNum[0] == 'L':
            romNum = romNum[1:]
            num += 50

            print(f"\t\tL  =   50 : 1 => num +   50 = {num}")

        if not len(romNum):
            break

        while romNum[0] == 'X':
            romNum = romNum[1:]
            num += 10
            cnt += 1

            if not len(romNum):
                print(f"\t\tX  =   10 : {cnt} => num +   {cnt * 10} = {num}")
                cnt = 0
                break

            elif romNum[0] != 'C':
                print(f"\t\tX  =   10 : {cnt} => num +   {cnt * 10} = {num}")
                cnt = 0
                break

        if not len(romNum):
            break

        if romNum[:2] == "IX":
            romNum = romNum[2:]
            num += 9

            print(f"\t\tIX =    9 : 1 => num +    9 = {num}")

        if not len(romNum):
            break

        if romNum[:2] == "IV":
            romNum = romNum[2:]
            num += 4

            print(f"\t\tIV =    4 : 1 => num +    4 = {num}")

        if not len(romNum):
            break

        if romNum[0] == 'V':
            romNum = romNum[1:]
            num += 5

            print(f"\t\tV  =    5 : 1 => num +    5 = {num}")

        if not len(romNum):
            break

        while romNum[0] == 'I':
            romNum = romNum[1:]
            num += 1
            cnt += 1

            if not len(romNum):
                print(f"\t\tI  =    1 : {cnt} => num +    {cnt * 1} = {num}")
                break

        if not len(romNum):
            break

    print()
    print("\tRom. num.:", romNumOrg)

    print("\tNum.:     ", num)
    print("\n")

