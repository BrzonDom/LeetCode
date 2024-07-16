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


InputLst = [[[1, 0, -1, 0, -2, 2], 0],
              [[2, 2, 2, 2, 2], 8]]

for csCnt, case in enumerate(InputLst):

    print(f"{csCnt + 1}. Case:\n")

    Nums = case[0]
    Trgt = case[1]

    print(f"\tNumbers: {Nums}")
    print(f"\tTarget: {Trgt}")
    print()

    outCmb = []
    cmbCnt = 1

    for n1, num1 in enumerate(Nums[:-3]):
        for n2, num2 in enumerate(Nums[1+n1:-2]):
            for n3, num3 in enumerate(Nums[2+n1+n2:-1]):
                for n4, num4 in enumerate(Nums[3+n1+n2+n3:]):
                    cmb = [num1, num2, num3, num4]
                    ttl = sum(cmb)

                    if ttl == Trgt:
                        outCmb.append(cmb)

                        print()
                        print(f"\t\t{cmbCnt}.Cmb.: {cmb} = {ttl}")
                        print()

                    else:
                        print(f"\t\t\t{cmbCnt}.Cmb.: {cmb} = {ttl}")

                    cmbCnt += 1
    print()

    for cmb in outCmb:
        print(f"\t\t{cmb}")

    print("\n")
