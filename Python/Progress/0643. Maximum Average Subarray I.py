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


if __name__ == "__main__":

    InputLst = [[[1, 12, -5, -6, 50, 3], 4],
                [[5], 1]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        Nmbs = case[0]
        Rng = case[1]

        print(f"\tNumbers: {Nmbs}")
        print(f"\tRange: {Rng}")
        print()

        for i in range(len(Nmbs) - Rng + 1):
            nmbs_sum = sum(Nmbs[i: Rng + i])
            nmbs_avr = nmbs_sum / Rng

            print(f"\t{Nmbs[i: Rng + i]}")
            print(nmbs_sum)
            print(nmbs_avr)

        print("\n")
