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

Input_Lst = [[-1, 0, 1, 2, -1, -4],
                [0, 1, 1],
                [0, 0, 0]]

print("Driver print:\n")

for case, InLst in enumerate(Input_Lst):

    print(f"\t{case+1}.Case:")
    print()

    print(f"\t\tList: {InLst}")
    print()

    # for indxI, numI in enumerate(InLst):
    #     for indxJ, numJ in enumerate(InLst[:indxI] + InLst[indxI+1:]):
    #         print(f"\t\t\t{numI:2} + {numJ:2} = {numI + numJ:2}")

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

    print("\n")