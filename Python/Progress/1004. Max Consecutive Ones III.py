"""
1004. Max Consecutive Ones III

https://leetcode.com/problems/max-consecutive-ones-iii/description/


    Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can
    flip at most k 0's.


    Example 1:

        Input: nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2

        Output: 6

        Explanation: [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1]
            Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

    Example 2:

        Input: nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k = 3

        Output: 10

        Explanation: [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1]
            Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


    Constraints:

        1 <= nums.length <= 10^5
        nums[i] is either 0 or 1.
        0 <= k <= nums.length


    Topics:

        Array
        Binary Search
        Sliding Window
        Prefix Sum


    Courses:

        LeetCode 75

"""


if __name__ == "__main__":

    InputLst = [[[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2],
                [[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3],
                [[0, 0, 0, 1], 4]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        print(f"\tBinary Array: {case[0]}")
        print(f"\tFlips: {case[1]}")
        print()

        Bin_Arr = case[0]
        Flp = case[1]

        cur_sum = max_sum = 0
        cur_flp = Flp
        lft_ptr = rgh_ptr = 0

        while rgh_ptr < len(Bin_Arr):
            if Bin_Arr[rgh_ptr] == 0:
                cur_flp -= 1

            if cur_flp >= 0:
                cur_sum += 1
                rgh_ptr += 1
            else:
                print(f"\t\t{Bin_Arr[lft_ptr:rgh_ptr]}")
                max_sum = max(max_sum, cur_sum)

                cur_flp = Flp
                cur_sum = 0
                lft_ptr += 1
                rgh_ptr = lft_ptr

        print(f"\t\t{Bin_Arr[lft_ptr:rgh_ptr]}")
        max_sum = max(max_sum, cur_sum)

        print()
        print(f"\tMax Consecutive Ones: {max_sum}")

        print("\n")
