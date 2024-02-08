"""
1342. Number of Steps to Reduce a Number to Zero

https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/

    Given an integer num, return the number of steps to reduce it to zero.

    In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.


    Example 1:

        Input: num = 14
        Output: 6

    Example 2:

        Input: num = 8
        Output: 4

    Example 3:

        Input: num = 123
        Output: 12

    Constraints:

        0 <= num <= 10^6
"""

Input_num = [14, 8, 123]

for num in Input_num:

    step = 0

    print(f"\tFor number: {num}")

    while (num > 0):
        if num % 2 == 0:
            num = num / 2
        else:
            num = num - 1
        step += 1

    print(f"\t\tSteps: {step}")