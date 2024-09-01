"""
66. Plus One

https://leetcode.com/problems/plus-one/description/

    You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of
    the integer. The digits are ordered from most significant to least significant in left-to-right order.
    The large integer does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of digits.


    Example 1:

        Input: digits = [1, 2, 3]

        Output: [1, 2, 4]

        Explanation: The array represents the integer 123.
            Incrementing by one gives 123 + 1 = 124.
            Thus, the result should be [1, 2, 4].

    Example 2:

        Input: digits = [4, 3, 2, 1]

        Output: [4, 3, 2, 2]

        Explanation: The array represents the integer 4321.
            Incrementing by one gives 4321 + 1 = 4322.
            Thus, the result should be [4, 3, 2, 2].

    Example 3:

        Input: digits = [9]

        Output: [1, 0]

        Explanation: The array represents the integer 9.
            Incrementing by one gives 9 + 1 = 10.
            Thus, the result should be [1, 0].


    Constraints:

        1 <= digits.length <= 100
        0 <= digits[i] <= 9
        digits does not contain any leading 0's.

"""


def Slt01_TpCnvApp_Prt(InNmbLst):

    print(f"\tInput Number list: {InNmbLst}")
    print()

    inNmb = ""

    print("\t\tInput number:  ", end="")
    for dg in InNmbLst:
        print(dg, end="")

        inNmb += str(dg)
    print()

    inNmb = int(inNmb)
    otNmb = str(inNmb + 1)

    print(f"\t\tOutput number: {otNmb}")
    print()

    OtNmbLst = []

    for dg in str(otNmb):
        OtNmbLst.append(int(dg))

    print(f"\tOutput Number list: {OtNmbLst}")

    return OtNmbLst


def Slt02_LstItrAdd_Prt(NmbLst):

    print(f"\tInput Number list: {NmbLst}")

    nmDg = len(NmbLst)
    print(f"\t\tInput Number digits: {nmDg}")
    print()

    return


if __name__ == "__main__":

    InputLst = [[1, 2, 3],
                [4, 3, 2, 1],
                [9]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        # Slt01_TpCnvApp_Prt(case)

        NmbLst = case

        print(f"\tInput Number list: {NmbLst}")

        nmDg = len(NmbLst)
        print(f"\t\tInput Number digits: {nmDg}")
        print()

        fndItr = False

        for idx, dig in enumerate(NmbLst[::-1]):
            # print(InNmbLst[-(idx+1)], end="")

            if dig == 9:
                NmbLst[-(idx+1)] = 0

            else:
                NmbLst[-(idx+1)] = dig + 1

                fndItr = True
                break

        if not fndItr:
            NmbLst = [1] + NmbLst

        print(f"\tOutput Number list: {NmbLst}")

        print("\n")
