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

"""

def comb_Print(inNumsLst):

    print("Combinations print:\n")

    for numLst in inNumsLst:
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


def twoSum_Sol01_Prt(inNumsLst):

    print("1.Function solution:\n")

    for numLst in inNumsLst:
        numArr = numLst[0]
        targ = numLst[1]

        print("\tNumbers array:", numArr)
        print("\t       Target:", targ)
        print()

        combFound = False

        for n1, num1 in enumerate(numArr):
            if combFound:
                break

            for n2, num2 in enumerate(numArr[n1+1:]):
                print(f"\t\t\t\tnums[{n1}] + nums[{n1+n2+1}] = {num1:2} + {num2:2} = {num1 + num2:2}")

                if num1 + num2 == targ:
                    print("\n\t\tFound combination:")
                    print(f"\t\t\tnums[{n1}] + nums[{n2}] = {num1:2} + {num2:2} = {num1 + num2:2}")

                    combFound = True
                    break
            print()
        print()


def twoSum_Sol02_Prt(inNumsLst):

    print("2.Function solution:\n")

    for numLst in inNumsLst:
        numArr = numLst[0]
        targ = numLst[1]

        print("\tNumbers array:", numArr)
        print("\t       Target:", targ)
        print()

        combFound = False

        for n1, num1 in enumerate(numArr):

            remain = targ - num1
            print(f"\t\t\t\tTarget - nums[{n1}] = {targ:2} - {num1:2} = {remain}")

            if remain in numArr[n1+1:]:
                num2 = remain
                n2 = numArr.index(num2, n1+1)

                print("\n\t\tFound combination:")
                print(f"\t\t\tnums[{n1}] + nums[{n2}] = {num1:2} + {num2:2} = {num1 + num2:2}")

                break
        print("\n")


if __name__ == '__main__':


    Input_numsLst = [[[2, 7, 11, 15], 9],
                     [[3, 2, 4], 6],
                     [[3, 3], 6],
                     [[3, 2, 3], 6]]

    comb_Print(Input_numsLst)

    twoSum_Sol01_Prt(Input_numsLst)

    twoSum_Sol02_Prt(Input_numsLst)
