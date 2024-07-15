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


def Sol03_StrPntr(Nums):

    Nums.sort()
    lenNum = len(Nums)
    outCmb = []

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

            elif ttl > 0:
                rg -= 1

            else:
                if cmb not in outCmb:
                    outCmb.append(cmb)

                lf += 1
                rg -= 1

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

        outRtrn = Sol03_StrPntr_Prt(case)

        Out_Prt(outRtrn)
