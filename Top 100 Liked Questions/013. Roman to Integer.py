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


def romNumConv_Prt(romNum):

    print("\tRom. num.:", romNum)
    print()

    romNumOrg = romNum

    num = 0

    while True:
        cnt = 0

        while romNum[0] == 'M':
            romNum = romNum[1:]
            num += 1000
            cnt += 1

            if not len(romNum):
                print(f"\t\tM  = {romCnv['M']:4} : {cnt} => num + {cnt * romCnv['M']:4} = {num}")
                cnt = 0
                break

            elif romNum[0] != 'M':
                print(f"\t\tM  = {romCnv['M']:4} : {cnt} => num + {cnt * romCnv['M']:4} = {num}")
                cnt = 0
                break

        if not len(romNum):
            break

        if romNum[:2] == "CM":
            romNum = romNum[2:]
            num += 900

            print(f"\t\tCM = {romCnv['CM']:4} : 1 => num + {romCnv['CM']:4} = {num}")

        if not len(romNum):
            break

        if romNum[:2] == "CD":
            romNum = romNum[2:]
            num += 400

            print(f"\t\tCD = {romCnv['CD']:4} : 1 => num + {romCnv['CD']:4} = {num}")

        if not len(romNum):
            break

        if romNum[0] == 'D':
            romNum = romNum[1:]
            num += 500

            print(f"\t\tD  = {romCnv['D']:4} : 1 => num + {romCnv['D']:4} = {num}")

        if not len(romNum):
            break

        while romNum[0] == 'C':
            romNum = romNum[1:]
            num += 100
            cnt += 1

            if not len(romNum):
                print(f"\t\tC  = {romCnv['C']:4} : {cnt} => num + {cnt * romCnv['C']:4} = {num}")
                cnt = 0
                break

            elif romNum[0] != 'C':
                print(f"\t\tC  = {romCnv['C']:4} : {cnt} => num + {cnt * romCnv['C']:4} = {num}")
                cnt = 0
                break

        if not len(romNum):
            break

        if romNum[:2] == "XC":
            romNum = romNum[2:]
            num += 90

            print(f"\t\tXC = {romCnv['XC']:4} : 1 => num + {romCnv['XC']:4} = {num}")

        if not len(romNum):
            break

        if romNum[:2] == "XL":
            romNum = romNum[2:]
            num += 40

            print(f"\t\tXL = {romCnv['XL']:4} : 1 => num + {romCnv['XL']:4} = {num}")

        if not len(romNum):
            break

        if romNum[0] == 'L':
            romNum = romNum[1:]
            num += 50

            print(f"\t\tL  = {romCnv['L']:4} : 1 => num + {romCnv['L']:4} = {num}")

        if not len(romNum):
            break

        while romNum[0] == 'X':
            romNum = romNum[1:]
            num += 10
            cnt += 1

            if not len(romNum):
                print(f"\t\tX  = {romCnv['X']:4} : {cnt} => num + {cnt * romCnv['X']:4} = {num}")
                cnt = 0
                break

            elif romNum[0] != 'X':
                print(f"\t\tX  = {romCnv['X']:4} : {cnt} => num + {cnt * romCnv['X']:4} = {num}")
                cnt = 0
                break

        if not len(romNum):
            break

        if romNum[:2] == "IX":
            romNum = romNum[2:]
            num += 9

            print(f"\t\tIX = {romCnv['IX']:4} : 1 => num + {romCnv['IX']:4} = {num}")

        if not len(romNum):
            break

        if romNum[:2] == "IV":
            romNum = romNum[2:]
            num += 4

            print(f"\t\tIV = {romCnv['IV']:4} : 1 => num + {romCnv['IV']:4} = {num}")

        if not len(romNum):
            break

        if romNum[0] == 'V':
            romNum = romNum[1:]
            num += 5

            print(f"\t\tV  = {romCnv['V']:4} : 1 => num + {romCnv['V']:4} = {num}")

        if not len(romNum):
            break

        while romNum[0] == 'I':
            romNum = romNum[1:]
            num += 1
            cnt += 1

            if not len(romNum):
                print(f"\t\tI  = {romCnv['I']:4} : {cnt} => num + {cnt * romCnv['I']:4} = {num}")
                break

        if not len(romNum):
            break

    print()
    print("\tRom. num.:", romNumOrg)

    print("\tNum.:     ", num)
    print("\n")


def romNumConv_Sol(romNum):

    num = 0

    while True:

        while romNum[0] == 'M':
            romNum = romNum[1:]
            num += 1000

            if not len(romNum):
                return num


        if romNum[:2] == "CM":
            romNum = romNum[2:]
            num += 900

            if not len(romNum):
                return num

        if romNum[:2] == "CD":
            romNum = romNum[2:]
            num += 400

            if not len(romNum):
                return num

        if romNum[0] == 'D':
            romNum = romNum[1:]
            num += 500

            if not len(romNum):
                return num

        while romNum[0] == 'C':
            romNum = romNum[1:]
            num += 100

            if not len(romNum):
                return num

        if romNum[:2] == "XC":
            romNum = romNum[2:]
            num += 90

            if not len(romNum):
                return num

        if romNum[:2] == "XL":
            romNum = romNum[2:]
            num += 40

            if not len(romNum):
                return num

        if romNum[0] == 'L':
            romNum = romNum[1:]
            num += 50

            if not len(romNum):
                return num

        while romNum[0] == 'X':
            romNum = romNum[1:]
            num += 10

            if not len(romNum):
                return num

        if romNum[:2] == "IX":
            romNum = romNum[2:]
            num += 9

            if not len(romNum):
                return num

        if romNum[:2] == "IV":
            romNum = romNum[2:]
            num += 4

            if not len(romNum):
                return num

        if romNum[0] == 'V':
            romNum = romNum[1:]
            num += 5

            if not len(romNum):
                return num

        while romNum[0] == 'I':
            romNum = romNum[1:]
            num += 1

            if not len(romNum):
                return num


romCnv = {
            'I'  :    1,
            'IV' :    4,
            'V'  :    5,
            'IX' :    9,
            'X'  :   10,
            'XL' :   40,
            'L'  :   50,
            'XC' :   90,
            'C'  :  100,
            'CD' :  400,
            'D'  :  500,
            'CM' :  900,
            'M'  : 1000
        }


Input_romNum = ["III", "LVIII", "MCMXCIV",
                "XIV", "XXXIX", "MCMLXXXIV", "MMXIV", "DCCXCVIII"]

"""
    3    = III
    58   = LVIII
    1994 = MCMXCIV
    14   = XIV
    39   = XXXIX
    1984 = MCMLXXXIV
    2014 = MMXIV
    798  = DCCXCVIII
"""

print("Driver print solution:\n")

for romNum in Input_romNum:
    print("\tRom. num.:", romNum)
    print()

    romNumOrg = romNum

    num = 0

    while True:
        cnt = 0

        while romNum[0] == 'M':
            romNum = romNum[1:]
            num += 1000
            cnt += 1

            if not len(romNum):
                print(f"\t\tM  = {romCnv['M']:4} : {cnt} => num + {cnt * romCnv['M']:4} = {num}")
                cnt = 0
                break

            elif romNum[0] != 'M':
                print(f"\t\tM  = {romCnv['M']:4} : {cnt} => num + {cnt * romCnv['M']:4} = {num}")
                cnt = 0
                break

        if not len(romNum):
            break

        if romNum[:2] == "CM":
            romNum = romNum[2:]
            num += 900

            print(f"\t\tCM = {romCnv['CM']:4} : 1 => num + {romCnv['CM']:4} = {num}")

        if not len(romNum):
            break

        if romNum[:2] == "CD":
            romNum = romNum[2:]
            num += 400

            print(f"\t\tCD = {romCnv['CD']:4} : 1 => num + {romCnv['CD']:4} = {num}")

        if not len(romNum):
            break

        if romNum[0] == 'D':
            romNum = romNum[1:]
            num += 500

            print(f"\t\tD  = {romCnv['D']:4} : 1 => num + {romCnv['D']:4} = {num}")

        if not len(romNum):
            break

        while romNum[0] == 'C':
            romNum = romNum[1:]
            num += 100
            cnt += 1

            if not len(romNum):
                print(f"\t\tC  = {romCnv['C']:4} : {cnt} => num + {cnt * romCnv['C']:4} = {num}")
                cnt = 0
                break

            elif romNum[0] != 'C':
                print(f"\t\tC  = {romCnv['C']:4} : {cnt} => num + {cnt * romCnv['C']:4} = {num}")
                cnt = 0
                break

        if not len(romNum):
            break

        if romNum[:2] == "XC":
            romNum = romNum[2:]
            num += 90

            print(f"\t\tXC = {romCnv['XC']:4} : 1 => num + {romCnv['XC']:4} = {num}")

        if not len(romNum):
            break

        if romNum[:2] == "XL":
            romNum = romNum[2:]
            num += 40

            print(f"\t\tXL = {romCnv['XL']:4} : 1 => num + {romCnv['XL']:4} = {num}")

        if not len(romNum):
            break

        if romNum[0] == 'L':
            romNum = romNum[1:]
            num += 50

            print(f"\t\tL  = {romCnv['L']:4} : 1 => num + {romCnv['L']:4} = {num}")

        if not len(romNum):
            break

        while romNum[0] == 'X':
            romNum = romNum[1:]
            num += 10
            cnt += 1

            if not len(romNum):
                print(f"\t\tX  = {romCnv['X']:4} : {cnt} => num + {cnt * romCnv['X']:4} = {num}")
                cnt = 0
                break

            elif romNum[0] != 'X':
                print(f"\t\tX  = {romCnv['X']:4} : {cnt} => num + {cnt * romCnv['X']:4} = {num}")
                cnt = 0
                break

        if not len(romNum):
            break

        if romNum[:2] == "IX":
            romNum = romNum[2:]
            num += 9

            print(f"\t\tIX = {romCnv['IX']:4} : 1 => num + {romCnv['IX']:4} = {num}")

        if not len(romNum):
            break

        if romNum[:2] == "IV":
            romNum = romNum[2:]
            num += 4

            print(f"\t\tIV = {romCnv['IV']:4} : 1 => num + {romCnv['IV']:4} = {num}")

        if not len(romNum):
            break

        if romNum[0] == 'V':
            romNum = romNum[1:]
            num += 5

            print(f"\t\tV  = {romCnv['V']:4} : 1 => num + {romCnv['V']:4} = {num}")

        if not len(romNum):
            break

        while romNum[0] == 'I':
            romNum = romNum[1:]
            num += 1
            cnt += 1

            if not len(romNum):
                print(f"\t\tI  = {romCnv['I']:4} : {cnt} => num + {cnt * romCnv['I']:4} = {num}")
                break

        if not len(romNum):
            break

    print()
    print("\tRom. num.:", romNumOrg)

    print("\tNum.:     ", num)
    print("\n")


print()
print("Function print solution:\n")

for romNum in Input_romNum:

    romNumConv_Prt(romNum)

print()
print("Function solve solution:\n")

for romNum in Input_romNum:

    print("\tRom. num.:", romNum)

    num = romNumConv_Sol(romNum)

    print("\tNum.:     ", num)
    print("\n")


