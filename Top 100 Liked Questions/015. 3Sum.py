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
            The distinct triplets are [-1,0,1] and [-1,-1,2].
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


def fndTrip_combSol(InLst):

    tripComb = combinations(InLst, 3)

    OutLst = []

    for trip in tripComb:
        if sum(trip) == 0:
            numI, numJ, numK = trip

            print(f"\t\t\t{numI:2} + {numJ:2} + {numK:2} = 0")

            trip = sorted(list(trip))

            if trip not in OutLst:
                OutLst.append(trip)

    print()

    print("\t\tOutput:")

    for Out in OutLst:
        print(f"\t\t\t{list(Out)}")

    return OutLst


Input_Lst = [[-1, 0, 1, 2, -1, -4],
             [0, 1, 1],
             [0, 0, 0]]

for case, InLst in enumerate(Input_Lst):

    print(f"\t{case+1}.Case:")
    print()

    print(f"\t\tList: {InLst}")
    print()

    # fndTrip_combSol(InLst)

    OutLst = []
    NumLst = sorted(InLst)

    for i, num in enumerate(NumLst):

        if num > 0:
            break

        if i != 0 and num == NumLst[i-1]:
            continue

        lft = i + 1
        rgt = len(NumLst) - 1

        while lft < rgt:
            tripSum = num + NumLst[lft] + NumLst[rgt]

            if tripSum > 0:
                rgt -= 1

            elif tripSum < 0:
                lft += 1

            else:
                trip = [num, NumLst[lft], NumLst[rgt]]
                OutLst.append(trip)

                lft += 1
                rgt -= 1

                while NumLst[lft] == NumLst[lft-1] and lft < rgt:
                    lft += 1

        for Out in OutLst:
            print(f"\t\t\t{list(Out)}")

    print("\n")
