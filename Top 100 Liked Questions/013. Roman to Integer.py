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

    For example, 2 is written as II in Roman numeral, just two ones added together.
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
        """     While loop just for the print solutions
                    Stops evaluating when string is empty    """

        cnt = 0

        while romNum[0] == 'M':

            romNum = romNum[1:]
            num += 1000
            cnt += 1

            if not len(romNum):
                print(f"\t\tM  = {romCnvAll['M']:4} : {cnt} => num + {cnt * romCnvAll['M']:4} = {num}")
                cnt = 0
                break

            elif romNum[0] != 'M':
                print(f"\t\tM  = {romCnvAll['M']:4} : {cnt} => num + {cnt * romCnvAll['M']:4} = {num}")
                cnt = 0
                break

        if not len(romNum):
            break

        if romNum[:2] == "CM":
            """     C can be placed before M (1000) to 900.    """

            romNum = romNum[2:]
            num += 900

            print(f"\t\tCM = {romCnvAll['CM']:4} : 1 => num + {romCnvAll['CM']:4} = {num}")

        if not len(romNum):
            break

        if romNum[:2] == "CD":
            """     C can be placed before D (500) to make 400.    """

            romNum = romNum[2:]
            num += 400

            print(f"\t\tCD = {romCnvAll['CD']:4} : 1 => num + {romCnvAll['CD']:4} = {num}")

        if not len(romNum):
            break

        if romNum[0] == 'D':

            romNum = romNum[1:]
            num += 500

            print(f"\t\tD  = {romCnvAll['D']:4} : 1 => num + {romCnvAll['D']:4} = {num}")

        if not len(romNum):
            break

        while romNum[0] == 'C':

            romNum = romNum[1:]
            num += 100
            cnt += 1

            if not len(romNum):
                print(f"\t\tC  = {romCnvAll['C']:4} : {cnt} => num + {cnt * romCnvAll['C']:4} = {num}")
                cnt = 0
                break

            elif romNum[0] != 'C':
                print(f"\t\tC  = {romCnvAll['C']:4} : {cnt} => num + {cnt * romCnvAll['C']:4} = {num}")
                cnt = 0
                break

        if not len(romNum):
            break

        if romNum[:2] == "XC":
            """     X can be placed before C (100) to make 90.    """

            romNum = romNum[2:]
            num += 90

            print(f"\t\tXC = {romCnvAll['XC']:4} : 1 => num + {romCnvAll['XC']:4} = {num}")

        if not len(romNum):
            break

        if romNum[:2] == "XL":
            """     X can be placed before L (50) to make 40.    """

            romNum = romNum[2:]
            num += 40

            print(f"\t\tXL = {romCnvAll['XL']:4} : 1 => num + {romCnvAll['XL']:4} = {num}")

        if not len(romNum):
            break

        if romNum[0] == 'L':

            romNum = romNum[1:]
            num += 50

            print(f"\t\tL  = {romCnvAll['L']:4} : 1 => num + {romCnvAll['L']:4} = {num}")

        if not len(romNum):
            break

        while romNum[0] == 'X':

            romNum = romNum[1:]
            num += 10
            cnt += 1

            if not len(romNum):
                print(f"\t\tX  = {romCnvAll['X']:4} : {cnt} => num + {cnt * romCnvAll['X']:4} = {num}")
                cnt = 0
                break

            elif romNum[0] != 'X':
                print(f"\t\tX  = {romCnvAll['X']:4} : {cnt} => num + {cnt * romCnvAll['X']:4} = {num}")
                cnt = 0
                break

        if not len(romNum):
            break

        if romNum[:2] == "IX":
            """     I can be placed before X (10) to make 9.    """

            romNum = romNum[2:]
            num += 9

            print(f"\t\tIX = {romCnvAll['IX']:4} : 1 => num + {romCnvAll['IX']:4} = {num}")

        if not len(romNum):
            break

        if romNum[:2] == "IV":
            """     I can be placed before V (5) to make 4.    """

            romNum = romNum[2:]
            num += 4

            print(f"\t\tIV = {romCnvAll['IV']:4} : 1 => num + {romCnvAll['IV']:4} = {num}")

        if not len(romNum):
            break

        if romNum[0] == 'V':

            romNum = romNum[1:]
            num += 5

            print(f"\t\tV  = {romCnvAll['V']:4} : 1 => num + {romCnvAll['V']:4} = {num}")

        if not len(romNum):
            break

        while romNum[0] == 'I':

            romNum = romNum[1:]
            num += 1
            cnt += 1

            if not len(romNum):
                print(f"\t\tI  = {romCnvAll['I']:4} : {cnt} => num + {cnt * romCnvAll['I']:4} = {num}")
                break

        if not len(romNum):
            break

    print()
    print("\tRom. num.:", romNumOrg)

    print("\tNum.:     ", num)
    print("\n")


def romNumConvV1_Sol(romNum):

    num = 0

    while romNum[0] == 'M':

        romNum = romNum[1:]
        num += 1000

        if not len(romNum):
            return num

    if romNum[:2] == "CM":
        """     C can be placed before M (1000) to 900.    """

        romNum = romNum[2:]
        num += 900

        if not len(romNum):
            return num

    if romNum[:2] == "CD":
        """     C can be placed before D (500) to make 400.    """

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
        """     X can be placed before C (100) to make 90.    """

        romNum = romNum[2:]
        num += 90

        if not len(romNum):
            return num

    if romNum[:2] == "XL":
        """     X can be placed before L (50) to make 40.    """

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
        """     I can be placed before X (10) to make 9.    """

        romNum = romNum[2:]
        num += 9

        if not len(romNum):
            return num

    if romNum[:2] == "IV":
        """     I can be placed before V (5) to make 4.    """

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


def romNumConvV2_Sol(romNum):

    num = 0
    prev = ' '

    for symb in romNum:

        num += romCnv[symb]

        if prev == 'I' and (symb == 'X' or symb == 'V'):
            num -= 2

        if prev == 'X' and (symb == 'C' or symb == 'L'):
            num -= 20

        if prev == 'C' and (symb == 'D' or symb == 'M'):
            num -= 200

        prev = symb

    return num


romCnvAll = {
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

romCnv = {
            'I'  :    1,
            'V'  :    5,
            'X'  :   10,
            'L'  :   50,
            'C'  :  100,
            'D'  :  500,
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

print("1. Driver print solution:\n")

for romNum in Input_romNum:

    print("\tRom. num.:", romNum)
    print()

    romNumOrg = romNum

    num = 0

    while True:
        """     While loop just for the print solutions
                    Stops evaluating when string is empty    """

        cnt = 0

        while romNum[0] == 'M':
            romNum = romNum[1:]
            num += 1000
            cnt += 1

            if not len(romNum):
                print(f"\t\tM  = {romCnvAll['M']:4} : {cnt} => num + {cnt * romCnvAll['M']:4} = {num}")
                cnt = 0
                break

            elif romNum[0] != 'M':
                print(f"\t\tM  = {romCnvAll['M']:4} : {cnt} => num + {cnt * romCnvAll['M']:4} = {num}")
                cnt = 0
                break

        if not len(romNum):
            break

        if romNum[:2] == "CM":
            """     C can be placed before M (1000) to 900.    """
            romNum = romNum[2:]
            num += 900

            print(f"\t\tCM = {romCnvAll['CM']:4} : 1 => num + {romCnvAll['CM']:4} = {num}")

        if not len(romNum):
            break

        if romNum[:2] == "CD":
            """     C can be placed before D (500) to make 400.    """
            romNum = romNum[2:]
            num += 400

            print(f"\t\tCD = {romCnvAll['CD']:4} : 1 => num + {romCnvAll['CD']:4} = {num}")

        if not len(romNum):
            break

        if romNum[0] == 'D':
            romNum = romNum[1:]
            num += 500

            print(f"\t\tD  = {romCnvAll['D']:4} : 1 => num + {romCnvAll['D']:4} = {num}")

        if not len(romNum):
            break

        while romNum[0] == 'C':
            romNum = romNum[1:]
            num += 100
            cnt += 1

            if not len(romNum):
                print(f"\t\tC  = {romCnvAll['C']:4} : {cnt} => num + {cnt * romCnvAll['C']:4} = {num}")
                cnt = 0
                break

            elif romNum[0] != 'C':
                print(f"\t\tC  = {romCnvAll['C']:4} : {cnt} => num + {cnt * romCnvAll['C']:4} = {num}")
                cnt = 0
                break

        if not len(romNum):
            break

        if romNum[:2] == "XC":
            """     X can be placed before C (100) 90.    """
            romNum = romNum[2:]
            num += 90

            print(f"\t\tXC = {romCnvAll['XC']:4} : 1 => num + {romCnvAll['XC']:4} = {num}")

        if not len(romNum):
            break

        if romNum[:2] == "XL":
            """     X can be placed before L (50) to make 40.    """
            romNum = romNum[2:]
            num += 40

            print(f"\t\tXL = {romCnvAll['XL']:4} : 1 => num + {romCnvAll['XL']:4} = {num}")

        if not len(romNum):
            break

        if romNum[0] == 'L':
            romNum = romNum[1:]
            num += 50

            print(f"\t\tL  = {romCnvAll['L']:4} : 1 => num + {romCnvAll['L']:4} = {num}")

        if not len(romNum):
            break

        while romNum[0] == 'X':
            romNum = romNum[1:]
            num += 10
            cnt += 1

            if not len(romNum):
                print(f"\t\tX  = {romCnvAll['X']:4} : {cnt} => num + {cnt * romCnvAll['X']:4} = {num}")
                cnt = 0
                break

            elif romNum[0] != 'X':
                print(f"\t\tX  = {romCnvAll['X']:4} : {cnt} => num + {cnt * romCnvAll['X']:4} = {num}")
                cnt = 0
                break

        if not len(romNum):
            break

        if romNum[:2] == "IX":
            """     I can be placed before X (10) to make 9.    """
            romNum = romNum[2:]
            num += 9

            print(f"\t\tIX = {romCnvAll['IX']:4} : 1 => num + {romCnvAll['IX']:4} = {num}")

        if not len(romNum):
            break

        if romNum[:2] == "IV":
            """     I can be placed before V (5) to make 4.    """
            romNum = romNum[2:]
            num += 4

            print(f"\t\tIV = {romCnvAll['IV']:4} : 1 => num + {romCnvAll['IV']:4} = {num}")

        if not len(romNum):
            break

        if romNum[0] == 'V':
            romNum = romNum[1:]
            num += 5

            print(f"\t\tV  = {romCnvAll['V']:4} : 1 => num + {romCnvAll['V']:4} = {num}")

        if not len(romNum):
            break

        while romNum[0] == 'I':
            romNum = romNum[1:]
            num += 1
            cnt += 1

            if not len(romNum):
                print(f"\t\tI  = {romCnvAll['I']:4} : {cnt} => num + {cnt * romCnvAll['I']:4} = {num}")
                break

        if not len(romNum):
            break

    print()
    print("\tRom. num.:", romNumOrg)

    print("\tNum.:     ", num)
    print("\n")

print()
print("2. Driver solve solution:\n")

for romNum in Input_romNum:

    print("\tRom. num.:", romNum)

    num = 0
    prev = ' '

    for symb in romNum:

        num += romCnv[symb]

        if prev == 'I' and (symb == 'X' or symb == 'V'):
            """     I can be placed before V (5) and X (10) to make 4 and 9.    """

            """     Subtract 2 * I, because I was added on previous iteration   """
            num -= 2

        if prev == 'X' and (symb == 'C' or symb == 'L'):
            """     X can be placed before L (50) and C (100) to make 40 and 90.    """

            """     Subtract 2 * X, because X was added on previous iteration   """
            num -= 20

        if prev == 'C' and (symb == 'D' or symb == 'M'):
            """     C can be placed before D (500) and M (1000) to make 400 and 900.    """

            """     Subtract 2 * C, because C was added on previous iteration   """
            num -= 200

        prev = symb

    print("\tNum.:     ", num)
    print("\n")


print()
print("1. Function print solution:\n")

for romNum in Input_romNum:

    romNumConv_Prt(romNum)

print()
print("1. Function solve solution:\n")

for romNum in Input_romNum:

    print("\tRom. num.:", romNum)

    num = romNumConvV1_Sol(romNum)

    print("\tNum.:     ", num)
    print("\n")

print()
print("2. Function solve solution:\n")

for romNum in Input_romNum:

    print("\tRom. num.:", romNum)

    num = romNumConvV2_Sol(romNum)

    print("\tNum.:     ", num)
    print("\n")
