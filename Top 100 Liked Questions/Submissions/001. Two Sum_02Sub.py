"""
1. Two Sum

https://leetcode.com/problems/two-sum/description/

    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    Example 1:

        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]

    Example 2:

        Input: nums = [3,2,4], target = 6
        Output: [1,2]

    Example 3:

        Input: nums = [3,3], target = 6
        Output: [0,1]

    Constraints:

        2 <= nums.length <= 10^4
        -10^9 <= nums[i] <= 10^9
        -10^9 <= target <= 10^9
        Only one valid answer exists

"""


def comb_Print(inLst):

    print("Combinations print:\n")

    for numLst in inLst:
        numArr = numLst[0]
        targ = numLst[1]

        print("\tNumbers array:", numArr)
        print("\t       Target:", targ)
        print()

        for n1, num1 in enumerate(numArr):
            for n2, num2 in enumerate(numArr):
                if n1 != n2:
                    print(f"\t\tnums[{n1}] + nums[{n2}] = {num1:2} + {num2:2} = {num1 + num2:2}")
            print()
        print()


def Sol02_LoopRemain_Prt(numArr, targ):

    # print("2.Function solution:\n")

    # numArr = numLst[0]
    # targ = numLst[1]

    # print("\tNumbers array:", numArr)
    # print("\t       Target:", targ)
    # print()

    combFound = False

    for n1, num1 in enumerate(numArr):

        remain = targ - num1
        # print(f"\t\t\t\tTarget - nums[{n1}] = {targ:2} - {num1:2} = {remain}")

        if remain in numArr[n1+1:]:
            num2 = remain
            n2 = numArr.index(num2, n1+1)

            # print("\n\t\tFound combination:")
            # print(f"\t\t\tnums[{n1}] + nums[{n2}] = {num1:2} + {num2:2} = {num1 + num2:2}")

            break
    # print("\n")


if __name__ == '__main__':


    InputLst = [[[2, 7, 11, 15], 9],
                [[3, 2, 4], 6],
                [[3, 3], 6],
                [[3, 2, 3], 6]]

    # comb_Print(InputLst)

    for case in InputLst:
        numArr = case[0]
        targ = case[1]

        Sol02_LoopRemain_Prt(InputLst)
