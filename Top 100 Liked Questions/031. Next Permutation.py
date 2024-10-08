"""
31. Next Permutation

https://leetcode.com/problems/next-permutation/description/

    A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

    For example, for arr = [1, 2, 3], the following are all the permutations of arr: [1, 2, 3], [1, 3, 2], [2, 1, 3],
    [2, 3, 1], [3, 1, 2], [3, 2, 1].
    The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
    More formally, if all the permutations of the array are sorted in one container according to their lexicographical
    order, then the next permutation of that array is the permutation that follows it in the sorted container. If such
    arrangement is not possible, the array must be rearranged as the lowest possible order
    (i.e., sorted in ascending order).

        - For example, the next permutation of arr = [1, 2, 3] is [1, 3, 2].
        - Similarly, the next permutation of arr = [2, 3, 1] is [3, 1, 2].
        - While the next permutation of arr = [3, 2, 1] is [1, 2, 3] because [3, 2, 1] does not have a lexicographical
          larger rearrangement.

    Given an array of integers nums, find the next permutation of nums.

    The replacement must be in place and use only constant extra memory.

    Example 1:

        Input: nums = [1, 2, 3]
        Output: [1, 3, 2]

    Example 2:

        Input: nums = [3, 2, 1]
        Output: [1, 2, 3]

    Example 3:

        Input: nums = [1, 1, 5]
        Output: [1, 5, 1]


    Constraints:

        1 <= nums.length <= 100
        0 <= nums[i] <= 100

"""


from itertools import permutations


def Brt01_PrmTl_Prt(prmIn):

    print(f"\tInput permutation: {prmIn}")
    print()

    PrmsLst = list(permutations(prmIn, 3))

    print(f"\t\t\tAll unsorted unset permutations:")
    for pCnt, prm in enumerate(PrmsLst):
        print(f"\t\t\t\t{pCnt + 1}. {prm}")
    print()

    PrmsLst = list(set(PrmsLst))

    print(f"\t\t\tAll unsorted set permutations:")
    for pCnt, prm in enumerate(PrmsLst):
        print(f"\t\t\t\t{pCnt + 1}. {prm}")
    print()

    PrmsLst = sorted(PrmsLst)
    nxtPrms = {}

    print(f"\t\t\tAll sorted set permutations:")
    for pCnt, prm in enumerate(PrmsLst):
        print(f"\t\t\t\t{pCnt + 1}. {prm}")

        nxtPrms[str(prm)] = pCnt + 1
    nxtPrms[str(PrmsLst[-1])] = 0
    print()

    print(f"\t\tNext permutations:")
    for cntC, prmCr in enumerate(PrmsLst):
        nxIdx = nxtPrms[str(prmCr)]
        prmNx = PrmsLst[nxIdx]

        print(f"\t\t\t{cntC + 1}. {prmCr} => {prmNx}")
    print()

    otIdx = nxtPrms[str(tuple(prmIn))]
    prmOt = list(PrmsLst[otIdx])

    print(f"\tInput permutation:  {prmIn}")
    print(f"\tOutput permutation: {prmOt}")

    print("\n")

    return prmOt


def Sol01_RvsSwtch_Prt(Prm):

    print(f"\tInput permutation: {Prm}")
    print()

    pNm = Prm[-1]
    encNms = {Prm[-1] : -1}

    # print("\t\tEncountered numbers:")
    # print(f"\t\t\t{pNm} = Prm[{encNms[pNm]}]")

    mxPrm = True

    for i, nm in enumerate(Prm[-2::-1]):

        if nm not in encNms:
            encNms[nm] = -(i+2)
            # print(f"\t\t\t{nm} = Prm[{encNms[nm]}]")

        if pNm > nm:

            mNm = pNm

            mId = -(i+1)
            pId = -(i+1)
            cId = -(i+2)

            for eNm in encNms:
                if mNm > eNm > nm:
                    mNm = eNm
                    mId = encNms[mNm]

            print(f"\t\tMin. Num.: {mNm} = Prm[{mId}]")
            print(f"\t\tPrv. Num.: {Prm[pId]} = Prm[{pId}]")
            print(f"\t\tCrn. Num.: {Prm[cId]} = Prm[{cId}]")
            print()

            Prm[mId], Prm[cId] = Prm[cId], Prm[mId]
            Prm[pId:] = sorted(Prm[pId:])

            mxPrm = False
            break

        pNm = nm

    if mxPrm:
        Prm.reverse()

        print("\t\tMaximum permutation")
        print()

    print(f"\tOutput permutation: {Prm}")

    print(f"\n")

    return Prm


if __name__ == "__main__":

    InputLst = [[1, 2, 3],
                [1, 3, 2],
                [1, 1, 5],
                [1, 2, 3, 4],
                [4, 3, 2, 1],
                [1, 2, 4, 3, 1],
                [2, 3, 1],
                [2, 2, 7, 5, 4, 3, 2, 2, 1]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt+1}.Case\n")

        # Brt01_PrmTl_Prt(case)

        Sol01_RvsSwtch_Prt(case)
