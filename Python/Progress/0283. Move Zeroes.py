"""
283. Move Zeroes

https://leetcode.com/problems/move-zeroes/description/


    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of
    the non-zero elements.

    Note that you must do this in-place without making a copy of the array.


    Example 1:

        Input: nums = [0, 1, 0, 3, 12]

        Output: [1, 3, 12, 0, 0]

    Example 2:

        Input: nums = [0]

        Output: [0]


    Constraints:

        1 <= nums.length <= 10^4
        -2^31 <= nums[i] <= 2^31 - 1


    Topics:

        Array
        Two Pointers


    Courses:

        LeetCode 75

"""


InputLst = [[0, 1, 0, 3, 12],
            [0]]

for csCnt, case in enumerate(InputLst):

    print(f"{csCnt + 1}.Case\n")

    print(f"\t{case}")

    print("\n")
