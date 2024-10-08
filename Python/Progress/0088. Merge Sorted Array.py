"""
88. Merge Sorted Array

https://leetcode.com/problems/merge-sorted-array/description/


    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
    representing the number of elements in nums1 and nums2 respectively.

    Merge nums1 and nums2 into a single array sorted in non-decreasing order.

    The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
    To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be
    merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


    Example 1:

        Input: nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3

        Output: [1, 2, 2, 3, 5, 6]

        Explanation: The arrays we are merging are [1, 2, 3] and [2, 5, 6].
            The result of the merge is [1, 2, 2, 3, 5, 6] with the underlined elements coming from nums1.

    Example 2:

        Input: nums1 = [1], m = 1, nums2 = [], n = 0

        Output: [1]

        Explanation: The arrays we are merging are [1] and [].
            The result of the merge is [1].

    Example 3:

        Input: nums1 = [0], m = 0, nums2 = [1], n = 1

        Output: [1]

        Explanation: The arrays we are merging are [] and [1].
            The result of the merge is [1].
            Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result
            can fit in nums1.


    Constraints:

        nums1.length == m + n
        nums2.length == n
        0 <= m, n <= 200
        1 <= m + n <= 200
        -10^9 <= nums1[i], nums2[j] <= 10^9

"""
"""
    Tags:
    
        Array
        Two Pointers
        Sorting
    
"""


if __name__ == "__main__":

    InputLst = [[[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3],
                [[1], 1, [], 0],
                [[0], 0, [1], 1]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        Nmbs1 = case[0]
        LnN1 = case[1]
        Nmbs2 = case[2]
        LnN2 = case[3]

        print(f"\t1. Numbers: {Nmbs1}")
        print(f"\t\t1. Numbers length: {LnN1}")
        print()

        print(f"\t2. Numbers: {Nmbs2}")
        print(f"\t\t2. Numbers length: {LnN2}")
        print()

        print(f"\t\tOriginal numbers:   {Nmbs1[:LnN1]}")

        if Nmbs1[LnN1:]:
            print(f"\t\tAdditional spaces:  {Nmbs1[LnN1:]}")
            print(f"\t\tAdditional numbers: {Nmbs2}")
            print()

            Nmbs1[LnN1:] = Nmbs2

            print(f"\t\tAll numbers: {Nmbs1}")

            Nmbs1.sort()
        print()

        print(f"\tSorted numbers: {Nmbs1}")

        print("\n")
