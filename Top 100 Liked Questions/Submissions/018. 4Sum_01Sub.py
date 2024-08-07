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


def Sol01_DblFrPntMtd_Prt(Nums, Trgt):

    print(f"\tNumbers unsorted: {Nums}")
    Nums.sort()
    print(f"\tNumbers sorted:   {Nums}")

    print(f"\tTarget: {Trgt}")
    print()

    lnNm = len(Nums)
    outCmb = []

    pFr = None

    cmbCnt = 1
    notOut = True

    print(f"\t\tAll combinations:")
    for fr in range(lnNm - 3):
        nFr = Nums[fr]

        if nFr == pFr:
            continue
        pFr = nFr
        pSc = None

        for sc in range(fr + 1, lnNm - 2):
            nSc = Nums[sc]

            if nSc == pSc:
                continue
            pSc = nSc

            lf = sc + 1
            rg = lnNm - 1

            while lf < rg:
                nLf = Nums[lf]
                nRg = Nums[rg]

                cmb = [nFr, nSc, nLf, nRg]
                ttl = sum(cmb)

                if ttl < Trgt:
                    lf += 1
                    while nLf == Nums[lf] and lf < rg:
                        lf += 1

                    print(f"\t\t\t\t{cmbCnt}.Cmb.: {cmb} = {ttl}")
                    notOut = True

                elif ttl > Trgt:
                    rg -= 1
                    while nRg == Nums[rg] and lf < rg:
                        rg -= 1

                    print(f"\t\t\t\t{cmbCnt}.Cmb.: {cmb} = {ttl}")
                    notOut = True

                else:
                    outCmb.append(cmb)

                    lf += 1
                    while nLf == Nums[lf] and lf < rg:
                        lf += 1

                    rg -= 1
                    while nRg == Nums[rg] and lf < rg:
                        rg -= 1

                    if notOut:
                        print()
                    print(f"\t\t\t{cmbCnt}.Cmb.: {cmb}")
                    print()
                    notOut = False

                cmbCnt += 1

    if notOut:
        print()

    return outCmb


def Sol01_DblFrPntMtd(Nums, Trgt):

    Nums.sort()
    lnNm = len(Nums)
    outCmb = []

    pFr = None

    for fr in range(lnNm - 3):
        nFr = Nums[fr]

        if nFr == pFr:
            continue
        pFr = nFr
        pSc = None

        for sc in range(fr + 1, lnNm - 2):
            nSc = Nums[sc]

            if nSc == pSc:
                continue
            pSc = nSc

            lf = sc + 1
            rg = lnNm - 1

            while lf < rg:
                nLf = Nums[lf]
                nRg = Nums[rg]

                cmb = [nFr, nSc, nLf, nRg]
                ttl = sum(cmb)

                if ttl < Trgt:
                    lf += 1
                    while nLf == Nums[lf] and lf < rg:
                        lf += 1

                elif ttl > Trgt:
                    rg -= 1
                    while nRg == Nums[rg] and lf < rg:
                        rg -= 1

                else:
                    outCmb.append(cmb)

                    lf += 1
                    while nLf == Nums[lf] and lf < rg:
                        lf += 1

                    rg -= 1
                    while nRg == Nums[rg] and lf < rg:
                        rg -= 1

    return outCmb


def Out_Prt(outCmb):

    print(f"\tOut combinations:")
    if outCmb:
        for cmbCnt, cmb in outCmb:
            print(f"\t\t{cmbCnt+1}. {cmb}")

    else:
        print("\t\tNone")


if __name__ == "__main__":

    InputLst = [[[1, 0, -1, 0, -2, 2], 0],
                [[2, 2, 2, 2, 2], 8]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}. Case:\n")

        out = Sol01_DblFrPntMtd_Prt(case[0], case[1])

        out = Sol01_DblFrPntMtd(case[0], case[1])

        Out_Prt(out)

        print("\n")
