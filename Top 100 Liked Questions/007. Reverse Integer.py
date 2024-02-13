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