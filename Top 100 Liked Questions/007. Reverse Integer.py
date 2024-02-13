"""
7. Reverse Integer

https://leetcode.com/problems/reverse-integer/description/

    Given a signed 32-bit integer x, return x with its digits reversed.
    If reversing x causes the value to go outside the signed
    32-bit integer range [-2³¹, 2³¹ - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

    Example 1:

        Input: x = 123
        Output: 321

    Example 2:

        Input: x = -123
        Output: -321

    Example 3:

        Input: x = 120
        Output: 21

    Constraints:

        -2³¹ <= x <= 2³¹ - 1
"""

Input_numLst = [123, -123, 120]

print("Driver print:\n")

for num in Input_numLst:
    print("\tNum.:", num)
    print("\n")


print("Driver solution:\n")

for num in Input_numLst:
    print("\tIn num.:", num)
    print()

    if num < 0:
        pol = -1
        strNum = str(num)[1:]

    elif num > 0:
        pol = 1
        strNum = str(num)

    else:
        print("\tOut num.:", num)
        print("\n")
        continue

    print("\t\tStr num.:", strNum)
    print()

    numOut = int(strNum[::-1])

    if pol == 1 and numOut < (2**31)-1:
        print("\tOut num.:", numOut)

    elif pol == -1 and numOut < (2**31):
        print("\tOut num.:", pol * numOut)
    else:
        print("\tOut num.:", 0)
        print("\t\tOut of int range !")

    print("\n")