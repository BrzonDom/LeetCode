"""
643. Maximum Average Subarray I

https://leetcode.com/problems/maximum-average-subarray-i/description/


    You are given an integer array nums consisting of n elements, and an integer k.

    Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
    Any answer with a calculation error less than 10^-5 will be accepted.


    Example 1:

        Input: nums = [1, 12, -5, -6, 50, 3], k = 4

        Output: 12.75000

        Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75


    Example 2:

        Input: nums = [5], k = 1

        Output: 5.00000


    Constraints:

        n == nums.length
        1 <= k <= n <= 10^5
        -10^4 <= nums[i] <= 10^4


    Topics:

        Array
        Sliding Window


    Courses:

        LeetCode 75

"""


def Brt01_FrLp_SldWndw_Prt(Nmbs, Rng):

    print(f"\tNumbers: {Nmbs}")
    print(f"\tRange: {Rng}")
    print()

    nmbs_sum = sum(Nmbs[:Rng])
    nmbs_avg = nmbs_sum / Rng

    print(f"\t\t{Nmbs[:Rng]}")
    print(f"\t\t\tSum: {nmbs_sum}")
    print(f"\t\t\tAvg: {nmbs_avg}")
    print()

    max_nmbs = Nmbs[:Rng]
    max_sum = sum(Nmbs[:Rng])
    max_avg = max_sum / Rng

    for i in range(1, len(Nmbs) - Rng + 1):
        nmbs_sum = sum(Nmbs[i: Rng + i])
        nmbs_avg = nmbs_sum / Rng

        print(f"\t\t{Nmbs[i: Rng + i]}")
        print(f"\t\t\tSum: {nmbs_sum}")
        print(f"\t\t\tAvg: {nmbs_avg}")

        if nmbs_avg > max_avg:
            max_nmbs = Nmbs[i: Rng + i]
            max_sum = nmbs_sum
            max_avg = nmbs_avg

    print(f"\tMax. numbers: {max_nmbs}")
    print(f"\tMax. sum: {max_sum}")
    print(f"\tMax. avg.: {max_avg}")

    return max_avg


if __name__ == "__main__":

    InputLst = [[[1, 12, -5, -6, 50, 3], 4],
                [[5], 1]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        Brt01_FrLp_SldWndw_Prt(case[0], case[1])

        print("\n")
