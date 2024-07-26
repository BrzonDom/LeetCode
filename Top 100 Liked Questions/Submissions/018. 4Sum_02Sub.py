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


def Hlp02_nSumPntMtd_Ptr(rmNmCr, trgtCr, shftCr, cmbCr):

    if rmNmCr == 2:

        lf = shftCr
        rg = len(Nums) - 1

        while lf < rg:

            nLf = Nums[lf]
            nRg = Nums[rg]

            cmbNx = cmbCr + [nLf, nRg]
            ttl = sum(cmbNx)

            print(f"\t\t\t{cmbNx} = {ttl}")

            if ttl < Trgt:
                lf += 1

                while nLf == Nums[lf] and lf < rg:
                    lf += 1

            elif ttl > Trgt:
                rg -= 1

                while nRg == Nums[rg] and lf < rg:
                    rg -= 1

            else:

                if cmbNx not in outCmb:
                    outCmb.append(cmbNx)

                lf += 1
                rg -= 1

    else:
        pNum = None

        for n, num in enumerate(Nums[shftCr:-2]):

            if num == pNum:
                continue
            pNum = num

            rmNmNx = rmNmCr - 1
            trgtNx = trgtCr - num
            shftNx = shftCr + n + 1
            cmbNx = cmbCr + [num]

            Hlp02_nSumPntMtd_Ptr(rmNmNx, trgtNx, shftNx, cmbNx)


if __name__ == "__main__":

    InputLst = [[[1, 0, -1, 0, -2, 2], 0],
                [[2, 2, 2, 2, 2], 8]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}. Case:\n")

        Nums = case[0]
        print(f"\tNumbers unsorted: {Nums}")

        Nums.sort()
        print(f"\tNumbers sorted:   {Nums}")

        Trgt = case[1]
        print(f"\tTarget: {Trgt}")
        print()

        lnNm = len(Nums)

        outCmb = []

        print(f"\t\tAll combinations:")
        Hlp02_nSumPntMtd_Ptr(4, Trgt, 0, [])
        print()

        print(f"\tOut combinations:")
        if outCmb:
            for cmb in outCmb:
                print(f"\t\t{cmb}")

        else:
            print("\t\tNone")

        print("\n")
