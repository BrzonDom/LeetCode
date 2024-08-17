"""
34. Find First and Last Position of Element in Sorted Array

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/


    Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of
    a given target value.

    If target is not found in the array, return [-1, -1].

    You must write an algorithm with O(log n) runtime complexity.


    Example 1:

        Input: nums = [5, 7, 7, 8, 8, 10], target = 8
        Output: [3, 4]

    Example 2:

        Input: nums = [5, 7, 7, 8, 8, 10], target = 6
        Output: [-1, -1]

    Example 3:

        Input: nums = [], target = 0
        Output: [-1, -1]


    Constraints:

        0 <= nums.length <= 10^5
        -10^9 <= nums[i] <= 10^9
        nums is a non-decreasing array.
        -10^9 <= target <= 10^9

"""


def Hlp_BnrSrch_NxtMd_Prt(Arr, Trg):

    ln = len(Arr)

    St = 0
    En = ln - 1
    Md = (St + En) // 2

    nSt = Arr[St]
    nEn = Arr[En]
    nMd = Arr[Md]

    return


if __name__ == "__main__":

    InputOrg = [[[5, 7, 7, 8, 8, 10], 8],
                [[5, 7, 7, 8, 8, 10], 6],
                [[], 0]]

    InputCstm = [[[1, 2, 3, 4, 4, 4, 4, 5, 6], 4],
                 [[2, 3, 3, 3, 3, 4, 5, 5, 6, 6, 6, 7, 8], 3]]

    InputLst = InputOrg + InputCstm

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt+1}.Case\n")

        Arr = case[0]
        Trg = case[1]

        print(f"\tArray: {Arr}")
        print(f"\tTarget: {Trg}")
        print()

        ln = len(Arr)
        print(f"\t\tLength: {ln}")
        print()

        if ln == 0:
            print("\tArray is empty")
            print("\n")

            continue

        St = 0
        En = ln - 1

        print("\tBinary Search:")
        print()

        trgFnd = False
        stpCnt = 0

        while St <= En:

            Md = (St + En) // 2

            nSt = Arr[St]
            nEn = Arr[En]
            nMd = Arr[Md]

            stpCnt += 1
            print(f"\t\t{stpCnt}. Start: {nSt} = Arr[{St}]")
            print(f"\t\t{stpCnt}. End:   {nEn} = Arr[{En}]")
            print(f"\t\t{stpCnt}. Mid:   {nMd} = Arr[{Md}]")
            print()

            if nMd == Trg:
                idBnS = [St, Md, En]

                trgFnd = True
                break

            if nMd < Trg:
                St = Md + 1

            elif nMd > Trg:
                En = Md - 1

        if trgFnd:

            rgTrg = idBnS[1]
            lfTrg = idBnS[1]

            St = idBnS[1] + 1
            En = idBnS[2]

            while St <= En:

                Md = (St + En) // 2

                nSt = Arr[St]
                nEn = Arr[En]
                nMd = Arr[Md]

                stpCnt += 1
                print(f"\t\t{stpCnt}. Start: {nSt} = Arr[{St}]")
                print(f"\t\t{stpCnt}. End:   {nEn} = Arr[{En}]")
                print(f"\t\t{stpCnt}. Mid:   {nMd} = Arr[{Md}]")
                print()

                if nMd == Trg:

                    rgTrg = Md

                    St = Md + 1
                    continue

                if nMd < Trg:
                    St = Md + 1

                elif nMd > Trg:
                    En = Md - 1

            St = idBnS[0]
            En = idBnS[1] - 1

            while St <= En:

                Md = (St + En) // 2

                nSt = Arr[St]
                nEn = Arr[En]
                nMd = Arr[Md]

                stpCnt += 1
                print(f"\t\t{stpCnt}. Start: {nSt} = Arr[{St}]")
                print(f"\t\t{stpCnt}. End:   {nEn} = Arr[{En}]")
                print(f"\t\t{stpCnt}. Mid:   {nMd} = Arr[{Md}]")
                print()

                if nMd == Trg:

                    lfTrg = Md

                    En = Md - 1
                    continue

                if nMd < Trg:
                    St = Md + 1

                elif nMd > Trg:
                    En = Md - 1

            print(f"\tTarget found on: {[lfTrg, rgTrg]}")

        else:
            print("\tTarget not found")

        print("\n")