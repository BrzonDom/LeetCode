"""
16. 3Sum Closest

https://leetcode.com/problems/3sum-closest/description/

    Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

    Return the sum of the three integers.

    You may assume that each input would have exactly one solution.


    Example 1:

        Input: nums = [-1, 2, 1, -4], target = 1
        Output: 2

        Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

    Example 2:

        Input: nums = [0, 0, 0], target = 1
        Output: 0

        Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).


    Constraints:

        3 <= nums.length <= 500
        -1000 <= nums[i] <= 1000
        -10^4 <= target <= 10^4

"""


import itertools


def Sol01A_TrpFrLp_Prt(InLst):

    for csCnt, case in enumerate(InLst):

        print(f"{csCnt + 1}. Case:\n")

        Nums = case[0]
        Trg = case[1]

        print(f"\tNumbers: {Nums}")
        print(f"\tTarget: {Trg}")
        print()

        clstDif = None
        clstTtl = None
        clstCmb = None
        clstFnd = False

        cmbCnt = 0

        for n1, num1 in enumerate(Nums[: -2]):
            if clstFnd:
                break

            for n2, num2 in enumerate(Nums[1 + n1: -1]):
                if clstFnd:
                    break

                for n3, num3 in enumerate(Nums[2 + n1 + n2:]):
                    ttl = num1 + num2 + num3
                    dif = abs(Trg - ttl)

                    print(f"\t\t{cmbCnt}.Cmb.: {num1} + {num2} + {num3}")
                    print(f"\t\t\tTotal:      {ttl}")
                    print(f"\t\t\tDifference: {dif}")
                    print()

                    if cmbCnt == 0:
                        clstDif = dif
                        clstTtl = ttl
                        clstCmb = [num1, num2, num3]

                    elif dif == 0:
                        clstDif = dif
                        clstTtl = ttl
                        clstCmb = [num1, num2, num3]

                        clstFnd = True
                        break

                    elif clstDif > dif:
                        clstDif = dif
                        clstTtl = ttl
                        clstCmb = [num1, num2, num3]

                    cmbCnt += 1

        print(f"\tClosest difference: {clstDif}")
        print(f"\tClosest total:      {clstTtl}")
        print(f"\t\tClosest combination: {clstCmb}")

        print("\n")


def Sol01_TrpFrLp_Prt(Nums, Trg):

    print(f"\tNumbers: {Nums}")
    print(f"\tTarget: {Trg}")
    print()

    clstDif = None
    clstTtl = None
    clstCmb = None
    clstFnd = False

    cmbCnt = 0

    for n1, num1 in enumerate(Nums[: -2]):
        if clstFnd:
            break

        for n2, num2 in enumerate(Nums[1 + n1: -1]):
            if clstFnd:
                break

            for n3, num3 in enumerate(Nums[2 + n1 + n2:]):
                ttl = num1 + num2 + num3
                dif = abs(Trg - ttl)

                print(f"\t\t{cmbCnt}.Cmb.: {num1} + {num2} + {num3}")
                print(f"\t\t\tTotal:      {ttl}")
                print(f"\t\t\tDifference: {dif}")
                print()

                if cmbCnt == 0:
                    clstDif = dif
                    clstTtl = ttl
                    clstCmb = [num1, num2, num3]

                elif dif == 0:
                    clstDif = dif
                    clstTtl = ttl
                    clstCmb = [num1, num2, num3]

                    clstFnd = True
                    break

                elif clstDif > dif:
                    clstDif = dif
                    clstTtl = ttl
                    clstCmb = [num1, num2, num3]

                cmbCnt += 1

    print(f"\tClosest difference: {clstDif}")
    print(f"\tClosest total:      {clstTtl}")
    print(f"\t\tClosest combination: {clstCmb}")

    print("\n")


def Sol02A_TlCmb_Prt(InLst):

    for csCnt, case in enumerate(InLst):

        print(f"{csCnt + 1}. Case:\n")

        Nums = case[0]
        Trg = case[1]

        print(f"\tNumbers: {Nums}")
        print(f"\tTarget: {Trg}")
        print()

        clstTtl = sum(Nums[:3])
        clstDfr = abs(Trg - clstTtl)
        clstCmb = Nums[:3]

        numCmb = itertools.combinations(Nums, 3)

        for cmbCnt, cmb in enumerate(numCmb):
            ttl = sum(cmb)
            dfr = abs(Trg - ttl)

            print(f"\t\t{cmbCnt}.Cmb.: {cmb[0]} + {cmb[1]} + {cmb[2]}")
            print(f"\t\t\tTotal:      {ttl}")
            print(f"\t\t\tDifference: {dfr}")
            print()

            if clstDfr > dfr:

                clstDfr = dfr
                clstTtl = ttl
                clstCmb = cmb

                if dfr == 0:
                    break

        print(f"\tClosest difference: {clstDfr}")
        print(f"\tClosest total:      {clstTtl}")
        print(f"\t\tClosest combination: {clstCmb}")

        print("\n")


def Sol02_TlCmb_Prt(case):

    Nums = case[0]
    Trg = case[1]

    print(f"\tNumbers: {Nums}")
    print(f"\tTarget: {Trg}")
    print()

    clstTtl = sum(Nums[:3])
    clstDfr = abs(Trg - clstTtl)
    clstCmb = Nums[:3]

    numCmb = itertools.combinations(Nums, 3)

    for cmbCnt, cmb in enumerate(numCmb):
        ttl = sum(cmb)
        dfr = abs(Trg - ttl)

        print(f"\t\t{cmbCnt}.Cmb.: {cmb[0]} + {cmb[1]} + {cmb[2]}")
        print(f"\t\t\tTotal:      {ttl}")
        print(f"\t\t\tDifference: {dfr}")
        print()

        if clstDfr > dfr:

            clstDfr = dfr
            clstTtl = ttl
            clstCmb = cmb

            if dfr == 0:
                break

    print(f"\tClosest difference: {clstDfr}")
    print(f"\tClosest total:      {clstTtl}")
    print(f"\t\tClosest combination: {clstCmb}")

    print("\n")


if __name__ == "__main__":

    InputLst = [[[-1, 2, 1, -4], 1],
                [[0, 0, 0], 1]]

    # Sol01A_TrpFrLp_Prt(InputLst)

    Sol02A_TlCmb_Prt(InputLst)

    # for csCnt, case in enumerate(InputLst):
    #
    #     print(f"{csCnt + 1}. Case:\n")

        # Sol01_TrpFrLp_Prt(case[0], case[1])

