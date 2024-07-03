"""
16. 3Sum Closest

https://leetcode.com/problems/3sum-closest/description/

    Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

    Return the sum of the three integers.

    You may assume that each input would have exactly one solution.


    Example 1:

        Input: nums = [-1, 2, 1, -4], target = 1
        Output: 2

        Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

    Example 2:

        Input: nums = [0, 0, 0], target = 1
        Output: 0

        Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).


    Constraints:

        3 <= nums.length <= 500
        -1000 <= nums[i] <= 1000
        -10^4 <= target <= 10^4

"""

InputLst = [[[-1, 2, 1, -4], 1],
            [[0, 0, 0], 1]]

for csCnt, case in enumerate(InputLst):

    print(f"{csCnt + 1}. Case:\n")

    Nums = case[0]
    Trg = case[1]

    print(f"\tNumbers: {Nums}")
    print(f"\tTarget: {Trg}")
    print()

    for n1, num1 in enumerate(Nums[:2]):
        for n2, num2 in enumerate(Nums[1:]):
            for n3, num3 in enumerate(Nums):
                ttl = num1 + num2 + num3
                dif = abs(Trg - ttl)

                print(f"\t\t{num1} + {num2} + {num3}")
                print(f"\t\t\tTotal:      {ttl}")
                print(f"\t\t\tDifference: {dif}")
                print()

    print("\n")
