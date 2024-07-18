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

        cmbCnt = 1

        for fr in range(lnNm - 3):
            nFr = Nums[fr]

            for sc in range(fr + 1, lnNm - 2):
                nSc = Nums[sc]

                lf = sc + 1
                rg = lnNm - 1

                nLf = Nums[lf]
                nRg = Nums[rg]

                cmb = [nFr, nSc, nLf, nRg]

                print(f"\t\t{cmbCnt}.Cmb.: {cmb}")
                cmbCnt += 1

        print("\n")
