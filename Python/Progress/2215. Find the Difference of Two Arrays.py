"""
2215. Find the Difference of Two Arrays

https://leetcode.com/problems/find-the-difference-of-two-arrays/description/


    Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

        - answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
        - answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

    Note that the integers in the lists may be returned in any order.


    Example 1:

        Input:
            nums1 = [1, 2, 3],
            nums2 = [2, 4, 6]

        Output: [[1, 3], [4, 6]]

        Explanation:
            For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not
                present in nums2. Therefore, answer[0] = [1,3].
            For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not
                present in nums1. Therefore, answer[1] = [4,6].

    Example 2:

        Input:
            nums1 = [1, 2, 3, 3],
            nums2 = [1, 1, 2, 2]

        Output: [[3], []]

        Explanation:
            For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is
                only included once and answer[0] = [3].
            Every integer in nums2 is present in nums1. Therefore, answer[1] = [].


    Constraints:

        1 <= nums1.length, nums2.length <= 1000
        -1000 <= nums1[i], nums2[i] <= 1000


    Topics:

        Array
        Hash Table


    Courses:

        LeetCode 75

"""


if __name__ == '__main__':

    Input_Lst = [[[1, 2, 3],[2, 4, 6]],
                 [[1, 2, 3, 3],[1, 1, 2, 2]]]

    for cs_cnt, case in enumerate(Input_Lst, start=1):

        print(f"{cs_cnt}. Case\n")

        Nms_1 = case[0]
        Nms_2 = case[1]

        print(f"\t1. Number array: {Nms_1}")
        print(f"\t2. Number array: {Nms_2}")
        print()

        nms_1_set = set(Nms_1)
        nms_2_set = set(Nms_2)

        print(f"\t\t1. Number set: {nms_1_set}")
        print(f"\t\t2. Number set: {nms_2_set}")
        print()

        dist_nms_arr = [list(nms_1_set - nms_2_set),
                        list(nms_2_set - nms_1_set)]

        print(f"\t1. Distinct numbers: {dist_nms_arr[0]}")
        print(f"\t2. Distinct numbers: {dist_nms_arr[1]}")

        print("\n")
