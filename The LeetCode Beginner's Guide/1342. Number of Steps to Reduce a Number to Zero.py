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

def NumOfSteps_Sol(num):
    step = 0

    while (num != 0):
        step += 1

        if num % 2 == 0:
            num /= 2

        else:
            num -= 1

    return step


def NumOfSteps_Prt(num):

    step = 0

    print(f"\t\tFor number: {num}\n")

    while (num > 0):
        step += 1

        if num % 2 == 0:
            print(f"\t\t\t\t{step:2}. {num:2} -> {num:2} / 2 = {num//2:2}")
            num = num // 2
        else:
            print(f"\t\t\t\t{step:2}. {num:2} -> {num:2} - 1 = {num-1:2}")
            num = num - 1

    print(f"\n\t\t\tSteps: {step}")

    return step


Input_num = [14, 8, 123]

print("Driver solution:\n")

for num in Input_num:

    step = 0

    print(f"\t\tFor number: {num}\n")

    while (num > 0):
        step += 1

        if num % 2 == 0:
            print(f"\t\t\t\t{step:2}. {num:2} -> {num:2} / 2 = {num//2:2}")
            num = num // 2
        else:
            print(f"\t\t\t\t{step:2}. {num:2} -> {num:2} - 1 = {num-1:2}")
            num = num - 1

    print(f"\n\t\t\tSteps: {step}\n\n")

print("Function solution:\n")

for num in Input_num:

    step = NumOfSteps_Prt(num)
    print("\t"*4 + f"Steps: {step}")
    print("\t"*5 + "Steps from print fun")

    step = NumOfSteps_Sol(num)
    print("\t"*4 + f"Steps: {step}")
    print("\t"*5 + "Steps from solution fun")
    print("\n")