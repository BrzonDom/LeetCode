"""
15. 3Sum

https://leetcode.com/problems/3sum/description/

    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
    and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.

    Example 1:

        Input: nums = [-1, 0, 1, 2, -1, -4]
        Output: [[-1, -1, 2], [-1, 0, 1]]

        Explanation:
            nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
            nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
            nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
            The distinct triplets are [-1, 0, 1] and [-1, -1, 2].
            Notice that the order of the output and the order of the triplets does not matter.

    Example 2:

        Input: nums = [0, 1, 1]
        Output: []

        Explanation:
            The only possible triplet does not sum up to 0.

    Example 3:

        Input: nums = [0, 0, 0]
        Output: [[0, 0, 0]]

        Explanation:
            The only possible triplet sums up to 0.


    Constraints:

        3 <= nums.length <= 3000
        -10^5 <= nums[i] <= 10^5

"""
from itertools import combinations


def Sol01_TrpFrLp_Prt(Nums):

    print(f"\tNums: {Nums}")
    print()

    outCmb = []

    print(f"\t\tAll combinations:")
    cmbCnt = 1

    for n1, num1 in enumerate(Nums[:-2]):
        for n2, num2 in enumerate(Nums[1 + n1:-1]):
            for n3, num3 in enumerate(Nums[2 + n1 + n2:]):
                cmb = [num1, num2, num3]
                ttl = sum(cmb)

                if ttl == 0:
                    print()
                    print(f"\t\t\t{cmbCnt+1}.Cmb.: \t{cmb} = {ttl}")

                    cmb.sort()

                    if cmb not in outCmb:
                        print(f"\t\t\t\t{len(outCmb) + 1}.Out Combination: {cmb}")

                        outCmb.append(cmb)
                    else:
                        print(f"\t\t\t\tCombination already counted: {cmb}")
                    print()

                else:
                    print(f"\t\t\t\t{cmbCnt+1}.Cmb.: {cmb} = {ttl}")

                cmbCnt += 1
    print()

    return outCmb


def Sol02_TlCmb_Prt(Nums):

    print(f"\tNums: {Nums}")
    print()

    trpCmb = combinations(Nums, 3)
    trpCmb = map(list, trpCmb)

    outCmb = []

    print(f"\t\tAll combinations:")
    for cmbCnt, cmb in enumerate(trpCmb):
        ttl = sum(cmb)

        if ttl == 0:
            print()
            print(f"\t\t\t{cmbCnt + 1}.Cmb.: \t{cmb} = {ttl}")
            print()

            outCmb.append(cmb)

        else:
            print(f"\t\t\t\t{cmbCnt + 1}.Cmb.: \t{cmb} = {ttl}")

    print()

    return outCmb


def Sol03_StrPntr_Prt(Nums):

    print(f"\tNums unsorted: {Nums}")

    Nums.sort()
    print(f"\tNums sorted:   {Nums}")

    lenNum = len(Nums)
    print(f"\t\tNums size: {lenNum}")
    print()

    outCmb = []

    print(f"\t\tAll combinations:")
    for st in range(lenNum):
        nSt = Nums[st]

        lf = st + 1
        rg = lenNum - 1

        while lf < rg:
            nLf = Nums[lf]
            nRg = Nums[rg]

            cmb = [nSt, nLf, nRg]
            ttl = sum(cmb)

            if ttl < 0:
                lf += 1

                print(f"\t\t\t\t{cmb} = {ttl}")

            elif ttl > 0:
                rg -= 1

                print(f"\t\t\t\t{cmb} = {ttl}")

            else:
                if cmb not in outCmb:
                    outCmb.append(cmb)

                lf += 1
                rg -= 1

                print(f"\t\t\t{cmb}")
    print()

    return outCmb


def Out_Prt(outCmb):

    print(f"\tOut combinations:")
    if outCmb:
        for cmb in outCmb:
            print(f"\t\t{cmb}")

    else:
        print("\t\tNone")

    print("\n")


if __name__ == "__main__":

    InputLst = [[-1, 0, 1, 2, -1, -4],
                [0, 1, 1],
                [0, 0, 0],
                [-1, -2, -3, -4, -5, 0, 1, 4, 5, 2]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}. Case:\n")

        # outRtrn = Sol01_TrpFrLp_Prt(case)

        # outRtrn = Sol02_TlCmb_Prt(case)

        outRtrn = Sol03_StrPntr_Prt(case)

        Out_Prt(outRtrn)
