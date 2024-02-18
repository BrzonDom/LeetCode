"""
12. Integer to Roman

https://leetcode.com/problems/integer-to-roman/description/

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

    Given an integer, convert it to a roman numeral.

    Example 1:

        Input: num = 3
        Output: "III"

        Explanation: 3 is represented as 3 ones.

    Example 2:

        Input: num = 58
        Output: "LVIII"

        Explanation: L = 50, V = 5, III = 3.

    Example 3:

        Input: num = 1994
        Output: "MCMXCIV"

        Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

    Constraints:

        1 <= num <= 3999
"""

Input_numLst = [3, 58, 1994,
                14, 39, 1984, 2014, 798]


romCnv = {
       1 : 'I',
       5 : 'V',
      10 : 'X',
      50 : 'L',
     100 : 'C',
     500 : 'D',
    1000 : 'M' }

print("Roman numeral conversion:\n")

for decNum in romCnv:
    print(f"\t{decNum:>4} = {romCnv[decNum]}")
print("\n")

# for decNum in list(romCnv)[::-1]:
#
#     print(type(decNum), decNum)
# print()


print("Driver print:\n")

for num in Input_numLst:
    print("\tNum.: ", num)
    print()

    romNumCnt = {}

    for decNum in list(romCnv)[::-1]:

        if decNum <= num:
            romNumCnt[decNum] = 1

            num -= decNum
            while decNum <= num:
                romNumCnt[decNum] += 1
                num -= decNum

            print(f"\t\t{romCnv[decNum]} = {decNum:<4} : {romNumCnt[decNum]} =>", romNumCnt[decNum] * romCnv[decNum])

    print()
    print("\t\t", romNumCnt)
    print("\n")


    # if 1000 <= num:
    #     romNumCnt[1000] = 1
    #
    #     num -= 1000
    #     while 1000 <= num:
    #         romNumCnt[1000] += 1
    #         num -= 1000
    #
    #     print(f"\t\t{romCnv[1000]} = 1000 : {romNumCnt[1000]} =>", romNumCnt[1000] * romCnv[1000])
    #
    #
    # if 500 <= num:
    #     romNumCnt[500] = 1
    #
    #     num -= 500
    #     while 500 <= num:
    #         romNumCnt[500] += 1
    #         num -= 500
    #
    #     print(f"\t\t{romCnv[500]} = 500  : {romNumCnt[500]} =>", romNumCnt[500] * romCnv[500])
    #
    # if 100 <= num:
    #     romNumCnt[100] = 1
    #
    #     num -= 100
    #     while 100 <= num:
    #         romNumCnt[100] += 1
    #         num -= 100
    #
    #     print(f"\t\t{romCnv[100]} = 100  : {romNumCnt[100]} =>", romNumCnt[100] * romCnv[100])
    #
    # if 50 <= num:
    #     romNumCnt[50] = 1
    #
    #     num -= 50
    #     while 50 <= num:
    #         romNumCnt[50] += 1
    #         num -= 50
    #
    #     print(f"\t\t{romCnv[50]} = 50   : {romNumCnt[50]} =>", romNumCnt[50] * romCnv[50])
    #
    # if 10 <= num:
    #     romNumCnt[10] = 1
    #
    #     num -= 10
    #     while 10 <= num:
    #         romNumCnt[10] += 1
    #         num -= 10
    #
    #     print(f"\t\t{romCnv[10]} = 10   : {romNumCnt[10]} =>", romNumCnt[10] * romCnv[10])
    #
    # if 5 <= num:
    #     romNumCnt[5] = 1
    #
    #     num -= 5
    #     while 5 <= num:
    #         romNumCnt[5] += 1
    #         num -= 5
    #
    #     print(f"\t\t{romCnv[5]} = 5    : {romNumCnt[5]} =>", romNumCnt[5] * romCnv[5])
    #
    # if 1 <= num:
    #     romNumCnt[1] = 1
    #
    #     num -= 1
    #     while 1 <= num:
    #         romNumCnt[1] += 1
    #         num -= 1
    #
    #     print(f"\t\t{romCnv[1]} = 1    : {romNumCnt[1]} =>", romNumCnt[1] * romCnv[1])

    # print()
    # print("\t\t", romNumCnt)
    # print("\n")

print()
print("Driver solution:\n")

for num in Input_numLst:
    print("\tNum.: ", num)
    print()

    romNumCnt = {}
    romNum = ""

    """ 
        Roman numeral, subtraction cases:
    
            I can be placed before V (5) and X (10) to make 4 and 9.
            X can be placed before L (50) and C (100) to make 40 and 90.
            C can be placed before D (500) and M (1000) to make 400 and 900.
    """


    if 1000 <= num:
        romNumCnt[1000] = 1

        num -= 1000
        while 1000 <= num:
            romNumCnt[1000] += 1
            num -= 1000

        print(f"\t\t{romCnv[1000]} = 1000 : {romNumCnt[1000]} =>", romNumCnt[1000] * romCnv[1000])


    if 500 <= num:
        romNumCnt[500] = 1

        num -= 500
        # while 500 <= num:
        #     romNumCnt[500] += 1
        #     num -= 500

        print(f"\t\t{romCnv[500]} = 500  : {romNumCnt[500]} =>", romNumCnt[500] * romCnv[500])

    if 100 <= num:
        romNumCnt[100] = 1

        num -= 100
        while 100 <= num:
            romNumCnt[100] += 1
            num -= 100

        """     C can be placed before D (500) and M (1000) to make 400 and 900.    """
        if romNumCnt[100] == 4 and 500 in romNumCnt:
            print(f"\t\t{romCnv[100]} = 100  : {romNumCnt[100]} ( + {romCnv[500]} = 500) => CM")

        elif romNumCnt[100] == 4:
            print(f"\t\t{romCnv[100]} = 100  : {romNumCnt[100]} => CD")

        else:
            print(f"\t\t{romCnv[100]} = 100  : {romNumCnt[100]} =>", romNumCnt[100] * romCnv[100])


    if 50 <= num:
        romNumCnt[50] = 1

        num -= 50
        # while 50 <= num:
        #     romNumCnt[50] += 1
        #     num -= 50

        print(f"\t\t{romCnv[50]} = 50   : {romNumCnt[50]} =>", romNumCnt[50] * romCnv[50])

    if 10 <= num:
        romNumCnt[10] = 1

        num -= 10
        while 10 <= num:
            romNumCnt[10] += 1
            num -= 10

        """     X can be placed before L (50) and C (100) to make 40 and 90.    """
        if romNumCnt[10] == 4 and 50 in romNumCnt:
            print(f"\t\t{romCnv[10]} = 10   : {romNumCnt[10]} ( + {romCnv[50]} = 50) => XC")

        elif romNumCnt[10] == 4:
            print(f"\t\t{romCnv[10]} = 10   : {romNumCnt[10]} => XL")

        else:
            print(f"\t\t{romCnv[10]} = 10   : {romNumCnt[10]} =>", romNumCnt[10] * romCnv[10])

    if 5 <= num:
        romNumCnt[5] = 1

        num -= 5
        # while 5 <= num:
        #     romNumCnt[5] += 1
        #     num -= 5

        print(f"\t\t{romCnv[5]} = 5    : {romNumCnt[5]} =>", romNumCnt[5] * romCnv[5])

    if 1 <= num:
        romNumCnt[1] = 1

        num -= 1
        while 1 <= num:
            romNumCnt[1] += 1
            num -= 1

        """     I can be placed before V (5) and X (10) to make 4 and 9.    """
        if romNumCnt[1] == 4 and 5 in romNumCnt:
            print(f"\t\t{romCnv[1]} = 1    : {romNumCnt[1]} ( + {romCnv[10]} = 10) => IX")

        elif romNumCnt[1] == 4:
            print(f"\t\t{romCnv[1]} = 1    : {romNumCnt[1]} => IV")

        else:
            print(f"\t\t{romCnv[1]} = 1    : {romNumCnt[1]} =>", romNumCnt[1] * romCnv[1])

    print()
    print("\t\t", romNumCnt)
    print("\n")

