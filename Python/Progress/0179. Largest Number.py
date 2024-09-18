"""
179. Largest Number

https://leetcode.com/problems/largest-number/description/


    Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

    Since the result may be very large, so you need to return a string instead of an integer.


    Example 1:

        Input: nums = [10, 2]

        Output: "210"

    Example 2:

        Input: nums = [3, 30, 34, 5, 9]

        Output: "9534330"


    Constraints:

        1 <= nums.length <= 100
        0 <= nums[i] <= 10^9


    Topics:

        Array
        String
        Greedy
        Sorting


    Course:

        Daily: 2024/09/18

"""


from itertools import permutations


def Brt01_PrmTl_Prt(Nmbs):

    print(f"\tNumbers: {Nmbs}")
    print()

    nmbPrms = permutations(Nmbs)

    mxNm = 0

    print("\t\tPermutations:")
    for prm in nmbPrms:

        crNm = ""

        for nm in prm:
            crNm += str(nm)

        if int(crNm) > mxNm:
            mxNm = int(crNm)

        print(f"\t\t\t{crNm}")
    print()

    print(f"\tMax Number: {mxNm}")

    return str(mxNm)


if __name__ == "__main__":

    InputLst = [[10, 2],
                [3, 30, 34, 5, 9]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        Brt01_PrmTl_Prt(case)

        # Nmbs = case
        #
        # print(f"\tNumbers: {Nmbs}")
        # print()
        #
        # nmbPrms = permutations(Nmbs)
        #
        # mxNm = 0
        #
        # print("\t\tPermutations:")
        # for prm in nmbPrms:
        #
        #     crNm = ""
        #
        #     for nm in prm:
        #         crNm += str(nm)
        #
        #     if int(crNm) > mxNm:
        #         mxNm = int(crNm)
        #
        #     print(f"\t\t\t{crNm}")
        # print()
        #
        # print(f"\tMax Number: {mxNm}")

        print("\n")
