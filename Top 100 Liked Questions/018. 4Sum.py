"""
18. 4Sum

https://leetcode.com/problems/4sum/description/

    Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c],
    nums[d]] such that:
        0 <= a, b, c, d < n
        a, b, c, and d are distinct.
        nums[a] + nums[b] + nums[c] + nums[d] == target

    You may return the answer in any order.

    Example 1:

        Input: nums = [1, 0, -1, 0, -2, 2], target = 0
        Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

    Example 2:

        Input: nums = [2, 2, 2, 2, 2], target = 8
        Output: [[2, 2, 2, 2]]


    Constraints:

        1 <= nums.length <= 200
        -10^9 <= nums[i] <= 10^9
        -10^9 <= target <= 10^9

"""


from itertools import combinations


def Brt01_QdrFrLp_Prt(Nums, Trgt):

    print(f"\tNumbers: {Nums}")
    print(f"\tTarget: {Trgt}")
    print()

    outCmb = []

    cmbCnt = 1
    notOut = True

    print(f"\t\tAll combinations:")
    for n1, num1 in enumerate(Nums[:-3]):
        for n2, num2 in enumerate(Nums[1+n1:-2]):
            for n3, num3 in enumerate(Nums[2+n1+n2:-1]):
                for n4, num4 in enumerate(Nums[3+n1+n2+n3:]):
                    cmb = [num1, num2, num3, num4]
                    ttl = sum(cmb)

                    if ttl == Trgt:

                        if cmb not in outCmb:
                            outCmb.append(cmb)

                        if notOut:
                            print()
                        print(f"\t\t\t{cmbCnt}.Cmb.: {cmb} = {ttl}")
                        print()

                        notOut = False

                    else:
                        print(f"\t\t\t\t{cmbCnt}.Cmb.: {cmb} = {ttl}")

                        notOut = True

                    cmbCnt += 1

    if notOut:
        print()

    return outCmb


def Brt02_TlCmb_Prt(Nums, Trgt):

    print(f"\tNumbers: {Nums}")
    print(f"\tTarget: {Trgt}")
    print()

    qdrCmb = combinations(Nums, 4)
    qdrCmb = map(list, qdrCmb)

    outCmb = []

    notOut = True

    print(f"\t\tAll combinations:")
    for cmbCnt, cmb in enumerate(qdrCmb):
        ttl = sum(cmb)

        if ttl == Trgt:

            if cmb not in outCmb:
                outCmb.append(cmb)

            if notOut:
                print()
            print(f"\t\t\t{cmbCnt+1}.Cmb.: {cmb} = {ttl}")
            print()

            notOut = False

        else:
            print(f"\t\t\t\t{cmbCnt+1}.Cmb.: {cmb} = {ttl}")

            notOut = True

    if notOut:
        print()

    return outCmb


def Out_Prt(outCmb):

    print(f"\tOut combinations:")
    if outCmb:
        for cmbCnt, cmb in enumerate(outCmb):
            print(f"\t\t{cmbCnt+1}. {cmb}")

    else:
        print(f"\t\tNone")

    print("\n")


if __name__ == "__main__":

    InputLst = [[[1, 0, -1, 0, -2, 2], 0],
                [[2, 2, 2, 2, 2], 8]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}. Case:\n")

        Nums = case[0]
        Trgt = case[1]

        print(f"\tNums unsorted: {Nums}")

        Nums.sort()
        print(f"\tNums sorted:   {Nums}")

        print(f"\tTarget: {Trgt}")
        print()

        lenNum = len(Nums)

        outCmb = []
        pFr = None

        cmbCnt = 1

        for fr in range(lenNum - 3):
            nFr = Nums[fr]

            if nFr == pFr:
                continue
            pFr = nFr

            pSc = None

            for sc in range(fr+1, lenNum - 2):
                nSc = Nums[sc]

                if nSc == pSc:
                    continue
                pSc = nSc

                lf = sc + 1
                rg = lenNum - 1

                while lf < rg:

                    nLf = Nums[lf]
                    nRg = Nums[rg]

                    cmb = [nFr, nSc, nLf, nRg]
                    ttl = sum(cmb)

                    if ttl < Trgt:
                        lf += 1

                        while nLf == Nums[lf] and lf < rg:
                            lf += 1

                        print(f"\t\t\t{cmbCnt}.Cmb.: {cmb} = {ttl}")

                    elif ttl > Trgt:
                        rg -= 1

                        while nRg == Nums[rg] and lf < rg:
                            rg -= 1

                        print(f"\t\t\t{cmbCnt}.Cmb.: {cmb} = {ttl}")

                    else:

                        outCmb.append(cmb)

                        lf += 1
                        while nLf == Nums[lf] and lf < rg:
                            lf += 1

                        rg -= 1
                        while nRg == Nums[rg] and lf < rg:
                            rg -= 1

                        print()
                        print(f"\t\t{cmbCnt}.Cmb.: {cmb} = {ttl}")
                        print()

                    cmbCnt += 1

        print("\n")

        # outRtrn = Brt01_QdrFrLp_Prt(case[0], case[1])

        # outRtrn = Brt02_TlCmb_Prt(case[0], case[1])

        # Out_Prt(outRtrn)
